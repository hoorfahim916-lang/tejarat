import os
import re

html_path = "C:/Users/LENOVO/Downloads/TEJARAT APP/index.html"
with open(html_path, "r", encoding="utf-8") as f:
    c = f.read()

# 1. Update Categories Array
old_cat_regex = r'const DEFAULT_CATEGORIES = \[[\s\S]*?\];'
new_cat_code = '''const DEFAULT_CATEGORIES = [
      { name: "Dry Fruits & Nuts", roman: "Dry Fruits & Nuts (خشک میوہ جات)", icon: "🥜", active: true },
      { name: "Pure Sidr Honey", roman: "Pure Sidr Honey (خالص بیری کا شہد)", icon: "🍯", active: true },
      { name: "Desi Ghee", roman: "Desi Ghee (خالص دیسی گھی)", icon: "🧈", active: true },
      { name: "Ladies Suits", roman: "Ladies Suits (خواتین کے سوٹ)", icon: "👗", active: false, comingSoon: true },
      { name: "Men Clothes", roman: "Men's Collection (مردانہ ملبوسات)", icon: "👔", active: false, comingSoon: true },
      { name: "Pants & Jeans", roman: "Pants & Jeans (پینٹس وغیرہ)", icon: "👖", active: false, comingSoon: true },
      { name: "Beauty & Makeup", roman: "Beauty & Cosmetics (کاسمیٹکس)", icon: "💄", active: false, comingSoon: true }
    ];'''
c = re.sub(old_cat_regex, new_cat_code, c)

# 2. Update Carousel Banners to Focus on Pure Dry Fruits, Sidr Honey & Desi Ghee
old_carousel_regex = r'<!-- Slides Container -->\s*<div id="carouselSlider" class="flex transition-transform duration-500 ease-out h-full">[\s\S]*?<!-- Carousel Navigation Dots -->'
new_carousel_code = '''<!-- Slides Container -->
            <div id="carouselSlider" class="flex transition-transform duration-500 ease-out h-full">
              <!-- Slide 1: Dry Fruits -->
              <div class="w-full h-full flex-shrink-0 relative">
                <img src="https://images.unsplash.com/photo-1563636619-e9143da7973b?w=900&auto=format&fit=crop" class="w-full h-full object-cover" />
                <div class="absolute inset-0 bg-gradient-to-r from-black/85 via-black/50 to-transparent p-5 flex flex-col justify-center text-white">
                  <span class="bg-amber-400 text-gray-950 text-[10px] font-black px-2 py-0.5 rounded-md uppercase w-max mb-1">🥜 100% Fresh Dry Fruits</span>
                  <h3 class="text-base font-black leading-tight">Chaman & Gilgit Ke Special Kagzi Akhrot</h3>
                  <p class="text-xs text-amber-200 mt-1">Wholesale rate par khud kharidein ya resell karein</p>
                  <button onclick="selectCategory('Dry Fruits & Nuts')" class="mt-2.5 bg-white text-gray-900 text-xs font-black px-3.5 py-1.5 rounded-xl w-max shadow-md hover:bg-amber-50">Dry Fruits Catalog Dekhein →</button>
                </div>
              </div>

              <!-- Slide 2: Sidr Honey -->
              <div class="w-full h-full flex-shrink-0 relative">
                <img src="https://images.unsplash.com/photo-1587049352847-4a222e784d38?w=900&auto=format&fit=crop" class="w-full h-full object-cover" />
                <div class="absolute inset-0 bg-gradient-to-r from-black/85 via-black/50 to-transparent p-5 flex flex-col justify-center text-white">
                  <span class="bg-amber-400 text-gray-950 text-[10px] font-black px-2 py-0.5 rounded-md uppercase w-max mb-1">🍯 100% Pure Sidr Honey</span>
                  <h3 class="text-base font-black leading-tight">Khalis Beri Ka Raw Organic Honey</h3>
                  <p class="text-xs text-amber-200 mt-1">Lab tested aur 100% khalis hone ki guarantee</p>
                  <button onclick="selectCategory('Pure Sidr Honey')" class="mt-2.5 bg-white text-gray-900 text-xs font-black px-3.5 py-1.5 rounded-xl w-max shadow-md hover:bg-amber-50">Sidr Honey Catalog Dekhein →</button>
                </div>
              </div>

              <!-- Slide 3: Desi Ghee -->
              <div class="w-full h-full flex-shrink-0 relative">
                <img src="https://images.unsplash.com/photo-1631451095765-2c91616fc9e6?w=900&auto=format&fit=crop" class="w-full h-full object-cover" />
                <div class="absolute inset-0 bg-gradient-to-r from-black/85 via-black/50 to-transparent p-5 flex flex-col justify-center text-white">
                  <span class="bg-amber-400 text-gray-950 text-[10px] font-black px-2 py-0.5 rounded-md uppercase w-max mb-1">🧈 Organic Desi Ghee</span>
                  <h3 class="text-base font-black leading-tight">Sahiwal Cow Ka Danedar Chatti Desi Ghee</h3>
                  <p class="text-xs text-amber-200 mt-1">Baghair kisi chemical ya artificial essence ke</p>
                  <button onclick="selectCategory('Desi Ghee')" class="mt-2.5 bg-white text-gray-900 text-xs font-black px-3.5 py-1.5 rounded-xl w-max shadow-md hover:bg-amber-50">Desi Ghee Catalog Dekhein →</button>
                </div>
              </div>
            </div>

            <!-- Carousel Navigation Dots -->'''
