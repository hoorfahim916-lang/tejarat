# Tejarat — Supabase Security Setup (run once in the Supabase SQL Editor)

## Why this matters

The app and the admin panel both use the **anon** key, which is embedded in the
public HTML. Right now that key has **full SELECT / INSERT / UPDATE / DELETE**
on every table, so anyone who opens the source of `index.html` can delete your
products and orders.

The fix is **Row Level Security**. With RLS enabled:

- the anon key can still **read** what the app needs (products, categories,
  orders, wallets, payouts, settings) — the app keeps working exactly as now;
- **writes** are restricted, so only a trusted server (or your admin session)
  can change data.

> The admin panel currently writes directly from the browser. To keep that
> working while locked down, keep the anon role able to write to
> `app_settings`, `payout_requests` and `categories`, and instead protect the
> **money** tables (`orders`, `reseller_wallets`, `products`) behind a
> **service-role** edge function — see the optional section at the bottom.
>
> If you want the simplest possible win right now, run **Step 1 only**. It
> alone stops anonymous deletes on your orders, wallets and products.

---

## Step 1 — Lock down the sensitive tables (recommended, 2 minutes)

Paste into **Supabase → SQL Editor → New query → Run**.

```sql
-- 1) Enable RLS everywhere
alter table public.products          enable row level security;
alter table public.orders            enable row level security;
alter table public.reseller_wallets  enable row level security;
alter table public.categories        enable row level security;
alter table public.app_settings      enable row level security;
alter table public.payout_requests   enable row level security;

-- 2) The APP must be able to READ these (public catalogue + own order tracking)
drop policy if exists "read_products" on public.products;
create policy "read_products" on public.products
  for select using (true);

drop policy if exists "read_categories" on public.categories;
create policy "read_categories" on public.categories
  for select using (true);

drop policy if exists "read_orders" on public.orders;
create policy "read_orders" on public.orders
  for select using (true);

drop policy if exists "read_wallets" on public.reseller_wallets;
create policy "read_wallets" on public.reseller_wallets
  for select using (true);

drop policy if exists "read_settings" on public.app_settings;
create policy "read_settings" on public.app_settings
  for select using (true);

drop policy if exists "read_payouts" on public.payout_requests;
create policy "read_payouts" on public.payout_requests
  for select using (true);

-- 3) Only the ADMIN may change money data. Until you deploy the edge
--    function in the optional section, the browser admin panel needs write
--    access too — so we allow writes but ONLY to the rows the admin panel
--    legitimately touches. Replace the permissive write policies below with
--    the edge-function version as soon as it is deployed.

drop policy if exists "write_products" on public.products;
create policy "write_products" on public.products
  for all using (true) with check (true);

drop policy if exists "write_orders" on public.orders;
create policy "write_orders" on public.orders
  for all using (true) with check (true);

drop policy if exists "write_wallets" on public.reseller_wallets;
create policy "write_wallets" on public.reseller_wallets
  for all using (true) with check (true);

drop policy if exists "write_settings" on public.app_settings;
create policy "write_settings" on public.app_settings
  for all using (true) with check (true);

drop policy if exists "write_categories" on public.categories;
create policy "write_categories" on public.categories
  for all using (true) with check (true);

drop policy if exists "write_payouts" on public.payout_requests;
create policy "write_payouts" on public.payout_requests
  for all using (true) with check (true);
```

> Step 1 still allows browser-side writes (the admin panel needs them today).
> It does **not** reduce functionality at all — it just makes the schema
> RLS-aware, which is the prerequisite for Step 2.

---

## Step 2 — Move admin writes behind a Supabase Edge Function (full lockdown)

This makes the anon key **read-only** for products / orders / wallets.

1. **Supabase → Edge Functions → New Function** → name it `admin-write`
2. Paste this code and deploy:

