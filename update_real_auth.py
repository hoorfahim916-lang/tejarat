import re

html_path = "C:/Users/LENOVO/Downloads/TEJARAT APP/index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the Auth Modal HTML
old_modal_regex = r'<!-- ==================== MODAL: GOOGLE / GMAIL VERIFIED LOGIN ==================== -->\s*<div id="authModal"[\s\S]*?<!-- ==================== MODAL 1: PRODUCT DETAILS VIEW ==================== -->'

new_modal_html = '''<!-- ==================== MODAL: REAL GOOGLE OAUTH & GMAIL OTP AUTH ==================== -->
  <div id="authModal" class="fixed inset-0 bg-black/75 z-50 hidden flex items-center justify-center p-3">
    <div class="bg-white rounded-3xl max-w-sm w-full p-5 space-y-4 shadow-2xl border border-gray-100 max-h-[92vh] overflow-y-auto">
      
      <!-- Modal Header -->
      <div class="flex items-center justify-between border-b border-gray-100 pb-3">
        <div class="flex items-center space-x-2.5">
          <div class="w-10 h-10 rounded-2xl overflow-hidden shadow border border-emerald-400/40 bg-white flex items-center justify-center flex-shrink-0">
            <img src="markaz_assets/tejarat_logo.png" onerror="this.onerror=null; this.src='tejarat_logo.png';" alt="Tejarat" class="w-full h-full object-cover" />
          </div>
          <div>
            <h3 class="font-black text-sm text-gray-900 leading-tight">Tejarat Reseller Sign In</h3>
            <p class="text-[10px] text-emerald-700 font-semibold">100% Real Google & Gmail Authentication</p>
          </div>
        </div>
        <button onclick="closeAuthModal()" class="w-8 h-8 rounded-full bg-gray-100 hover:bg-gray-200 flex items-center justify-center text-gray-500 transition">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <!-- Trust & Verification Notice -->
      <div class="bg-gradient-to-r from-emerald-50 via-teal-50 to-emerald-50 border border-emerald-200/80 rounded-2xl p-3 text-center space-y-1">
        <div class="flex items-center justify-center space-x-1.5">
          <span class="text-xs font-black text-[#047857]">Real Verified Reseller Account</span>
          <span class="text-[9px] bg-amber-400 text-gray-950 font-black px-1.5 py-0.5 rounded uppercase shadow-sm">VERIFIED</span>
        </div>
        <p class="text-[11px] text-gray-600 leading-relaxed">
          Google ya Gmail Code se sign-in karein. Aapka account direct <strong>Supabase</strong> aur <strong>Admin Panel</strong> mein register ho jayega.
        </p>
      </div>

      <!-- Method 1: Google OAuth Direct Button -->
      <div class="space-y-2">
        <button type="button" onclick="handleGoogleOAuth()" id="btnGoogleOAuth" class="w-full bg-white hover:bg-gray-50 border-2 border-gray-300 text-gray-800 font-bold py-3 px-4 rounded-2xl shadow-sm flex items-center justify-center space-x-3 transition active:scale-[0.98]">
          <svg class="w-5 h-5 flex-shrink-0" viewBox="0 0 24 24">
            <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
            <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
            <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
            <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
          </svg>
          <span class="text-xs font-bold text-gray-800">Sign Up / Login with Google</span>
        </button>
      </div>

      <!-- Divider -->
      <div class="relative flex py-1 items-center">
        <div class="flex-grow border-t border-gray-200"></div>
        <span class="flex-shrink mx-2 text-[10px] text-gray-400 uppercase font-black tracking-wider">ya phir Real Gmail Code / Pass</span>
        <div class="flex-grow border-t border-gray-200"></div>
      </div>

      <!-- Sub Tabs: [Gmail OTP Code] | [Password Login] -->
      <div class="bg-gray-100 p-1 rounded-xl flex space-x-1 text-xs font-bold">
        <button type="button" id="tabBtnOtp" onclick="switchAuthTab('otp')" class="flex-1 py-1.5 rounded-lg bg-white text-gray-900 shadow-sm transition text-center">
          📩 Gmail 6-Digit Code (OTP)
        </button>
        <button type="button" id="tabBtnPass" onclick="switchAuthTab('pass')" class="flex-1 py-1.5 rounded-lg text-gray-600 hover:text-gray-900 transition text-center">
          🔑 Password Login
        </button>
      </div>

      <!-- TAB 1: GMAIL OTP SYSTEM -->
      <div id="authTabOtpSection" class="space-y-3">
        <!-- OTP Step 1: Input Email & Request Code -->
        <div id="otpStep1" class="space-y-3">
          <div>
            <label class="block text-[11px] font-bold text-gray-700 mb-1">Apna Google / Gmail Address <span class="text-rose-500">*</span></label>
            <div class="relative">
              <input type="email" id="inpOtpEmail" required placeholder="apna.email@gmail.com" class="w-full border-2 border-gray-200 rounded-xl pl-9 pr-3 py-2 text-xs font-semibold outline-none focus:border-[#047857] transition" />
              <div class="absolute left-3 top-2.5">
                <i data-lucide="mail" class="w-4 h-4 text-gray-400"></i>
              </div>
            </div>
            <p class="text-[10px] text-gray-500 mt-1">Is Gmail par foran 6-hanso ka verification code bheja jayega.</p>
          </div>

          <div>
            <label class="block text-[11px] font-bold text-gray-700 mb-1">Aap Ka Naam / Reseller Name</label>
            <input type="text" id="inpOtpName" placeholder="Misaal: Hoor Fahim" class="w-full border-2 border-gray-200 rounded-xl px-3 py-2 text-xs font-semibold outline-none focus:border-[#047857] transition" />
          </div>

          <button type="button" onclick="sendGmailOtpCode()" id="btnSendOtp" class="w-full bg-[#047857] hover:bg-emerald-800 text-white font-black py-2.5 px-4 rounded-xl shadow-md flex items-center justify-center space-x-2 transition">
            <i data-lucide="send" class="w-4 h-4 text-amber-300"></i>
            <span class="text-xs">Gmail Par 6-Digit Code (OTP) Bhejein</span>
          </button>
        </div>

        <!-- OTP Step 2: Enter 6-Digit Code Sent to Gmail -->
        <div id="otpStep2" class="space-y-3 hidden">
          <div class="bg-amber-50 border border-amber-200 rounded-2xl p-3 text-center space-y-1">
            <p class="text-xs font-bold text-amber-900">Code aap ke Gmail par bhej diya gaya hai!</p>
            <p class="text-[11px] text-amber-700 font-medium">
              Bara-e-karam apna <span id="lblSentEmail" class="font-bold underline"></span> ka Inbox ya Spam folder check karein.
            </p>
          </div>

          <div>
            <label class="block text-[11px] font-bold text-gray-700 mb-1">6-Hanso Ka Verification Code (OTP) <span class="text-rose-500">*</span></label>
            <input type="text" id="inpOtpToken" maxlength="8" placeholder="Jaise: 123456" class="w-full border-2 border-emerald-500 rounded-xl px-3 py-2.5 text-center text-lg font-black tracking-widest outline-none focus:ring-2 focus:ring-emerald-500" />
          </div>

          <button type="button" onclick="verifyGmailOtpCode()" id="btnVerifyOtp" class="w-full bg-[#047857] hover:bg-emerald-800 text-white font-black py-3 px-4 rounded-xl shadow-md flex items-center justify-center space-x-2 transition">
            <i data-lucide="shield-check" class="w-4 h-4 text-amber-300"></i>
            <span class="text-xs">Code Verify Karein & Account Banayein</span>
          </button>

          <div class="flex items-center justify-between pt-1 text-[11px]">
            <button type="button" onclick="resetOtpStep()" class="text-gray-500 hover:text-gray-800 font-semibold underline">
              Email tabdeel karein
            </button>
            <button type="button" onclick="sendGmailOtpCode()" class="text-[#047857] hover:text-emerald-800 font-bold underline">
              Dobara code bhejein
            </button>
          </div>
        </div>
      </div>

      <!-- TAB 2: EMAIL & PASSWORD SYSTEM -->
      <div id="authTabPassSection" class="space-y-3 hidden">
        <div>
          <label class="block text-[11px] font-bold text-gray-700 mb-1">Gmail / Email Address <span class="text-rose-500">*</span></label>
          <input type="email" id="inpPassEmail" placeholder="apna.name@gmail.com" class="w-full border-2 border-gray-200 rounded-xl px-3 py-2 text-xs font-semibold outline-none focus:border-[#047857] transition" />
        </div>

        <div>
          <label class="block text-[11px] font-bold text-gray-700 mb-1">Password <span class="text-rose-500">*</span></label>
          <input type="password" id="inpPassPassword" placeholder="Kam az kam 6 characters" class="w-full border-2 border-gray-200 rounded-xl px-3 py-2 text-xs font-semibold outline-none focus:border-[#047857] transition" />
        </div>

        <div>
          <label class="block text-[11px] font-bold text-gray-700 mb-1">Aap Ka Naam (Naye Account Ke Liye)</label>
          <input type="text" id="inpPassName" placeholder="Misaal: Hoor Fahim" class="w-full border-2 border-gray-200 rounded-xl px-3 py-2 text-xs font-semibold outline-none focus:border-[#047857] transition" />
        </div>

        <div class="grid grid-cols-2 gap-2 pt-1">
          <button type="button" onclick="handlePasswordLogin()" id="btnPassLogin" class="w-full bg-[#047857] hover:bg-emerald-800 text-white font-black py-2.5 px-3 rounded-xl shadow-sm text-xs transition">
            Login Karein
          </button>
          <button type="button" onclick="handlePasswordSignUp()" id="btnPassSignUp" class="w-full bg-white hover:bg-gray-50 border-2 border-[#047857] text-[#047857] font-black py-2.5 px-3 rounded-xl shadow-sm text-xs transition">
            Naya Account
          </button>
        </div>
      </div>

      <!-- Footer Note -->
      <div class="text-center pt-2 border-t border-gray-100">
        <p class="text-[10px] text-gray-400 font-medium">
          🔒 Supabase Secured · Verified Reseller Status · Free Registration
        </p>
      </div>

    </div>
  </div>

  <!-- ==================== MODAL 1: PRODUCT DETAILS VIEW ==================== -->'''