c = re.sub(old_carousel_regex, new_carousel_code, c)

# 3. Add Theme Switcher Modal and Options
theme_modal_html = '''
  <!-- ==================== MODAL: LIVE COLOR THEME PICKER ==================== -->
  <div id="themePickerModal" class="fixed inset-0 bg-black/75 z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-sm w-full p-5 space-y-4 shadow-2xl border border-gray-100 animate-in fade-in zoom-in duration-150">
      <div class="flex items-center justify-between border-b pb-3">
        <div class="flex items-center space-x-2">
          <span class="text-xl">🎨</span>
          <div>
            <h3 class="font-black text-sm text-gray-900">App Color Theme Select Karein</h3>
            <p class="text-[10px] text-gray-500">Apni pasand ka color theme chunein</p>
          </div>
        </div>
        <button onclick="closeThemePickerModal()" class="w-7 h-7 rounded-full bg-gray-100 hover:bg-gray-200 flex items-center justify-center text-gray-500">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <div class="space-y-2.5">
        <!-- Option 1: Royal Sapphire Blue -->
        <button onclick="applyAppTheme('blue')" class="w-full p-3 rounded-2xl border-2 border-blue-500 hover:bg-blue-50/50 flex items-center justify-between transition text-left">
          <div class="flex items-center space-x-3">
            <span class="w-8 h-8 rounded-xl bg-gradient-to-r from-blue-900 via-blue-700 to-blue-500 shadow-md"></span>
            <div>
              <p class="text-xs font-black text-gray-900">1. Royal Sapphire Blue</p>
              <p class="text-[10px] text-gray-500">Daraz / Amazon Style · Corporate & Trustworthy</p>
            </div>
          </div>
          <span class="text-xs font-bold text-blue-600">Select</span>
        </button>

        <!-- Option 2: Imperial Purple / Modern Magenta -->
        <button onclick="applyAppTheme('purple')" class="w-full p-3 rounded-2xl border-2 border-purple-500 hover:bg-purple-50/50 flex items-center justify-between transition text-left">
          <div class="flex items-center space-x-3">
            <span class="w-8 h-8 rounded-xl bg-gradient-to-r from-purple-900 via-purple-700 to-purple-500 shadow-md"></span>
            <div>
              <p class="text-xs font-black text-gray-900">2. Imperial Purple (Markaz Style)</p>
              <p class="text-[10px] text-gray-500">Trendy · High Conversion · Reseller Signature</p>
            </div>
          </div>
          <span class="text-xs font-bold text-purple-600">Select</span>
        </button>

        <!-- Option 3: Midnight Navy & Gold -->
        <button onclick="applyAppTheme('navy')" class="w-full p-3 rounded-2xl border-2 border-slate-700 hover:bg-slate-50 flex items-center justify-between transition text-left">
          <div class="flex items-center space-x-3">
            <span class="w-8 h-8 rounded-xl bg-gradient-to-r from-slate-950 via-slate-900 to-slate-800 border border-amber-400 shadow-md"></span>
            <div>
              <p class="text-xs font-black text-gray-900">3. Midnight Navy & Gold</p>
              <p class="text-[10px] text-gray-500">Luxury Premium · High-End Organic Store</p>
            </div>
          </div>
          <span class="text-xs font-bold text-slate-800">Select</span>
        </button>

        <!-- Option 4: Deep Burgundy / Persian Plum -->
        <button onclick="applyAppTheme('burgundy')" class="w-full p-3 rounded-2xl border-2 border-rose-800 hover:bg-rose-50/50 flex items-center justify-between transition text-left">
          <div class="flex items-center space-x-3">
            <span class="w-8 h-8 rounded-xl bg-gradient-to-r from-rose-950 via-rose-900 to-rose-700 shadow-md"></span>
            <div>
              <p class="text-xs font-black text-gray-900">4. Persian Plum & Burgundy</p>
              <p class="text-[10px] text-gray-500">Warm · Royal Pakistani Cultural Aesthetic</p>
            </div>
          </div>
          <span class="text-xs font-bold text-rose-800">Select</span>
        </button>

        <!-- Option 5: Emerald Green & Gold (Default) -->
        <button onclick="applyAppTheme('green')" class="w-full p-3 rounded-2xl border-2 border-emerald-600 hover:bg-emerald-50/50 flex items-center justify-between transition text-left">
          <div class="flex items-center space-x-3">
            <span class="w-8 h-8 rounded-xl bg-gradient-to-r from-[#064E3B] via-[#047857] to-[#0D9488] shadow-md"></span>
            <div>
              <p class="text-xs font-black text-gray-900">5. Deep Emerald Green & Gold</p>
              <p class="text-[10px] text-gray-500">Organic · Pure Nature · Halal Wholesale</p>
            </div>
          </div>
          <span class="text-xs font-bold text-emerald-700">Select</span>
        </button>
      </div>

      <button onclick="closeThemePickerModal()" class="w-full bg-gray-900 text-white font-black py-2.5 rounded-xl text-xs shadow transition">
        Band Karein
      </button>
    </div>
  </div>
'''

