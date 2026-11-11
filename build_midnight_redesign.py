import re

html_path = "C:/Users/LENOVO/Downloads/TEJARAT APP/index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Header to Midnight Navy & Heavy Gold
old_header_tag = r'<header class="bg-gradient-to-r from-\[#065F46\] via-\[#047857\] to-\[#0D9488\] text-white sticky top-0 z-30 shadow-md top-safe-header">'
new_header_tag = '<header class="bg-gradient-to-r from-[#030712] via-[#0F172A] to-[#1E293B] text-white sticky top-0 z-30 shadow-lg border-b border-amber-500/25 top-safe-header">'
content = re.sub(old_header_tag, new_header_tag, content)

# 2. Update Default Theme in JS to Navy & Gold
content = content.replace("localStorage.getItem('tejarat_theme') || 'green'", "localStorage.getItem('tejarat_theme') || 'navy'")

# 3. Replace Profile / Business Tab (#tab-business) with Screenshot 1 Architecture
old_business_tab_regex = r'<div id="tab-business" class="tab-view hidden px-4 py-4 space-y-4">[\s\S]*?<!-- ==================== BOTTOM NAVIGATION BAR ==================== -->'

new_business_tab = '''<div id="tab-business" class="tab-view hidden px-4 py-3.5 space-y-3.5 pb-24">
        
        <!-- User Login / Profile Card -->
        <div id="userProfileHeaderCard" class="bg-white rounded-3xl p-4 shadow-sm border border-gray-100 flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <div id="userAvatarBox" class="w-12 h-12 rounded-2xl bg-gradient-to-br from-slate-900 to-slate-800 text-amber-400 font-black text-xl flex items-center justify-center shadow-md border border-amber-500/30">
              <span id="userAvatarText">T</span>
            </div>
            <div>
              <div class="flex items-center space-x-1.5">
                <h3 id="profileUserFullName" class="font-black text-sm text-gray-900">Mehmon Reseller</h3>
                <span id="profileVerifiedBadge" class="bg-gray-100 text-gray-500 text-[10px] font-bold px-1.5 py-0.5 rounded">Guest (Unverified)</span>
              </div>
              <p id="profileUserEmail" class="text-xs text-gray-500 font-medium mt-0.5">Gmail se login karein</p>
            </div>
          </div>
          <div>
            <button id="authActionBtn" onclick="openAuthModal()" class="bg-amber-400 hover:bg-amber-500 text-gray-950 text-xs font-black px-3.5 py-2 rounded-xl shadow-md transition">
              Login Karein
            </button>
          </div>
        </div>

        <!-- MIDNIGHT NAVY & GOLD RESELLER METRICS CARD (SCREENSHOT 1 STYLE) -->
        <div class="rounded-3xl p-5 text-white shadow-xl relative overflow-hidden border border-amber-500/30 bg-gradient-to-br from-[#030712] via-[#0F172A] to-[#1E293B]">
          <!-- Ambient Gold Glow -->
          <div class="absolute -top-12 -right-12 w-36 h-36 bg-amber-500/15 rounded-full blur-2xl pointer-events-none"></div>

          <!-- Top Dropdown & Store Title -->
          <div class="flex items-center justify-between relative z-10">
            <div>
              <span id="bizStoreSubtitle" class="text-[10px] text-amber-300 uppercase font-black tracking-wider">Verified Reseller Store</span>
              <h2 id="bizStoreName" class="text-lg font-black mt-0.5 text-white">Mera Online Store</h2>
            </div>
            <!-- All Time Dropdown Filter -->
            <div class="relative">
              <select id="selTimeMetrics" onchange="setTimeMetrics(this.value)" class="bg-white/10 hover:bg-white/15 border border-white/20 text-white text-xs font-bold px-3 py-1.5 rounded-xl outline-none transition cursor-pointer appearance-none pr-7">
                <option value="all" class="text-gray-900 bg-white">All Time ⌵</option>
                <option value="month" class="text-gray-900 bg-white">This Month ⌵</option>
              </select>
              <i data-lucide="chevron-down" class="w-3.5 h-3.5 text-amber-300 absolute right-2.5 top-2.5 pointer-events-none"></i>
            </div>
          </div>

          <!-- Total Sales (Hero Metric) -->
          <div class="text-center py-3 relative z-10">
            <h1 id="bizMetricSales" class="text-3xl font-black text-white tracking-tight">Rs. 0</h1>
            <p class="text-xs font-semibold text-gray-300 mt-0.5">Total Sales</p>
          </div>

          <!-- 3-Sub Metrics Row -->
          <div class="grid grid-cols-3 gap-2 pt-3 border-t border-white/10 text-center relative z-10 bg-black/25 rounded-2xl p-2.5 backdrop-blur-sm">
            <div>
              <h4 id="bizMetricOrders" class="text-sm font-black text-white">0</h4>
              <p class="text-[10px] text-gray-400 font-medium mt-0.5">Completed Orders</p>
            </div>
            <div class="border-x border-white/10">
              <h4 id="bizMetricProfit" class="text-sm font-black text-amber-400">Rs. 0</h4>
              <p class="text-[10px] text-amber-300/80 font-medium mt-0.5">Total Profit</p>
            </div>
            <div>
              <h4 id="bizMetricBonus" class="text-sm font-black text-emerald-400">Rs. 0</h4>
              <p class="text-[10px] text-gray-400 font-medium mt-0.5">Total Bonus</p>
            </div>
          </div>
        </div>

        <!-- TWO SIDE-BY-SIDE CARDS: MERI PAYMENTS & MERI OFFERS (SCREENSHOT 1 EXACT RECREATION) -->
        <div class="grid grid-cols-2 gap-3">
          <!-- Card 1: Meri Payments -->
          <div onclick="openMeriPaymentsModal()" class="bg-white rounded-3xl p-4 shadow-sm border border-gray-100 hover:border-amber-400/50 hover:shadow-md transition cursor-pointer flex flex-col items-center text-center space-y-2 group">
            <div class="w-14 h-14 rounded-2xl bg-amber-50 flex items-center justify-center shadow-inner group-hover:scale-105 transition">
              <span class="text-3xl">👝</span>
            </div>
            <div>
              <h4 class="font-black text-sm text-gray-900 leading-tight">Meri Payments</h4>
              <p class="text-[10px] text-emerald-600 font-bold mt-0.5">Auto-Transfer Status</p>
            </div>
          </div>

          <!-- Card 2: Meri Offers -->
          <div onclick="openMeriOffersModal()" class="bg-white rounded-3xl p-4 shadow-sm border border-gray-100 hover:border-amber-400/50 hover:shadow-md transition cursor-pointer flex flex-col items-center text-center space-y-2 group">
            <div class="w-14 h-14 rounded-2xl bg-amber-50 flex items-center justify-center shadow-inner group-hover:scale-105 transition">
              <span class="text-3xl">💵</span>
            </div>
            <div>
              <h4 class="font-black text-sm text-gray-900 leading-tight">Meri Offers</h4>
              <p class="text-[10px] text-amber-600 font-bold mt-0.5">Rs. 1,100 Bonus Target</p>
            </div>
          </div>
        </div>

        <!-- ACCOUNT MENU SECTION (SCREENSHOT 1 STRUCTURE) -->
        <div class="bg-white rounded-3xl shadow-sm border border-gray-100 overflow-hidden divide-y divide-gray-100">
          <div class="px-4 py-3 bg-gray-50/70 border-b border-gray-100">
            <h3 class="text-xs font-black text-gray-800 uppercase tracking-wider">Account Settings</h3>
          </div>

          <!-- 1. Business Details -->
          <button onclick="openBusinessDetailsModal()" class="w-full px-4 py-3.5 flex items-center justify-between hover:bg-gray-50 transition text-left group">
            <div class="flex items-center space-x-3">
              <div class="w-9 h-9 rounded-xl bg-slate-100 flex items-center justify-center text-slate-700 group-hover:bg-amber-100 group-hover:text-amber-800 transition">
                <i data-lucide="store" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="text-xs font-bold text-gray-800">Business Details</h4>
                <p id="subBizName" class="text-[10px] text-gray-500">Mera Online Store · Profile Info</p>
              </div>
            </div>
            <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400 group-hover:translate-x-0.5 transition"></i>
          </button>

          <!-- 2. Profit Account (Add Account for Withdraw) -->
          <button onclick="openProfitAccountModal()" class="w-full px-4 py-3.5 flex items-center justify-between hover:bg-gray-50 transition text-left group">
            <div class="flex items-center space-x-3">
              <div class="w-9 h-9 rounded-xl bg-amber-50 flex items-center justify-center text-amber-700 group-hover:bg-amber-100 transition">
                <i data-lucide="credit-card" class="w-4 h-4"></i>
              </div>
              <div>
                <div class="flex items-center space-x-1.5">
                  <h4 class="text-xs font-bold text-gray-800">Profit Account (Withdrawal)</h4>
                  <span id="badgeProfitSet" class="text-[9px] bg-amber-100 text-amber-900 font-bold px-1.5 py-0.2 rounded">Set Karein</span>
                </div>
                <p id="subProfitAccount" class="text-[10px] text-gray-500">EasyPaisa, JazzCash, Meezan, HBL</p>
              </div>
            </div>
            <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400 group-hover:translate-x-0.5 transition"></i>
          </button>

          <!-- 3. Followed Shops -->
          <button onclick="showToast('Followed Shops: Aap ne Tejarat Wholesale Hub ko follow kiya hua hai.')" class="w-full px-4 py-3.5 flex items-center justify-between hover:bg-gray-50 transition text-left group">
            <div class="flex items-center space-x-3">
              <div class="w-9 h-9 rounded-xl bg-slate-100 flex items-center justify-center text-slate-700">
                <i data-lucide="shopping-bag" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="text-xs font-bold text-gray-800">Followed Shops</h4>
                <p class="text-[10px] text-gray-500">1 Verified Wholesale Supplier</p>
              </div>
            </div>
            <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400"></i>
          </button>

          <!-- 4. Catalogs Viewed -->
          <button onclick="switchTab('categories')" class="w-full px-4 py-3.5 flex items-center justify-between hover:bg-gray-50 transition text-left group">
            <div class="flex items-center space-x-3">
              <div class="w-9 h-9 rounded-xl bg-slate-100 flex items-center justify-center text-slate-700">
                <i data-lucide="grid" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="text-xs font-bold text-gray-800">Catalogs Viewed</h4>
                <p class="text-[10px] text-gray-500">Dry Fruits, Sidr Honey, Desi Ghee</p>
              </div>
            </div>
            <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400"></i>
          </button>

          <!-- 5. My Favorites -->
          <button onclick="openFavoritesModal()" class="w-full px-4 py-3.5 flex items-center justify-between hover:bg-gray-50 transition text-left group">
            <div class="flex items-center space-x-3">
              <div class="w-9 h-9 rounded-xl bg-rose-50 flex items-center justify-center text-rose-600">
                <i data-lucide="heart" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="text-xs font-bold text-gray-800">My Favorites</h4>
                <p class="text-[10px] text-gray-500">Pasandeeda products list</p>
              </div>
            </div>
            <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400"></i>
          </button>

          <!-- 6. My Shares -->
          <button onclick="showToast('My Shares: Aap ne 0 products WhatsApp par share kiye hain.')" class="w-full px-4 py-3.5 flex items-center justify-between hover:bg-gray-50 transition text-left group">
            <div class="flex items-center space-x-3">
              <div class="w-9 h-9 rounded-xl bg-slate-100 flex items-center justify-center text-slate-700">
                <i data-lucide="share-2" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="text-xs font-bold text-gray-800">My Shares</h4>
                <p class="text-[10px] text-gray-500">Customers ke sath share ki gayi items</p>
              </div>
            </div>
            <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400"></i>
          </button>

          <!-- 7. Help & Support -->
          <button onclick="openChatbotModal()" class="w-full px-4 py-3.5 flex items-center justify-between hover:bg-gray-50 transition text-left group">
            <div class="flex items-center space-x-3">
              <div class="w-9 h-9 rounded-xl bg-emerald-50 flex items-center justify-center text-[#047857]">
                <i data-lucide="help-circle" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="text-xs font-bold text-gray-800">Help & Support (24/7 Helpline)</h4>
                <p class="text-[10px] text-gray-500">WhatsApp: 03190328256</p>
              </div>
            </div>
            <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400"></i>
          </button>
        </div>

      </div>

      <!-- ==================== BOTTOM NAVIGATION BAR ===================='''