content = re.sub(old_modal_regex, new_modal_html, content)

# Now update the JavaScript Authentication Code
old_js_regex = r'// ==================== AUTHENTICATION \(GOOGLE & DIRECT GMAIL\) ====================[\s\S]*?// ==================== RENDER CATEGORIES ===================='

new_js_code = '''// ==================== REAL AUTHENTICATION (GOOGLE OAUTH, GMAIL OTP & PASSWORD) ====================
    let pendingOtpEmail = '';
    let pendingOtpName = '';

    // Initialize Auth Listener & Session on page load
    async function checkAuthSession() {
      try {
        // Listen to live Supabase Auth changes
        supabaseClient.auth.onAuthStateChange(async (event, session) => {
          if (session && session.user) {
            await handleAuthSuccess(session.user);
          } else if (event === 'SIGNED_OUT') {
            enforceGuestUI();
          }
        });

        // Check active session
        const { data: { session } } = await supabaseClient.auth.getSession();
        if (session && session.user) {
          await handleAuthSuccess(session.user);
          return;
        }
      } catch (err) {
        console.warn('Supabase getSession check:', err);
      }

      // Check local storage backup
      const savedUser = localStorage.getItem('tejarat_user');
      if (savedUser) {
        try {
          const u = JSON.parse(savedUser);
          if (u && u.verified) {
            applyLoggedInUserUI(u);
            return;
          }
        } catch (e) {}
      }

      // Default to Guest Mode
      enforceGuestUI();
    }

    // Switch between OTP and Password tabs
    function switchAuthTab(tab) {
      const otpSec = document.getElementById('authTabOtpSection');
      const passSec = document.getElementById('authTabPassSection');
      const btnOtp = document.getElementById('tabBtnOtp');
      const btnPass = document.getElementById('tabBtnPass');

      if (tab === 'otp') {
        otpSec.classList.remove('hidden');
        passSec.classList.add('hidden');
        btnOtp.className = 'flex-1 py-1.5 rounded-lg bg-white text-gray-900 shadow-sm transition text-center';
        btnPass.className = 'flex-1 py-1.5 rounded-lg text-gray-600 hover:text-gray-900 transition text-center';
      } else {
        otpSec.classList.add('hidden');
        passSec.classList.remove('hidden');
        btnPass.className = 'flex-1 py-1.5 rounded-lg bg-white text-gray-900 shadow-sm transition text-center';
        btnOtp.className = 'flex-1 py-1.5 rounded-lg text-gray-600 hover:text-gray-900 transition text-center';
      }
      lucide.createIcons();
    }

    // 1. Google OAuth
    async function handleGoogleOAuth() {
      try {
        showToast('Google OAuth service se rabta kiya ja raha hai...');
        const { data, error } = await supabaseClient.auth.signInWithOAuth({
          provider: 'google',
          options: {
            redirectTo: window.location.href
          }
        });
        if (error) {
          console.warn('OAuth redirect error:', error);
          showToast('Google Cloud OAuth Supabase console mein connect hone tak, Gmail OTP Code se login karein!');
          switchAuthTab('otp');
        }
      } catch (err) {
        console.error('Google OAuth exception:', err);
        showToast('Bara-e-karam Gmail OTP Code istemal karein!');
        switchAuthTab('otp');
      }
    }

    // 2. Send 6-Digit Gmail OTP Code
    async function sendGmailOtpCode() {
      const inp = document.getElementById('inpOtpEmail');
      const email = inp ? inp.value.trim().toLowerCase() : '';
      const nameInp = document.getElementById('inpOtpName');
      const name = nameInp ? nameInp.value.trim() : '';

      if (!email || !email.includes('@')) {
        showToast('Bara-e-karam apna durust Gmail / Email darj karein!');
        return;
      }

      pendingOtpEmail = email;
      pendingOtpName = name || email.split('@')[0];

      const btn = document.getElementById('btnSendOtp');
      const origText = btn.innerHTML;
      btn.innerHTML = '<span>Code bheja ja raha hai...</span>';
      btn.disabled = true;

      try {
        const { data, error } = await supabaseClient.auth.signInWithOtp({
          email: email,
          options: {
            shouldCreateUser: true
          }
        });

        if (error) {
          showToast('Error: ' + error.message);
          btn.innerHTML = origText;
          btn.disabled = false;
          return;
        }

        // Successfully sent OTP
        document.getElementById('lblSentEmail').innerText = email;
        document.getElementById('otpStep1').classList.add('hidden');
        document.getElementById('otpStep2').classList.remove('hidden');
        showToast('✓ 6-Digit Code aap ke Gmail par bhej diya gaya hai!');
        lucide.createIcons();
      } catch (err) {
        showToast('Error: ' + (err.message || 'Internet issue'));
      } finally {
        btn.innerHTML = origText;
        btn.disabled = false;
      }
    }

    // Reset OTP back to step 1
    function resetOtpStep() {
      document.getElementById('otpStep1').classList.remove('hidden');
      document.getElementById('otpStep2').classList.add('hidden');
      lucide.createIcons();
    }

    // 3. Verify Gmail 6-Digit OTP Code
    async function verifyGmailOtpCode() {
      const tokenInp = document.getElementById('inpOtpToken');
      const token = tokenInp ? tokenInp.value.trim() : '';

      if (!token || token.length < 4) {
        showToast('Bara-e-karam Gmail par aya hua 6-digit code darj karein!');
        return;
      }

      const btn = document.getElementById('btnVerifyOtp');
      const origText = btn.innerHTML;
      btn.innerHTML = '<span>Code verify ho raha hai...</span>';
      btn.disabled = true;

      try {
        const { data, error } = await supabaseClient.auth.verifyOtp({
          email: pendingOtpEmail,
          token: token,
          type: 'email'
        });

        if (error) {
          showToast('Ghalat code! Bara-e-karam durust code darj karein.');
          btn.innerHTML = origText;
          btn.disabled = false;
          return;
        }

        if (data && data.user) {
          await handleAuthSuccess(data.user, pendingOtpName);
        } else {
          showToast('Verification kamyab!');
        }
      } catch (err) {
        showToast('Verification failed: ' + (err.message || 'Error'));
      } finally {
        btn.innerHTML = origText;
        btn.disabled = false;
      }
    }

    // 4. Password Login
    async function handlePasswordLogin() {
      const email = document.getElementById('inpPassEmail').value.trim().toLowerCase();
      const password = document.getElementById('inpPassPassword').value;

      if (!email || !password) {
        showToast('Bara-e-karam Email aur Password dono darj karein!');
        return;
      }

      const btn = document.getElementById('btnPassLogin');
      btn.innerText = 'Checking...';
      btn.disabled = true;

      try {
        const { data, error } = await supabaseClient.auth.signInWithPassword({
          email: email,
          password: password
        });

        if (error) {
          showToast('Login Failed: ' + error.message);
          return;
        }

        if (data && data.user) {
          await handleAuthSuccess(data.user);
        }
      } catch (err) {
        showToast('Error: ' + err.message);
      } finally {
        btn.innerText = 'Login Karein';
        btn.disabled = false;
      }
    }

    // 5. Password Sign Up
    async function handlePasswordSignUp() {
      const email = document.getElementById('inpPassEmail').value.trim().toLowerCase();
      const password = document.getElementById('inpPassPassword').value;
      const name = document.getElementById('inpPassName').value.trim();

      if (!email || !password || password.length < 6) {
        showToast('Email aur kam az kam 6-digit password darj karein!');
        return;
      }

      const btn = document.getElementById('btnPassSignUp');
      btn.innerText = 'Ban raha hai...';
      btn.disabled = true;

      try {
        const { data, error } = await supabaseClient.auth.signUp({
          email: email,
          password: password,
          options: {
            data: {
              full_name: name || email.split('@')[0]
            }
          }
        });

        if (error) {
          showToast('Signup Failed: ' + error.message);
          return;
        }

        if (data && data.user) {
          await handleAuthSuccess(data.user, name);
          showToast('✓ Account ban gaya!');
        }
      } catch (err) {
        showToast('Error: ' + err.message);
      } finally {
        btn.innerText = 'Naya Account';
        btn.disabled = false;
      }
    }

    // 6. Handle Successful Authentication (Local state + Supabase reseller_wallets Sync)
    async function handleAuthSuccess(user, customName) {
      const email = user.email || '';
      const rawName = customName || (user.user_metadata && user.user_metadata.full_name) || email.split('@')[0] || 'Reseller Partner';
      const cleanName = rawName.charAt(0).toUpperCase() + rawName.slice(1);
      const storeName = cleanName.endsWith('Store') ? cleanName : (cleanName + ' Online Store');

      const userObj = {
        id: user.id,
        email: email,
        full_name: cleanName,
        store_name: storeName,
        provider: user.app_metadata ? user.app_metadata.provider : 'gmail',
        verified: true,
        verified_at: user.confirmed_at || new Date().toISOString()
      };

      // Persist locally
      localStorage.setItem('tejarat_user', JSON.stringify(userObj));
      currentUser = userObj;

      // Update UI elements
      applyLoggedInUserUI(userObj);
      closeAuthModal();

      // Sync wallet record to Supabase (visible in Admin Panel!)
      try {
        await supabaseClient.from('reseller_wallets').upsert({
          user_id: user.id,
          email: email,
          phone: email,
          store_name: storeName,
          available_balance: 0,
          pending_profit: 0,
          total_withdrawn: 0,
          completed_orders: 0
        }, { onConflict: 'user_id' });
      } catch (err) {
        console.warn('Supabase reseller_wallets upsert error:', err);
      }

      showToast(`✓ Welcome ${cleanName}! Account verified ho gaya!`);
    }

    // 7. Apply Logged In UI
    function applyLoggedInUserUI(u) {
      // Top Bar Header Badge -> Show VERIFIED in Gold
      const headerBadge = document.getElementById('headerBrandBadge');
      if (headerBadge) {
        headerBadge.innerText = '✓ VERIFIED';
        headerBadge.className = 'text-[9px] bg-amber-400 text-gray-950 font-black px-1.5 py-0.5 rounded uppercase shadow-sm flex items-center space-x-0.5';
      }

      // Profile Tab Card
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

      // Store Name & Subtitle
      const storeSub = document.getElementById('bizStoreSubtitle');
      if (storeSub) storeSub.innerText = '✓ Verified Reseller Store';

      const storeName = document.getElementById('bizStoreName');
      if (storeName && u.store_name) storeName.innerText = u.store_name;

      // Auth Button -> Logout
      const btn = document.getElementById('authActionBtn');
      if (btn) {
        btn.innerText = 'Logout';
        btn.className = 'bg-rose-50 text-rose-600 border border-rose-200 text-xs font-black px-3.5 py-2 rounded-xl shadow-sm transition hover:bg-rose-100';
        btn.onclick = logoutUser;
      }
    }

    // 8. Enforce Guest Mode (When Logged Out)
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

    // 9. Logout
    async function logoutUser() {
      try {
        await supabaseClient.auth.signOut();
      } catch (e) {}
      localStorage.removeItem('tejarat_user');
      currentUser = null;
      enforceGuestUI();
      showToast('Account se logout ho gaye.');
    }

    // 10. Open/Close Modal
    function openAuthModal() {
      const savedUser = localStorage.getItem('tejarat_user');
      if (savedUser) {
        try {
          const u = JSON.parse(savedUser);
          if (u.email && document.getElementById('inpOtpEmail')) {
            document.getElementById('inpOtpEmail').value = u.email;
          }
          if (u.full_name && document.getElementById('inpOtpName')) {
            document.getElementById('inpOtpName').value = u.full_name;
          }
        } catch(e) {}
      }
      resetOtpStep();
      document.getElementById('authModal').classList.remove('hidden');
      lucide.createIcons();
    }

    function closeAuthModal() {
      document.getElementById('authModal').classList.add('hidden');
    }

    // ==================== RENDER CATEGORIES ===================='''

content = re.sub(old_js_regex, new_js_code, content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html updated with real Google OAuth and Gmail OTP Auth successfully!")