if 'id="themePickerModal"' not in c:
    c = c.replace('</body>', theme_modal_html + '\n</body>')

# Add Palette button in the top bar header next to help
old_top_bar_help = '''<!-- Chatbot Help Pill -->
          <button onclick="openChatbotModal()" class="flex items-center space-x-1 bg-emerald-900/60 hover:bg-emerald-900 border border-emerald-400/30 px-2.5 py-1.5 rounded-full text-xs font-bold transition shadow-sm">
            <span class="w-2 h-2 rounded-full bg-amber-400 animate-ping"></span>
            <span>Madad</span>
          </button>'''

new_top_bar_help = '''<!-- Theme Picker Button -->
          <button onclick="openThemePickerModal()" title="App Ka Color Badlein" class="flex items-center space-x-1 bg-black/25 hover:bg-black/40 border border-white/20 px-2.5 py-1.5 rounded-full text-xs font-bold transition shadow-sm">
            <span>🎨 Color</span>
          </button>

          <!-- Chatbot Help Pill -->
          <button onclick="openChatbotModal()" class="flex items-center space-x-1 bg-black/25 hover:bg-black/40 border border-white/20 px-2.5 py-1.5 rounded-full text-xs font-bold transition shadow-sm">
            <span class="w-2 h-2 rounded-full bg-amber-400 animate-ping"></span>
            <span>Madad</span>
          </button>'''