content = re.sub(old_business_tab_regex, new_business_tab, content)

# 4. Replace Orders Tab (#tab-orders) with Screenshot 2 Architecture (8 Lifecycle Stages)
old_orders_tab_regex = r'<div id="tab-orders" class="tab-view hidden px-4 py-4 space-y-3\.5">[\s\S]*?<div id="ordersListContainer" class="space-y-3"></div>\s*</div>'

new_orders_tab = '''<div id="tab-orders" class="tab-view hidden px-4 py-3.5 space-y-3.5 pb-24">
        
        <!-- Header Card -->
        <div class="bg-white rounded-3xl p-4 shadow-sm border border-gray-100 flex items-center justify-between">
          <div>
            <h2 class="text-base font-black text-gray-900 leading-tight">Mere Orders (Tracking)</h2>
            <p class="text-xs text-gray-500">Har order ka live status aur munafa yahan check karein</p>
          </div>
          <button onclick="fetchAllCloudData(true)" class="text-xs font-bold text-slate-900 bg-amber-100 px-3 py-1.5 rounded-xl flex items-center space-x-1 transition hover:bg-amber-200">
            <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
            <span>Refresh</span>
          </button>
        </div>

        <!-- 8 ORDER STATUS LIFECYCLE LIST (SCREENSHOT 2 EXACT RECREATION) -->
        <div class="bg-white rounded-3xl shadow-sm border border-gray-100 overflow-hidden divide-y divide-gray-100">
          
          <!-- 1. Verification Pending -->
          <div onclick="filterOrdersByStage('Verification Pending')" class="px-4 py-3.5 flex items-center justify-between hover:bg-gray-50 cursor-pointer transition group">
            <div class="flex items-center space-x-3.5">
              <div class="w-10 h-10 rounded-full bg-rose-50 border border-rose-100 flex items-center justify-center text-rose-500 shadow-sm flex-shrink-0">
                <i data-lucide="phone-call" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="text-xs font-bold text-gray-900">Verification Pending</h4>
                <p class="text-[10px] text-gray-500">Customer ko call / confirmation pending</p>
              </div>
            </div>
            <div class="flex items-center space-x-2">
              <span id="badgeCountPending" class="text-xs font-black text-gray-600 bg-gray-100 px-2 py-0.5 rounded-full">0</span>
              <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400 group-hover:translate-x-0.5 transition"></i>
            </div>
          </div>

          <!-- 2. Verification Failed -->
          <div onclick="filterOrdersByStage('Verification Failed')" class="px-4 py-3.5 flex items-center justify-between hover:bg-gray-50 cursor-pointer transition group">
            <div class="flex items-center space-x-3.5">
              <div class="w-10 h-10 rounded-full bg-amber-50 border border-amber-100 flex items-center justify-center text-amber-600 shadow-sm flex-shrink-0">
                <i data-lucide="alert-circle" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="text-xs font-bold text-gray-900">Verification Failed</h4>
                <p class="text-[10px] text-gray-500">Customer number band ya incorrect address</p>
              </div>
            </div>
            <div class="flex items-center space-x-2">
              <span id="badgeCountFailed" class="text-xs font-black text-gray-600 bg-gray-100 px-2 py-0.5 rounded-full">0</span>
              <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400 group-hover:translate-x-0.5 transition"></i>
            </div>
          </div>

          <!-- 3. In-progress -->
          <div onclick="filterOrdersByStage('In-progress')" class="px-4 py-3.5 flex items-center justify-between hover:bg-gray-50 cursor-pointer transition group">
            <div class="flex items-center space-x-3.5">
              <div class="w-10 h-10 rounded-full bg-blue-50 border border-blue-100 flex items-center justify-center text-blue-600 shadow-sm flex-shrink-0">
                <i data-lucide="truck" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="text-xs font-bold text-gray-900">In-progress</h4>
                <p class="text-[10px] text-gray-500">Warehouse mein packing aur dispatch tayyari</p>
              </div>
            </div>
            <div class="flex items-center space-x-2">
              <span id="badgeCountInProgress" class="text-xs font-black text-gray-600 bg-gray-100 px-2 py-0.5 rounded-full">0</span>
              <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400 group-hover:translate-x-0.5 transition"></i>
            </div>
          </div>

          <!-- 4. Shipper's Advice -->
          <div onclick="filterOrdersByStage('Shipper Advice')" class="px-4 py-3.5 flex items-center justify-between hover:bg-gray-50 cursor-pointer transition group">
            <div class="flex items-center space-x-3.5">
              <div class="w-10 h-10 rounded-full bg-orange-50 border border-orange-100 flex items-center justify-center text-orange-600 shadow-sm flex-shrink-0">
                <i data-lucide="alert-triangle" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="text-xs font-bold text-gray-900">Shipper's Advice</h4>
                <p class="text-[10px] text-gray-500">Courier company se update / issue</p>
              </div>
            </div>
            <div class="flex items-center space-x-2">
              <span id="badgeCountAdvice" class="text-xs font-black text-gray-600 bg-gray-100 px-2 py-0.5 rounded-full">0</span>
              <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400 group-hover:translate-x-0.5 transition"></i>
            </div>
          </div>

          <!-- 5. Out for Delivery -->
          <div onclick="filterOrdersByStage('Out for Delivery')" class="px-4 py-3.5 flex items-center justify-between hover:bg-gray-50 cursor-pointer transition group">
            <div class="flex items-center space-x-3.5">
              <div class="w-10 h-10 rounded-full bg-purple-50 border border-purple-100 flex items-center justify-center text-purple-600 shadow-sm flex-shrink-0">
                <i data-lucide="package" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="text-xs font-bold text-gray-900">Out for Delivery</h4>
                <p class="text-[10px] text-gray-500">Rider customer ke address par pohanch raha hai</p>
              </div>
            </div>
            <div class="flex items-center space-x-2">
              <span id="badgeCountOutForDelivery" class="text-xs font-black text-gray-600 bg-gray-100 px-2 py-0.5 rounded-full">0</span>
              <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400 group-hover:translate-x-0.5 transition"></i>
            </div>
          </div>

          <!-- 6. Delivered -->
          <div onclick="filterOrdersByStage('Delivered')" class="px-4 py-3.5 flex items-center justify-between hover:bg-gray-50 cursor-pointer transition group">
            <div class="flex items-center space-x-3.5">
              <div class="w-10 h-10 rounded-full bg-emerald-50 border border-emerald-100 flex items-center justify-center text-emerald-600 shadow-sm flex-shrink-0">
                <i data-lucide="check-circle-2" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="text-xs font-bold text-gray-900">Delivered</h4>
                <p class="text-[10px] text-emerald-600 font-semibold">Kamyab delivery · Munafa wallet mein transfer</p>
              </div>
            </div>
            <div class="flex items-center space-x-2">
              <span id="badgeCountDelivered" class="text-xs font-black text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded-full">0</span>
              <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400 group-hover:translate-x-0.5 transition"></i>
            </div>
          </div>

          <!-- 7. Returned -->
          <div onclick="filterOrdersByStage('Returned')" class="px-4 py-3.5 flex items-center justify-between hover:bg-gray-50 cursor-pointer transition group">
            <div class="flex items-center space-x-3.5">
              <div class="w-10 h-10 rounded-full bg-gray-100 border border-gray-200 flex items-center justify-center text-gray-600 shadow-sm flex-shrink-0">
                <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="text-xs font-bold text-gray-900">Returned</h4>
                <p class="text-[10px] text-gray-500">Customer ne parcel return kar diya</p>
              </div>
            </div>
            <div class="flex items-center space-x-2">
              <span id="badgeCountReturned" class="text-xs font-black text-gray-600 bg-gray-100 px-2 py-0.5 rounded-full">0</span>
              <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400 group-hover:translate-x-0.5 transition"></i>
            </div>
          </div>

          <!-- 8. Cancelled -->
          <div onclick="filterOrdersByStage('Cancelled')" class="px-4 py-3.5 flex items-center justify-between hover:bg-gray-50 cursor-pointer transition group">
            <div class="flex items-center space-x-3.5">
              <div class="w-10 h-10 rounded-full bg-red-50 border border-red-100 flex items-center justify-center text-red-600 shadow-sm flex-shrink-0">
                <i data-lucide="x-circle" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="text-xs font-bold text-gray-900">Cancelled</h4>
                <p class="text-[10px] text-gray-500">Order cancel kar diya gaya</p>
              </div>
            </div>
            <div class="flex items-center space-x-2">
              <span id="badgeCountCancelled" class="text-xs font-black text-gray-600 bg-gray-100 px-2 py-0.5 rounded-full">0</span>
              <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400 group-hover:translate-x-0.5 transition"></i>
            </div>
          </div>

        </div>

        <!-- Orders Detailed List Container (When Stage Selected) -->
        <div id="ordersStageView" class="space-y-3 hidden">
          <div class="flex items-center justify-between px-1">
            <button onclick="backToOrdersStages()" class="text-xs font-bold text-amber-500 flex items-center space-x-1 hover:underline">
              <i data-lucide="arrow-left" class="w-4 h-4"></i>
              <span>Tamam Stages Par Wapis</span>
            </button>
            <span id="lblCurrentStageTitle" class="text-xs font-black text-gray-900"></span>
          </div>
          <div id="ordersListContainer" class="space-y-3"></div>
        </div>

      </div>'''