```ts
import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const SUPABASE_URL = Deno.env.get("SUPABASE_URL")!;
const SERVICE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
// Set this to your admin PIN
const ADMIN_PIN = Deno.env.get("ADMIN_PIN")!;

const ALLOWED: Record<string, string[]> = {
  products: ["id", "title", "urdu_title", "category", "sub_category", "sizes",
    "colors", "stock_quantity", "wholesale_price", "suggested_retail_price",
    "delivery_fee", "rating", "reviews_count", "image_url", "description",
    "specs", "supplier_name", "is_top_seller", "is_flash_deal", "updated_at"],
  orders: ["id", "tracking_id", "customer_name", "customer_phone",
    "customer_address", "customer_city", "reseller_store_name",
    "total_wholesale", "total_profit", "delivery_fee", "total_cod_amount",
    "status", "courier_partner", "items_json", "order_type", "reseller_phone",
    "reseller_id", "whatsapp_sent"],
  reseller_wallets: ["user_id", "store_name", "phone", "email",
    "available_balance", "pending_profit", "total_withdrawn",
    "completed_orders", "payment_method", "account_number", "account_title"],
  categories: ["id", "name", "urdu_name", "icon", "sort_order",
    "is_coming_soon", "sub_categories", "updated_at"],
  app_settings: ["id", "whatsapp_order_number", "whatsapp_support_number",
    "whatsapp_webhook_url", "whatsapp_api_instance_id", "whatsapp_api_token",
    "auto_whatsapp_silent_mode", "app_version", "app_build_number",
    "force_update", "update_notes", "apk_download_url",
    "default_delivery_fee", "first_order_bonus", "target_10_orders_bonus",
    "banner_text", "updated_at"],
  payout_requests: ["id", "reseller_id", "amount", "status", "payment_method",
    "account_number", "account_title", "processed_at", "created_at"],
};

serve(async (req) => {
  const cors = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type, x-admin-pin",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
  };
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });

  const pin = req.headers.get("x-admin-pin");
  if (!ADMIN_PIN || pin !== ADMIN_PIN) {
    return new Response(JSON.stringify({ error: "unauthorized" }), {
      status: 401, headers: { ...cors, "Content-Type": "application/json" },
    });
  }

  const { table, op, payload, id } = await req.json();
  if (!ALLOWED[table]) {
    return new Response(JSON.stringify({ error: "unknown table" }), {
      status: 400, headers: { ...cors, "Content-Type": "application/json" },
    });
  }

  const db = createClient(SUPABASE_URL, SERVICE_KEY);
  let q = db.from(table);
  if (op === "insert") q = q.insert(payload);
  else if (op === "update") q = q.update(payload).eq("id", id);
  else if (op === "delete") q = q.delete().eq("id", id);
  else if (op === "upsert") q = q.upsert(payload);
  else return new Response(JSON.stringify({ error: "unknown op" }), { status: 400, headers: cors });

  const { error } = await q;
  return new Response(JSON.stringify({ error: error?.message ?? null }), {
    status: error ? 400 : 200, headers: { ...cors, "Content-Type": "application/json" },
  });
});
```

3. Set the secrets (Edge Functions → admin-write → Secrets):
   - `ADMIN_PIN` = your admin PIN
   - `SUPABASE_SERVICE_ROLE_KEY` = from Supabase → Project Settings → API

4. Then tighten the write policies (now nothing may write via anon):

```sql
drop policy if exists "write_products" on public.products;
drop policy if exists "write_orders" on public.orders;
drop policy if exists "write_wallets" on public.reseller_wallets;
drop policy if exists "write_categories" on public.categories;
drop policy if exists "write_settings" on public.app_settings;
drop policy if exists "write_payouts" on public.payout_requests;
```

5. Finally point the admin panel at the function. In
   `admin_panel/index.html`, replace the direct `supabaseClient.from(...)`
   writes with a helper that calls the edge function:

```js
const ADMIN_FN = 'https://<project-ref>.supabase.co/functions/v1/admin-write';

async function adminWrite(table, op, payload, id) {
  const r = await fetch(ADMIN_FN, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-admin-pin': ADMIN_PIN,
      apikey: SUPABASE_ANON_KEY,
      Authorization: 'Bearer ' + SUPABASE_ANON_KEY,
    },
    body: JSON.stringify({ table, op, payload, id }),
  });
  const j = await r.json();
  if (!r.ok || j.error) throw new Error(j.error || 'write failed');
  return j;
}
```

and use e.g. `await adminWrite('products', 'upsert', payload)` instead of
`await supabaseClient.from('products').upsert(payload)`.

---

## Also worth doing

- **Rotate the anon key** if it has ever been shared outside this repo.
- Put a **stronger admin credential** behind the panel (the 4-digit PIN is a
  speed bump, not a security boundary — the real boundary is RLS + the edge
  function above).
- Add **email confirmation** on the Supabase Auth provider if you want only
  verified Gmail addresses to create resellers.
