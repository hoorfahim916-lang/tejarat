import re

html_path = "C:/Users/LENOVO/Downloads/TEJARAT APP/index.html"
with open(html_path, "r", encoding="utf-8") as f:
    c = f.read()

# Replace renderCategoryChips and renderCategoriesList
old_cat_render_regex = r'// ==================== RENDER CATEGORIES ====================[\s\S]*?// ==================== RENDER PRODUCTS GRID ===================='

new_cat_render = '''// ==================== RENDER CATEGORIES ====================
    function renderCategoryChips() {
      const container = document.getElementById('homeCategoryChips');
      if (!container) return;

      let html = `
        <button onclick="selectCategory('All')" class="px-3.5 py-1.5 rounded-full text-xs font-bold whitespace-nowrap transition shadow-sm ${
          activeCategoryFilter === 'All' ? 'bg-[#047857] text-white' : 'bg-white text-gray-700 border border-gray-200'
        }">
          Tamam Catalogs
        </button>
      `;

      categories.forEach(cat => {
        if (!cat.comingSoon) {
          const isSel = activeCategoryFilter === cat.name;
          html += `
            <button onclick="selectCategory('${cat.name}')" class="px-3.5 py-1.5 rounded-full text-xs font-bold whitespace-nowrap transition shadow-sm flex items-center space-x-1.5 ${
              isSel ? 'bg-[#047857] text-white' : 'bg-white text-gray-700 border border-gray-200'
            }">
              <span>${cat.icon}</span>
              <span>${cat.roman.split('(')[0].trim()}</span>
            </button>
          `;
        }
      });

      container.innerHTML = html;
    }

    function renderCategoriesList() {
      const container = document.getElementById('categoriesFullList');
      if (!container) return;

      container.innerHTML = categories.map(cat => {
        const catProds = products.filter(p => p.category === cat.name);
        if (cat.comingSoon) {
          return `
            <div onclick="showToast('✨ ${cat.roman} jald live hone wali hai!')" class="bg-gray-50/80 rounded-2xl p-4 shadow-sm border border-gray-200 flex items-center justify-between cursor-pointer hover:bg-gray-100 transition opacity-80">
              <div class="flex items-center space-x-3">
                <span class="text-3xl p-2 rounded-2xl bg-gray-200/70 grayscale">${cat.icon || '📦'}</span>
                <div>
                  <div class="flex items-center space-x-2">
                    <h4 class="font-black text-sm text-gray-700">${cat.roman || cat.name}</h4>
                    <span class="text-[9px] bg-amber-100 text-amber-800 font-black px-1.5 py-0.5 rounded uppercase">Coming Soon</span>
                  </div>
                  <p class="text-[11px] text-gray-400 font-semibold mt-0.5">Jald live ho raha hai</p>
                </div>
              </div>
              <i data-lucide="lock" class="w-4 h-4 text-gray-400"></i>
            </div>
          `;
        }

        return `
          <div onclick="selectCategory('${cat.name}'); switchTab('home');" class="bg-white rounded-2xl p-4 shadow-sm border border-gray-100 flex items-center justify-between cursor-pointer hover:border-emerald-300 transition">
            <div class="flex items-center space-x-3">
              <span class="text-3xl p-2 rounded-2xl bg-emerald-50">${cat.icon || '📦'}</span>
              <div>
                <div class="flex items-center space-x-2">
                  <h4 class="font-black text-sm text-gray-900">${cat.roman || cat.name}</h4>
                  <span class="text-[9px] bg-emerald-100 text-emerald-800 font-black px-1.5 py-0.5 rounded uppercase">Active</span>
                </div>
                <p class="text-[11px] text-gray-500 font-semibold mt-0.5">${catProds.length} Wholesale Items Available</p>
              </div>
            </div>
            <i data-lucide="chevron-right" class="w-5 h-5 text-gray-400"></i>
          </div>
        `;
      }).join('');

      lucide.createIcons();
    }

    // ==================== RENDER PRODUCTS GRID ===================='''

c = re.sub(old_cat_render_regex, new_cat_render, c)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(c)

print("Updated category render functions successfully!")