content = re.sub(old_orders_tab_regex, new_orders_tab, content)

# 5. Add All Dedicated Modals: Profit Account (Bank & Wallets), Meri Payments, Meri Offers, Business Details
dedicated_modals_html = '''
  <!-- ==================== MODAL: ADD / EDIT PROFIT ACCOUNT (WITHDRAWAL) ==================== -->
  <div id="profitAccountModal" class="fixed inset-0 bg-black/75 z-50 hidden flex items-center justify-center p-3">
    <div class="bg-white rounded-3xl max-w-sm w-full p-5 space-y-4 shadow-2xl border border-gray-100 max-h-[92vh] overflow-y-auto animate-in fade-in zoom-in duration-150">
      
      <div class="flex items-center justify-between border-b pb-3">
        <div class="flex items-center space-x-2">
          <div class="w-9 h-9 rounded-xl bg-amber-50 border border-amber-200 flex items-center justify-center text-amber-700">
            <i data-lucide="landmark" class="w-5 h-5"></i>
          </div>
          <div>
            <h3 class="font-black text-sm text-gray-900">Add Account for Withdraw</h3>
            <p class="text-[10px] text-gray-500">Apna munafa hasil karne ke liye account darj karein</p>
          </div>
        </div>
        <button onclick="closeProfitAccountModal()" class="w-7 h-7 rounded-full bg-gray-100 hover:bg-gray-200 flex items-center justify-center text-gray-500">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <!-- Trust Note -->
      <div class="bg-amber-50 border border-amber-200 rounded-2xl p-3 text-xs text-amber-900 leading-relaxed">
        <strong>100% Free Auto-Payout:</strong> Admin har hafte aap ka verified munafa is account mein direct transfer karega.
      </div>

      <!-- Step 1: Choose Wallet or Bank -->
      <div>
        <label class="block text-[11px] font-bold text-gray-700 mb-1.5">Payment Method / Bank Chunein <span class="text-rose-500">*</span></label>
        <div class="grid grid-cols-2 gap-2 text-xs font-bold max-h-48 overflow-y-auto p-1 border rounded-2xl">
          
          <button type="button" onclick="selectPayoutBank('EasyPaisa', '🟢 EasyPaisa (Telenor)')" class="payout-bank-btn p-2.5 rounded-xl border flex items-center space-x-2 hover:bg-amber-50 transition border-amber-400 bg-amber-50/50" data-bank="EasyPaisa">
            <span class="w-6 h-6 rounded-lg bg-emerald-600 text-white flex items-center justify-center text-[10px] font-black">EP</span>
            <span class="text-[11px] text-gray-900">EasyPaisa</span>
          </button>

          <button type="button" onclick="selectPayoutBank('JazzCash', '🔴 JazzCash (Mobilink)')" class="payout-bank-btn p-2.5 rounded-xl border flex items-center space-x-2 hover:bg-amber-50 transition border-gray-200" data-bank="JazzCash">
            <span class="w-6 h-6 rounded-lg bg-red-600 text-white flex items-center justify-center text-[10px] font-black">JC</span>
            <span class="text-[11px] text-gray-900">JazzCash</span>
          </button>

          <button type="button" onclick="selectPayoutBank('SadaPay', '🟣 SadaPay Wallet')" class="payout-bank-btn p-2.5 rounded-xl border flex items-center space-x-2 hover:bg-amber-50 transition border-gray-200" data-bank="SadaPay">
            <span class="w-6 h-6 rounded-lg bg-teal-600 text-white flex items-center justify-center text-[10px] font-black">SP</span>
            <span class="text-[11px] text-gray-900">SadaPay</span>
          </button>

          <button type="button" onclick="selectPayoutBank('NayaPay', '🟠 NayaPay Wallet')" class="payout-bank-btn p-2.5 rounded-xl border flex items-center space-x-2 hover:bg-amber-50 transition border-gray-200" data-bank="NayaPay">
            <span class="w-6 h-6 rounded-lg bg-orange-500 text-white flex items-center justify-center text-[10px] font-black">NP</span>
            <span class="text-[11px] text-gray-900">NayaPay</span>
          </button>

          <button type="button" onclick="selectPayoutBank('Meezan Bank', '🟩 Meezan Bank Limited')" class="payout-bank-btn p-2.5 rounded-xl border flex items-center space-x-2 hover:bg-amber-50 transition border-gray-200" data-bank="Meezan Bank">
            <span class="w-6 h-6 rounded-lg bg-emerald-800 text-amber-300 flex items-center justify-center text-[10px] font-black">MZN</span>
            <span class="text-[11px] text-gray-900">Meezan Bank</span>
          </button>

          <button type="button" onclick="selectPayoutBank('HBL', '🔵 Habib Bank Limited (HBL)')" class="payout-bank-btn p-2.5 rounded-xl border flex items-center space-x-2 hover:bg-amber-50 transition border-gray-200" data-bank="HBL">
            <span class="w-6 h-6 rounded-lg bg-green-700 text-white flex items-center justify-center text-[10px] font-black">HBL</span>
            <span class="text-[11px] text-gray-900">HBL Bank</span>
          </button>

          <button type="button" onclick="selectPayoutBank('UBL', '🟦 United Bank Limited (UBL)')" class="payout-bank-btn p-2.5 rounded-xl border flex items-center space-x-2 hover:bg-amber-50 transition border-gray-200" data-bank="UBL">
            <span class="w-6 h-6 rounded-lg bg-blue-700 text-white flex items-center justify-center text-[10px] font-black">UBL</span>
            <span class="text-[11px] text-gray-900">UBL Bank</span>
          </button>

          <button type="button" onclick="selectPayoutBank('Bank Alfalah', '🔴 Bank Alfalah')" class="payout-bank-btn p-2.5 rounded-xl border flex items-center space-x-2 hover:bg-amber-50 transition border-gray-200" data-bank="Bank Alfalah">
            <span class="w-6 h-6 rounded-lg bg-red-700 text-white flex items-center justify-center text-[10px] font-black">BA</span>
            <span class="text-[11px] text-gray-900">Bank Alfalah</span>
          </button>

        </div>
      </div>

      <!-- Step 2: Account Holder Inputs -->
      <form onsubmit="saveProfitAccount(event)" class="space-y-3 pt-1">
        <div>
          <label class="block text-[11px] font-bold text-gray-700 mb-1">Muntakhab Shuda Bank / Wallet</label>
          <input type="text" id="lblSelectedBank" readonly value="🟢 EasyPaisa (Telenor)" class="w-full bg-gray-50 border-2 border-gray-200 rounded-xl px-3 py-2 text-xs font-bold text-gray-800 outline-none" />
        </div>

        <div>
          <label class="block text-[11px] font-bold text-gray-700 mb-1">Account Holder Ka Asal Naam <span class="text-rose-500">*</span></label>
          <input type="text" id="inpPayoutAccountTitle" required placeholder="Misaal: Hoor Fahim" class="w-full border-2 border-gray-200 rounded-xl px-3 py-2 text-xs font-semibold outline-none focus:border-amber-500 transition" />
          <p class="text-[10px] text-gray-400 mt-0.5">Jo naam aap ke bank ya wallet par registered hai</p>
        </div>

        <div>
          <label class="block text-[11px] font-bold text-gray-700 mb-1">Account Number / Mobile Number / IBAN <span class="text-rose-500">*</span></label>
          <input type="text" id="inpPayoutAccountNumber" required placeholder="Jaise: 03222089610 ya PK12MEZN..." class="w-full border-2 border-gray-200 rounded-xl px-3 py-2 text-xs font-mono font-bold outline-none focus:border-amber-500 transition" />
        </div>

        <div>
          <label class="block text-[11px] font-bold text-gray-700 mb-1">CNIC Number / Tareekh-e-Pedaish (Optional)</label>
          <input type="text" id="inpPayoutCnic" placeholder="42101-xxxxxxx-x" class="w-full border-2 border-gray-200 rounded-xl px-3 py-2 text-xs font-mono outline-none focus:border-amber-500 transition" />
        </div>

        <button type="submit" id="btnSavePayoutAccount" class="w-full bg-amber-400 hover:bg-amber-500 text-gray-950 font-black py-3 px-4 rounded-xl shadow-md flex items-center justify-center space-x-2 transition active:scale-95">
          <i data-lucide="check-circle" class="w-4 h-4"></i>
          <span>Save Account for Withdraw</span>
        </button>
      </form>

    </div>
  </div>

  <!-- ==================== MODAL: MERI PAYMENTS (DETAIL SHEET) ==================== -->
  <div id="meriPaymentsModal" class="fixed inset-0 bg-black/75 z-50 hidden flex items-center justify-center p-3">
    <div class="bg-white rounded-3xl max-w-sm w-full p-5 space-y-4 shadow-2xl border border-gray-100 max-h-[90vh] overflow-y-auto animate-in fade-in zoom-in duration-150">
      <div class="flex items-center justify-between border-b pb-3">
        <div class="flex items-center space-x-2">
          <span class="text-2xl">👝</span>
          <div>
            <h3 class="font-black text-sm text-gray-900">Meri Payments & Balance</h3>
            <p class="text-[10px] text-gray-500">Total Profit & Auto Transfer Ledger</p>
          </div>
        </div>
        <button onclick="closeMeriPaymentsModal()" class="w-7 h-7 rounded-full bg-gray-100 hover:bg-gray-200 flex items-center justify-center text-gray-500">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <div class="grid grid-cols-2 gap-3">
        <div class="bg-emerald-50 border border-emerald-200 rounded-2xl p-3.5 text-center">
          <p class="text-[11px] font-semibold text-gray-600">Paid Munafa (Transfer Shuda)</p>
          <h3 id="sheetPaidBalance" class="text-lg font-black text-emerald-700 mt-1">Rs. 0</h3>
        </div>
        <div class="bg-amber-50 border border-amber-200 rounded-2xl p-3.5 text-center">
          <p class="text-[11px] font-semibold text-gray-600">Pending Munafa (In Process)</p>
          <h3 id="sheetPendingBalance" class="text-lg font-black text-amber-700 mt-1">Rs. 0</h3>
        </div>
      </div>

      <div class="bg-slate-900 text-white rounded-2xl p-4 space-y-2 border border-amber-500/30">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold text-amber-300">Active Payout Account</span>
          <button onclick="closeMeriPaymentsModal(); openProfitAccountModal();" class="text-[11px] font-bold text-amber-400 underline">Change</button>
        </div>
        <p id="sheetPayoutInfo" class="text-xs font-mono font-bold">EasyPaisa: Not Set Yet</p>
        <p class="text-[10px] text-gray-400">Har hafte Monday ko delivered orders ka munafa auto-transfer hota hai.</p>
      </div>

      <button onclick="closeMeriPaymentsModal()" class="w-full bg-gray-100 text-gray-800 font-bold py-2.5 rounded-xl text-xs hover:bg-gray-200 transition">
        Wapis Profile Par Jayein
      </button>
    </div>
  </div>

  <!-- ==================== MODAL: MERI OFFERS & BONUSES ==================== -->
  <div id="meriOffersModal" class="fixed inset-0 bg-black/75 z-50 hidden flex items-center justify-center p-3">
    <div class="bg-white rounded-3xl max-w-sm w-full p-5 space-y-4 shadow-2xl border border-gray-100 max-h-[90vh] overflow-y-auto animate-in fade-in zoom-in duration-150">
      <div class="flex items-center justify-between border-b pb-3">
        <div class="flex items-center space-x-2">
          <span class="text-2xl">💵</span>
          <div>
            <h3 class="font-black text-sm text-gray-900">Meri Offers & Targets</h3>
            <p class="text-[10px] text-amber-600 font-bold">Active Extra Cash Rewards</p>
          </div>
        </div>
        <button onclick="closeMeriOffersModal()" class="w-7 h-7 rounded-full bg-gray-100 hover:bg-gray-200 flex items-center justify-center text-gray-500">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <div class="space-y-3">
        <!-- Offer 1 -->
        <div class="bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-200 rounded-2xl p-4 space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-black text-gray-900">🎉 Pehla Order Bonus</span>
            <span class="bg-amber-400 text-gray-950 text-xs font-black px-2 py-0.5 rounded-lg">+Rs. 100 Cash</span>
          </div>
          <p class="text-[11px] text-gray-600">Apna pehla kamyab order deliver karwayein aur foran 100 rupay ka bonus paayein.</p>
          <div class="w-full bg-gray-200 rounded-full h-2 overflow-hidden">
            <div id="progOfferFirst" class="bg-amber-500 h-2 rounded-full" style="width: 0%"></div>
          </div>
          <p id="lblOfferFirst" class="text-[10px] font-bold text-amber-800">0/1 Orders Delivered</p>
        </div>

        <!-- Offer 2 -->
        <div class="bg-gradient-to-r from-amber-50 to-yellow-50 border border-amber-200 rounded-2xl p-4 space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-black text-gray-900">🏆 10 Orders Milestone</span>
            <span class="bg-amber-400 text-gray-950 text-xs font-black px-2 py-0.5 rounded-lg">+Rs. 1,000 Cash</span>
          </div>
          <p class="text-[11px] text-gray-600">Mahine mein 10 orders complete karne par 1,000 rupay seedha aapke wallet mein.</p>
          <div class="w-full bg-gray-200 rounded-full h-2 overflow-hidden">
            <div id="progOfferTen" class="bg-amber-500 h-2 rounded-full" style="width: 0%"></div>
          </div>
          <p id="lblOfferTen" class="text-[10px] font-bold text-amber-800">0/10 Orders Completed</p>
        </div>
      </div>

      <button onclick="closeMeriOffersModal()" class="w-full bg-gray-900 text-white font-black py-2.5 rounded-xl text-xs shadow hover:bg-black transition">
        Theek Hai
      </button>
    </div>
  </div>

  <!-- ==================== MODAL: BUSINESS DETAILS ==================== -->
  <div id="businessDetailsModal" class="fixed inset-0 bg-black/75 z-50 hidden flex items-center justify-center p-3">
    <div class="bg-white rounded-3xl max-w-sm w-full p-5 space-y-4 shadow-2xl border border-gray-100 max-h-[90vh] overflow-y-auto animate-in fade-in zoom-in duration-150">
      <div class="flex items-center justify-between border-b pb-3">
        <div class="flex items-center space-x-2">
          <div class="w-8 h-8 rounded-xl bg-slate-100 flex items-center justify-center text-slate-800">
            <i data-lucide="store" class="w-4 h-4"></i>
          </div>
          <div>
            <h3 class="font-black text-sm text-gray-900">Business Details</h3>
            <p class="text-[10px] text-gray-500">Customer Bill & Store Name</p>
          </div>
        </div>
        <button onclick="closeBusinessDetailsModal()" class="w-7 h-7 rounded-full bg-gray-100 hover:bg-gray-200 flex items-center justify-center text-gray-500">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <form onsubmit="saveBusinessDetails(event)" class="space-y-3">
        <div>
          <label class="block text-[11px] font-bold text-gray-700 mb-1">Aap Ke Online Store Ka Naam</label>
          <input type="text" id="inpStoreNameSetting" required placeholder="Misaal: Hoor Fahim Store" class="w-full border-2 border-gray-200 rounded-xl px-3 py-2 text-xs font-bold outline-none focus:border-amber-500" />
          <p class="text-[10px] text-gray-400 mt-0.5">Yehi naam parcel ke label par likha hoga</p>
        </div>

        <div>
          <label class="block text-[11px] font-bold text-gray-700 mb-1">Aap Ka Asal Naam</label>
          <input type="text" id="inpResellerNameSetting" required placeholder="Misaal: Hoor Fahim" class="w-full border-2 border-gray-200 rounded-xl px-3 py-2 text-xs font-semibold outline-none focus:border-amber-500" />
        </div>

        <div>
          <label class="block text-[11px] font-bold text-gray-700 mb-1">WhatsApp / Phone Number</label>
          <input type="tel" id="inpPhoneSetting" placeholder="03001234567" class="w-full border-2 border-gray-200 rounded-xl px-3 py-2 text-xs font-semibold outline-none focus:border-amber-500" />
        </div>

        <div>
          <label class="block text-[11px] font-bold text-gray-700 mb-1">Shahar (City)</label>
          <input type="text" id="inpCitySetting" placeholder="Lahore / Karachi / Islamabad..." class="w-full border-2 border-gray-200 rounded-xl px-3 py-2 text-xs font-semibold outline-none focus:border-amber-500" />
        </div>

        <button type="submit" class="w-full bg-amber-400 hover:bg-amber-500 text-gray-950 font-black py-2.5 rounded-xl text-xs shadow-md transition">
          Business Details Save Karein
        </button>
      </form>
    </div>
  </div>
'''