c = c.replace(old_top_bar_help, new_top_bar_help)

# 4. Javascript Theme Engine
theme_js = '''
    // ==================== DYNAMIC APP THEME ENGINE ====================
    const THEME_DEFINITIONS = {
      blue: {
        headerGradient: 'from-[#172554] via-[#1E40AF] to-[#2563EB]',
        primaryBg: '#1E40AF',
        primaryHover: '#1D4ED8',
        lightBg: '#EFF6FF',
        textPrimary: '#1E40AF',
        borderPrimary: '#3B82F6'
      },
      purple: {
        headerGradient: 'from-[#4C1D95] via-[#6D28D9] to-[#7C3AED]',
        primaryBg: '#6D28D9',
        primaryHover: '#5B21B6',
        lightBg: '#FAF5FF',
        textPrimary: '#6D28D9',
        borderPrimary: '#8B5CF6'
      },
      navy: {
        headerGradient: 'from-[#020617] via-[#0F172A] to-[#1E293B]',
        primaryBg: '#0F172A',
        primaryHover: '#020617',
        lightBg: '#F8FAFC',
        textPrimary: '#0F172A',
        borderPrimary: '#334155'
      },
      burgundy: {
        headerGradient: 'from-[#4C0519] via-[#881337] to-[#BE123C]',
        primaryBg: '#881337',
        primaryHover: '#700E2B',
        lightBg: '#FFF1F2',
        textPrimary: '#881337',
        borderPrimary: '#F43F5E'
      },
      green: {
        headerGradient: 'from-[#065F46] via-[#047857] to-[#0D9488]',
        primaryBg: '#047857',
        primaryHover: '#065F46',
        lightBg: '#ECFDF5',
        textPrimary: '#047857',
        borderPrimary: '#10B981'
      }
    };

    function applyAppTheme(themeKey) {
      const theme = THEME_DEFINITIONS[themeKey] || THEME_DEFINITIONS.green;
      localStorage.setItem('tejarat_theme', themeKey);

      // Update Header
      const header = document.querySelector('header');
      if (header) {
        header.className = `bg-gradient-to-r ${theme.headerGradient} text-white sticky top-0 z-30 shadow-md top-safe-header`;
      }

      // Update Meta Theme Color
      const metaTheme = document.querySelector('meta[name="theme-color"]');
      if (metaTheme) metaTheme.setAttribute('content', theme.primaryBg);

      // Update Primary Buttons across views
      document.querySelectorAll('.theme-primary-btn').forEach(btn => {
        btn.style.backgroundColor = theme.primaryBg;
      });

      closeThemePickerModal();
      showToast(`✓ Color theme '${themeKey.toUpperCase()}' apply ho gaya!`);
    }

    function initTheme() {
      const saved = localStorage.getItem('tejarat_theme') || 'green';
      applyAppTheme(saved);
    }

    function openThemePickerModal() {
      document.getElementById('themePickerModal').classList.remove('hidden');
      lucide.createIcons();
    }

    function closeThemePickerModal() {
      document.getElementById('themePickerModal').classList.add('hidden');
    }
'''

c = c.replace(
    '// ==================== AUTO-SLIDING CAROUSEL ====================',
    theme_js + '\n    // ==================== AUTO-SLIDING CAROUSEL ===================='
)

# Call initTheme in init
c = c.replace('renderAllViews();', 'initTheme();\n        renderAllViews();')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(c)

print("Updated index.html with Category filtering, Organic Banners & Live Color Theme Picker successfully!")
