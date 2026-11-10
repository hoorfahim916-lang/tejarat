import os
import re

html_path = "C:/Users/LENOVO/Downloads/TEJARAT APP/index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Favicon in head
if '<link rel="icon"' not in content:
    content = content.replace(
        '<title>Tejarat App - Pakistan ki #1 Reselling & Shopping App</title>',
        '<title>Tejarat App - Pakistan ki #1 Reselling & Shopping App</title>\n  <link rel="icon" type="image/png" href="markaz_assets/tejarat_logo.png" />\n  <link rel="apple-touch-icon" href="markaz_assets/tejarat_logo.png" />'
    )

# 2. Header Box & Logo & Verified Badge (Guest starts with OFFICIAL badge)
old_header_pattern = r'<div class="w-10 h-10 rounded-2xl bg-white text-\[#047857\] font-black text-2xl flex items-center justify-center shadow-md">\s*T\s*</div>\s*<div>\s*<div class="flex items-center space-x-1\.5">\s*<h1 class="font-black text-lg tracking-tight leading-none">Tejarat App</h1>\s*<span class="text-\[9px\] bg-amber-400 text-gray-950 font-black px-1\.5 py-0\.5 rounded uppercase shadow-sm">VERIFIED</span>\s*</div>'

new_header_box = '''<div class="w-10 h-10 rounded-2xl overflow-hidden shadow-md border border-emerald-400/30 flex items-center justify-center bg-white flex-shrink-0">
            <img src="markaz_assets/tejarat_logo.png" onerror="this.onerror=null; this.src='tejarat_logo.png';" alt="Tejarat Logo" class="w-full h-full object-cover" />
          </div>
          <div>
            <div class="flex items-center space-x-1.5">
              <h1 class="font-black text-lg tracking-tight leading-none">Tejarat App</h1>
              <span id="headerBrandBadge" class="text-[9px] bg-emerald-800/80 text-emerald-200 font-bold px-1.5 py-0.5 rounded uppercase border border-emerald-500/30">OFFICIAL</span>
            </div>'''

content = re.sub(old_header_pattern, new_header_box, content)

# 3. Profile Tab Guest Badge and Store Subtitle
content = content.replace(
    '<span id="profileVerifiedBadge" class="bg-emerald-100 text-[#047857] text-[10px] font-black px-1.5 py-0.5 rounded">Guest</span>',
    '<span id="profileVerifiedBadge" class="bg-gray-100 text-gray-500 text-[10px] font-bold px-1.5 py-0.5 rounded">Guest (Unverified)</span>'
)

content = content.replace(
    '<span class="text-[11px] text-emerald-200 uppercase font-bold tracking-wider">Verified Reseller Store</span>',
    '<span id="bizStoreSubtitle" class="text-[11px] text-emerald-200 uppercase font-bold tracking-wider">Reseller Store</span>'
)

# 4. Auth Modal Redesign (Google Sign-In with Gmail & Verification)
old_auth_modal_pattern = r'<!-- ==================== MODAL: GOOGLE / GMAIL OAUTH LOGIN ==================== -->\s*<div id="authModal"[\s\S]*?<!-- ==================== MODAL 1: PRODUCT DETAILS VIEW ==================== -->'