content = content.replace('</body>', dedicated_modals_html + '\n</body>')

# 6. Add JavaScript Engine for:
# - filterOrdersByStage (8 stages)
# - selectPayoutBank & saveProfitAccount
# - open/close sub modals
# - sync with Supabase reseller_wallets
js_additions = '''
    // ==================== SCREENSHOT 1 & 2 ADVANCED BUSINESS LOGIC ====================
    let selectedPayoutMethod = 'EasyPaisa';

    function openProfitAccountModal() {
      // Pre-fill if exists
      const savedAcc = localStorage.getItem('tejarat_payout_account');
      if (savedAcc) {
        try {
          const acc = JSON.parse(savedAcc);
          if (acc.account_title) document.getElementById('inpPayoutAccountTitle').value = acc.account_title;
          if (acc.account_number) document.getElementById('inpPayoutAccountNumber').value = acc.account_number;
          if (acc.cnic) document.getElementById('inpPayoutCnic').value = acc.cnic;
          if (acc.method) selectPayoutBank(acc.method, acc.method);
        } catch(e) {}
      }
      document.getElementById('profitAccountModal').classList.remove('hidden');
      lucide.createIcons();
    }

    function closeProfitAccountModal() {
      document.getElementById('profitAccountModal').classList.add('hidden');
    }

    function selectPayoutBank(methodKey, displayTitle) {
      selectedPayoutMethod = methodKey;
      document.getElementById('lblSelectedBank').value = displayTitle;

      document.querySelectorAll('.payout-bank-btn').forEach(btn => {
        if (btn.getAttribute('data-bank') === methodKey) {
          btn.className = 'payout-bank-btn p-2.5 rounded-xl border flex items-center space-x-2 bg-amber-50 border-amber-400 transition shadow-sm';
        } else {
          btn.className = 'payout-bank-btn p-2.5 rounded-xl border flex items-center space-x-2 border-gray-200 hover:bg-gray-50 transition';
        }
      });
    }

    async function saveProfitAccount(e) {
      if (e) e.preventDefault();
      const title = document.getElementById('inpPayoutAccountTitle').value.trim();
      const number = document.getElementById('inpPayoutAccountNumber').value.trim();
      const cnic = document.getElementById('inpPayoutCnic').value.trim();

      if (!title || !number) {
        showToast('Bara-e-karam Account Title aur Number dono darj karein!');
        return;
      }

      const accObj = {
        method: selectedPayoutMethod,
        account_title: title,
        account_number: number,
        cnic: cnic,
        updated_at: new Date().toISOString()
      };

      localStorage.setItem('tejarat_payout_account', JSON.stringify(accObj));

      // Update UI elements in Profile tab
      const badge = document.getElementById('badgeProfitSet');
      if (badge) {
        badge.innerText = '✓ ' + selectedPayoutMethod;
        badge.className = 'text-[9px] bg-emerald-100 text-emerald-800 font-bold px-1.5 py-0.2 rounded';
      }

      const subLabel = document.getElementById('subProfitAccount');
      if (subLabel) {
        subLabel.innerText = `${selectedPayoutMethod}: ${number} (${title})`;
      }

      // Sync with Supabase reseller_wallets
      if (currentUser && currentUser.email) {
        try {
          await supabaseClient.from('reseller_wallets').upsert({
            user_id: currentUser.id,
            email: currentUser.email,
            phone: currentUser.email,
            store_name: currentUser.store_name || (currentUser.full_name + ' Store'),
            payment_method: selectedPayoutMethod,
            account_number: number,
            account_title: title
          }, { onConflict: 'user_id' });
        } catch(err) {
          console.warn('Sync payout account to supabase error:', err);
        }
      }

      closeProfitAccountModal();
      showToast(`✓ ${selectedPayoutMethod} Account kamyabi se save ho gaya!`);
    }

    // Meri Payments Modal
    function openMeriPaymentsModal() {
      const savedAcc = localStorage.getItem('tejarat_payout_account');
      if (savedAcc) {
        try {
          const acc = JSON.parse(savedAcc);
          document.getElementById('sheetPayoutInfo').innerText = `${acc.method}: ${acc.account_number} (${acc.account_title})`;
        } catch(e) {}
      }
      document.getElementById('meriPaymentsModal').classList.remove('hidden');
      lucide.createIcons();
    }

    function closeMeriPaymentsModal() {
      document.getElementById('meriPaymentsModal').classList.add('hidden');
    }

    // Meri Offers Modal
    function openMeriOffersModal() {
      const deliveredCount = orders.filter(o => o.status === 'Delivered').length;
      document.getElementById('lblOfferFirst').innerText = `${Math.min(deliveredCount, 1)}/1 Orders Delivered`;
      document.getElementById('progOfferFirst').style.width = deliveredCount >= 1 ? '100%' : '0%';

      document.getElementById('lblOfferTen').innerText = `${Math.min(deliveredCount, 10)}/10 Orders Completed`;
      document.getElementById('progOfferTen').style.width = `${Math.min(deliveredCount * 10, 100)}%`;

      document.getElementById('meriOffersModal').classList.remove('hidden');
      lucide.createIcons();
    }

    function closeMeriOffersModal() {
      document.getElementById('meriOffersModal').classList.add('hidden');
    }

    // Business Details Modal
    function openBusinessDetailsModal() {
      if (currentUser) {
        if (currentUser.store_name) document.getElementById('inpStoreNameSetting').value = currentUser.store_name;
        if (currentUser.full_name) document.getElementById('inpResellerNameSetting').value = currentUser.full_name;
      }
      document.getElementById('businessDetailsModal').classList.remove('hidden');
      lucide.createIcons();
    }

    function closeBusinessDetailsModal() {
      document.getElementById('businessDetailsModal').classList.add('hidden');
    }

    async function saveBusinessDetails(e) {
      if (e) e.preventDefault();
      const sName = document.getElementById('inpStoreNameSetting').value.trim();
      const rName = document.getElementById('inpResellerNameSetting').value.trim();
      const phone = document.getElementById('inpPhoneSetting').value.trim();

      if (!sName || !rName) {
        showToast('Store name aur apna naam darj karein!');
        return;
      }

      if (currentUser) {
        currentUser.store_name = sName;
        currentUser.full_name = rName;
        localStorage.setItem('tejarat_user', JSON.stringify(currentUser));
        applyLoggedInUserUI(currentUser);
      }

      document.getElementById('subBizName').innerText = `${sName} · Profile Info`;
      document.getElementById('bizStoreName').innerText = sName;

      closeBusinessDetailsModal();
      showToast('✓ Business Details kamyabi se update ho gayi!');
    }

    // Orders Filtering by 8 Lifecycle Stages
    function filterOrdersByStage(stageName) {
      document.getElementById('ordersStageView').classList.remove('hidden');
      document.getElementById('lblCurrentStageTitle').innerText = stageName;

      const container = document.getElementById('ordersListContainer');
      let filtered = [];

      if (stageName === 'Verification Pending') {
        filtered = orders.filter(o => o.status === 'Pending' || o.status === 'Verification Pending');
      } else if (stageName === 'Delivered') {
        filtered = orders.filter(o => o.status === 'Delivered');
      } else if (stageName === 'In-progress') {
        filtered = orders.filter(o => o.status === 'Confirmed' || o.status === 'In-progress' || o.status === 'Dispatched');
      } else if (stageName === 'Out for Delivery') {
        filtered = orders.filter(o => o.status === 'Out for Delivery');
      } else if (stageName === 'Returned') {
        filtered = orders.filter(o => o.status === 'Returned');
      } else if (stageName === 'Cancelled') {
        filtered = orders.filter(o => o.status === 'Cancelled' || o.status === 'Verification Failed');
      } else {
        filtered = orders.filter(o => o.status === stageName);
      }

      if (filtered.length === 0) {
        container.innerHTML = `
          <div class="bg-white rounded-3xl p-8 text-center space-y-2 border border-gray-100 shadow-sm">
            <span class="text-3xl">📦</span>
            <h4 class="font-black text-sm text-gray-800">Is stage mein koi orders nahi hain</h4>
            <p class="text-xs text-gray-500">Jab is stage ka koi order hoga to yahan live show hoga.</p>
          </div>
        `;
        return;
      }

      container.innerHTML = filtered.map(o => `
        <div class="bg-white rounded-2xl p-4 shadow-sm border border-gray-100 space-y-2">
          <div class="flex items-center justify-between border-b pb-2">
            <div>
              <span class="font-mono text-xs font-bold text-gray-700">#${o.id.substring(0, 8)}</span>
              <p class="text-[10px] text-gray-400">${new Date(o.created_at).toLocaleString()}</p>
            </div>
            <span class="text-xs font-black bg-amber-100 text-amber-900 px-2 py-0.5 rounded-full">${o.status}</span>
          </div>
          <div class="flex items-center justify-between text-xs pt-1">
            <span class="text-gray-600">${o.customer_name} (${o.customer_city || 'Pakistan'})</span>
            <span class="font-black text-gray-900">Total COD: Rs. ${o.total_cod_amount}</span>
          </div>
          <div class="flex items-center justify-between text-xs pt-1 border-t border-gray-50">
            <span class="text-amber-600 font-bold">Aap Ka Profit: Rs. ${o.total_profit}</span>
            <a href="https://wa.me/923222089610?text=Order%20Tracking%20${o.id}" target="_blank" class="text-[#047857] font-bold text-[11px] underline">Courier Track Karein →</a>
          </div>
        </div>
      `).join('');

      lucide.createIcons();
    }

    function backToOrdersStages() {
      document.getElementById('ordersStageView').classList.add('hidden');
    }

    function updateOrdersBadges() {
      const pendingCount = orders.filter(o => o.status === 'Pending' || o.status === 'Verification Pending').length;
      const inProgCount = orders.filter(o => o.status === 'Confirmed' || o.status === 'In-progress' || o.status === 'Dispatched').length;
      const deliveredCount = orders.filter(o => o.status === 'Delivered').length;

      if (document.getElementById('badgeCountPending')) document.getElementById('badgeCountPending').innerText = pendingCount;
      if (document.getElementById('badgeCountInProgress')) document.getElementById('badgeCountInProgress').innerText = inProgCount;
      if (document.getElementById('badgeCountDelivered')) document.getElementById('badgeCountDelivered').innerText = deliveredCount;
    }
'''

content = content.replace(
    '// ==================== 100% REAL AUTHENTICATION (DIRECT GMAIL, PASSWORD & GOOGLE) ====================',
    js_additions + '\n    // ==================== 100% REAL AUTHENTICATION (DIRECT GMAIL, PASSWORD & GOOGLE) ===================='
)

# Call updateOrdersBadges in renderAllViews
content = content.replace('renderOrdersList();', 'renderOrdersList();\n        updateOrdersBadges();')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html with Screenshot 1, 2, 3 parity & Profit Account Setup successfully!")
