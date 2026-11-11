import re

html_path = "C:/Users/LENOVO/Downloads/TEJARAT APP/index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update the Google button in auth modal
content = content.replace(
    'onclick="handleGoogleOneTapLogin()" id="btnGoogleOneTap"',
    'onclick="handleGoogleOAuth()" id="btnGoogleOAuth"'
)

# Add Google Setup Guide Modal before closing </body>
guide_modal_html = '''
  <!-- ==================== MODAL: GOOGLE OAUTH SUPABASE SETUP GUIDE ==================== -->
  <div id="googleSetupGuideModal" class="fixed inset-0 bg-black/75 z-50 hidden flex items-center justify-center p-3">
    <div class="bg-white rounded-3xl max-w-sm w-full p-5 space-y-4 shadow-2xl border border-gray-100 max-h-[90vh] overflow-y-auto animate-in fade-in zoom-in duration-150">
      <div class="flex items-center justify-between border-b pb-3">
        <div class="flex items-center space-x-2">
          <svg class="w-6 h-6 flex-shrink-0" viewBox="0 0 24 24">
            <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
            <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
            <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
            <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
          </svg>
          <h3 class="font-black text-sm text-gray-900">Google OAuth Activate Karein</h3>
        </div>
        <button onclick="closeGoogleSetupGuideModal()" class="w-7 h-7 rounded-full bg-gray-100 hover:bg-gray-200 flex items-center justify-center text-gray-500">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <div class="space-y-3 text-xs text-gray-700">
        <div class="bg-amber-50 border border-amber-200 rounded-2xl p-3 space-y-1">
          <p class="font-bold text-amber-900">Google OAuth 50,000 Users/Month Free Hai!</p>
          <p class="text-[11px] text-amber-800">
            اس پر کوئی ای میل لمیٹ نہیں ہوتی۔ صرف گوگل کلاؤڈ سے کلائنٹ آئی ڈی لا کر سپابیس میں سیو کرنی ہے۔
          </p>
        </div>

        <div class="space-y-2 text-[11px]">
          <p class="font-bold text-gray-900">طریقہ کار (2 منٹ کا آسان سیٹ اپ):</p>
          <ol class="list-decimal list-inside space-y-1.5 text-gray-600 font-medium">
            <li>Google Cloud Console (<a href="https://console.cloud.google.com" target="_blank" class="text-blue-600 underline font-bold">console.cloud.google.com</a>) اوپن کریں۔</li>
            <li><strong>OAuth Client ID</strong> (Web Application) کریٹ کریں۔</li>
            <li>Authorized Redirect URI میں یہ پاتھ ڈالیں:</li>
          </ol>
          <div class="bg-gray-100 p-2.5 rounded-xl border flex items-center justify-between">
            <span class="font-mono text-[10px] break-all select-all">https://xdsxmgzcfihkohsbzszq.supabase.co/auth/v1/callback</span>
            <button onclick="copySupabaseCallbackUrl()" class="ml-2 bg-[#047857] text-white px-2 py-1 rounded text-[10px] font-bold whitespace-nowrap">Copy</button>
          </div>
          <ol start="4" class="list-decimal list-inside space-y-1.5 text-gray-600 font-medium">
            <li>Supabase Dashboard -> <strong>Authentication</strong> -> <strong>Providers</strong> -> <strong>Google</strong> اوپن کریں۔</li>
            <li>Google کو <strong>ON</strong> کر کے Client ID اور Client Secret پیسٹ کر کے <strong>Save</strong> کر دیں۔</li>
          </ol>
        </div>

        <button onclick="closeGoogleSetupGuideModal()" class="w-full bg-[#047857] hover:bg-emerald-800 text-white font-black py-2.5 rounded-xl text-xs shadow transition">
          Samajh Aa Gaya (Theek Hai)
        </button>
      </div>
    </div>
  </div>
'''

if 'id="googleSetupGuideModal"' not in content:
    content = content.replace('</body>', guide_modal_html + '\n</body>')

# Add Javascript functions for handleGoogleOAuth and copy
js_funcs = '''
    // Real Supabase Google OAuth Handler
    async function handleGoogleOAuth() {
      try {
        showToast('Google Sign-In open ho raha hai...');
        const redirectUrl = window.location.origin + window.location.pathname;
        const { data, error } = await supabaseClient.auth.signInWithOAuth({
          provider: 'google',
          options: {
            redirectTo: redirectUrl,
            queryParams: {
              access_type: 'offline',
              prompt: 'select_account'
            }
          }
        });

        if (error) {
          console.warn('Google OAuth error:', error);
          if (error.message.includes('Provider is not enabled') || error.status === 400) {
            openGoogleSetupGuideModal();
          } else {
            showToast('Google Sign-In Error: ' + error.message);
          }
        }
      } catch (err) {
        console.error('Google OAuth exception:', err);
        openGoogleSetupGuideModal();
      }
    }

    function openGoogleSetupGuideModal() {
      document.getElementById('googleSetupGuideModal').classList.remove('hidden');
      lucide.createIcons();
    }

    function closeGoogleSetupGuideModal() {
      document.getElementById('googleSetupGuideModal').classList.add('hidden');
    }

    function copySupabaseCallbackUrl() {
      const url = "https://xdsxmgzcfihkohsbzszq.supabase.co/auth/v1/callback";
      navigator.clipboard.writeText(url).then(() => {
        showToast('✓ Redirect URL Copy ho gaya!');
      }).catch(() => {
        showToast('Copy: ' + url);
      });
    }
'''

content = content.replace(
    '// 4. Google 1-Tap Login (Zero 404 errors, fast, reliable)',
    js_funcs + '\n    // 4. Google 1-Tap Login (Zero 404 errors, fast, reliable)'
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html with real Supabase Google OAuth and Guide Modal successfully!")