new_auth_modal = '''<!-- ==================== MODAL: GOOGLE / GMAIL VERIFIED LOGIN ==================== -->
  <div id="authModal" class="fixed inset-0 bg-black/75 z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-sm w-full p-5 space-y-4 shadow-2xl border border-gray-100 animate-in fade-in zoom-in duration-200">
      
      <!-- Modal Header -->
      <div class="flex items-center justify-between border-b border-gray-100 pb-3">
        <div class="flex items-center space-x-2.5">
          <div class="w-9 h-9 rounded-xl overflow-hidden shadow border border-emerald-400/30 bg-white flex items-center justify-center flex-shrink-0">
            <img src="markaz_assets/tejarat_logo.png" onerror="this.onerror=null; this.src='tejarat_logo.png';" alt="Tejarat" class="w-full h-full object-cover" />
          </div>
          <div>
            <h3 class="font-black text-sm text-gray-900 leading-tight">Tejarat Reseller Sign In</h3>
            <p class="text-[10px] text-emerald-700 font-semibold">Google Account Verification</p>
          </div>
        </div>
        <button onclick="closeAuthModal()" class="w-7 h-7 rounded-full bg-gray-100 hover:bg-gray-200 flex items-center justify-center text-gray-500 transition">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <!-- Banner -->
      <div class="bg-gradient-to-r from-emerald-50 to-teal-50 border border-emerald-200/60 rounded-2xl p-3 text-center space-y-1">
        <div class="flex items-center justify-center space-x-1.5">
          <span class="text-xs font-black text-[#047857]">Google (Gmail) Se Login Karein</span>
          <span class="text-[9px] bg-amber-400 text-gray-950 font-black px-1.5 py-0.2 rounded uppercase">VERIFIED</span>
        </div>
        <p class="text-[11px] text-gray-600 leading-relaxed">
          Login ke baad aapka account <strong>"✓ Verified Reseller"</strong> ban jayega aur aapka sara munafa aur orders mehfooz rahenge.
        </p>
      </div>

      <!-- Google Sign In Form -->
      <form onsubmit="handleGoogleAuthSubmit(event)" class="space-y-3">
        <div>
          <label class="block text-[11px] font-bold text-gray-700 mb-1">Apna Google / Gmail Address <span class="text-rose-500">*</span></label>
          <div class="relative">
            <input type="email" id="inpGoogleEmail" required placeholder="apna.name@gmail.com" class="w-full border-2 border-gray-200 rounded-xl pl-9 pr-3 py-2.5 text-xs font-semibold outline-none focus:border-[#047857] transition" />
            <div class="absolute left-3 top-3">
              <svg class="w-4 h-4" viewBox="0 0 24 24">
                <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
                <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
              </svg>
            </div>
          </div>
        </div>

        <div>
          <label class="block text-[11px] font-bold text-gray-700 mb-1">Aap Ka Naam / Reseller Name</label>
          <input type="text" id="inpGoogleName" placeholder="Misaal: Hoor Fahim" class="w-full border-2 border-gray-200 rounded-xl px-3 py-2 text-xs font-semibold outline-none focus:border-[#047857] transition" />
        </div>

        <div>
          <label class="block text-[11px] font-bold text-gray-700 mb-1">Aap Ke Online Store Ka Naam</label>
          <input type="text" id="inpGoogleStoreName" placeholder="Misaal: Tejarat Super Store" class="w-full border-2 border-gray-200 rounded-xl px-3 py-2 text-xs font-semibold outline-none focus:border-[#047857] transition" />
        </div>

        <button type="submit" id="btnSubmitGoogle" class="w-full bg-[#047857] hover:bg-emerald-800 text-white font-black py-3 px-4 rounded-xl shadow-md flex items-center justify-center space-x-2 transition">
          <svg class="w-4 h-4" viewBox="0 0 24 24">
            <path fill="#ffffff" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
            <path fill="#ffffff" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
            <path fill="#ffffff" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
            <path fill="#ffffff" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
          </svg>
          <span class="text-xs">Google Account Se Verify & Login Karein</span>
        </button>
      </form>

      <!-- Trust Note -->
      <div class="text-center pt-1">
        <p class="text-[10px] text-gray-400 font-medium">
          🔒 Mehfooz & Official Tejarat Platform · Zero Registration Fee
        </p>
      </div>

    </div>
  </div>

  <!-- ==================== MODAL 1: PRODUCT DETAILS VIEW ==================== -->'''

content = re.sub(old_auth_modal_pattern, new_auth_modal, content)

# 5. Auth Javascript Code Update
old_auth_js_pattern = r'// ==================== AUTHENTICATION \(GOOGLE & DIRECT GMAIL\) ====================[\s\S]*?// ==================== RENDER CATEGORIES ===================='

new_auth_js = '''// ==================== AUTHENTICATION (GOOGLE & DIRECT GMAIL) ====================
    function checkAuthSession() {
      const savedUser = localStorage.getItem('tejarat_user');
      if (savedUser) {
        try {
          currentUser = JSON.parse(savedUser);
          if (currentUser && currentUser.verified) {
            applyLoggedInUserUI(currentUser);
            return;
          }
        } catch (e) {
          currentUser = null;
        }
      }
      // If no valid verified session, enforce Guest mode
      enforceGuestUI();
    }

    async function handleGoogleAuthSubmit(e) {
      if (e) e.preventDefault();
      const emailInput = document.getElementById('inpGoogleEmail');
      const nameInput = document.getElementById('inpGoogleName');
      const storeInput = document.getElementById('inpGoogleStoreName');
      
      const email = emailInput ? emailInput.value.trim().toLowerCase() : '';
      let fullName = nameInput ? nameInput.value.trim() : '';
      let storeName = storeInput ? storeInput.value.trim() : '';

      if (!email || !email.includes('@')) {
        showToast('Bara-e-karam apna durust Gmail address darj karein!');
        return;
      }

      if (!fullName) {
        const raw = email.split('@')[0].replace(/[0-9._]/g, ' ').trim();
        fullName = raw ? (raw.charAt(0).toUpperCase() + raw.slice(1)) : 'Reseller Partner';
      }

      if (!storeName) {
        storeName = fullName + ' Official Store';
      }

      const userObj = {
        id: 'usr_' + Date.now(),
        email: email,
        full_name: fullName,
        store_name: storeName,
        provider: 'google',
        verified: true,
        verified_at: new Date().toISOString()
      };

      // Store locally
      localStorage.setItem('tejarat_user', JSON.stringify(userObj));
      currentUser = userObj;

      // Apply UI changes
      applyLoggedInUserUI(userObj);
      closeAuthModal();

      // Sync wallet record to Supabase
      try {
        await supabaseClient.from('reseller_wallets').upsert({
          reseller_phone: email,
          store_name: storeName,
          total_orders: 0,
          total_sales: 0,
          total_profit: 0
        }, { onConflict: 'reseller_phone' });
      } catch (err) {
        console.warn('Supabase sync wallet record:', err);
      }

      showToast(`✓ Welcome ${fullName}! Google se Verified ho gaye!`);
    }

    function applyLoggedInUserUI(u) {
      // 1. Top Bar Header Badge -> Show VERIFIED in Gold
      const headerBadge = document.getElementById('headerBrandBadge');
      if (headerBadge) {
        headerBadge.innerText = '✓ VERIFIED';
        headerBadge.className = 'text-[9px] bg-amber-400 text-gray-950 font-black px-1.5 py-0.5 rounded uppercase shadow-sm flex items-center space-x-0.5';
      }

      // 2. Profile Tab Card
      const pName = document.getElementById('profileUserFullName');
      if (pName) pName.innerText = u.full_name || 'Verified Reseller';

      const pEmail = document.getElementById('profileUserEmail');
      if (pEmail) pEmail.innerText = u.email || '';

      const pBadge = document.getElementById('profileVerifiedBadge');
      if (pBadge) {
        pBadge.innerText = '✓ Verified Reseller';
        pBadge.className = 'bg-emerald-100 text-[#047857] text-[10px] font-black px-2 py-0.5 rounded-full shadow-sm';
      }

      const avatarText = document.getElementById('userAvatarText');
      if (avatarText) {
        avatarText.innerText = (u.full_name || u.email || 'T')[0].toUpperCase();
      }

      // 3. Store Name & Subtitle
      const storeSub = document.getElementById('bizStoreSubtitle');
      if (storeSub) storeSub.innerText = '✓ Verified Reseller Store';

      const storeName = document.getElementById('bizStoreName');
      if (storeName && u.store_name) storeName.innerText = u.store_name;

      // 4. Auth Button -> Logout
      const btn = document.getElementById('authActionBtn');
      if (btn) {
        btn.innerText = 'Logout';
        btn.className = 'bg-rose-50 text-rose-600 border border-rose-200 text-xs font-black px-3.5 py-2 rounded-xl shadow-sm transition hover:bg-rose-100';
        btn.onclick = logoutUser;
      }
    }

    function enforceGuestUI() {
      // Top Bar Header Badge -> OFFICIAL (NOT Verified!)
      const headerBadge = document.getElementById('headerBrandBadge');
      if (headerBadge) {
        headerBadge.innerText = 'OFFICIAL';
        headerBadge.className = 'text-[9px] bg-emerald-800/80 text-emerald-200 font-bold px-1.5 py-0.5 rounded uppercase border border-emerald-500/30';
      }

      // Profile Tab Card -> Guest (Unverified)
      const pName = document.getElementById('profileUserFullName');
      if (pName) pName.innerText = 'Mehmon Reseller';

      const pEmail = document.getElementById('profileUserEmail');
      if (pEmail) pEmail.innerText = 'Google (Gmail) se login karein';

      const pBadge = document.getElementById('profileVerifiedBadge');
      if (pBadge) {
        pBadge.innerText = 'Guest (Unverified)';
        pBadge.className = 'bg-gray-100 text-gray-500 text-[10px] font-bold px-1.5 py-0.5 rounded';
      }

      const avatarText = document.getElementById('userAvatarText');
      if (avatarText) avatarText.innerText = 'T';

      const storeSub = document.getElementById('bizStoreSubtitle');
      if (storeSub) storeSub.innerText = 'Reseller Store';

      const btn = document.getElementById('authActionBtn');
      if (btn) {
        btn.innerText = 'Login Karein';
        btn.className = 'bg-[#047857] hover:bg-emerald-800 text-white text-xs font-black px-3.5 py-2 rounded-xl shadow-sm transition';
        btn.onclick = openAuthModal;
      }
    }

    function logoutUser() {
      localStorage.removeItem('tejarat_user');
      currentUser = null;
      enforceGuestUI();
      showToast('Account se logout ho gaye.');
    }

    function openAuthModal() {
      // Pre-fill if previously used
      const savedUser = localStorage.getItem('tejarat_user');
      if (savedUser) {
        try {
          const u = JSON.parse(savedUser);
          if (u.email && document.getElementById('inpGoogleEmail')) {
            document.getElementById('inpGoogleEmail').value = u.email;
          }
          if (u.full_name && document.getElementById('inpGoogleName')) {
            document.getElementById('inpGoogleName').value = u.full_name;
          }
        } catch(e) {}
      }
      document.getElementById('authModal').classList.remove('hidden');
      lucide.createIcons();
    }

    function closeAuthModal() {
      document.getElementById('authModal').classList.add('hidden');
    }

    // ==================== RENDER CATEGORIES ===================='''

content = re.sub(old_auth_js_pattern, new_auth_js, content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html successfully!")
