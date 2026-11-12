package com.tejarat.reseller.app;

import android.app.Activity;
import android.app.AlertDialog;
import android.app.DownloadManager;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Color;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.util.Log;
import android.view.KeyEvent;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.webkit.ConsoleMessage;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

/**
 * Tejarat Reseller App — WebView shell.
 *
 * OTA strategy (2 layers):
 *  1. CONTENT OTA  — the whole UI is a web app hosted on GitHub Pages.
 *     When the device is online we load the LIVE url, so every push to
 *     GitHub updates every installed app on its next launch. If the network
 *     is unavailable (or the live url fails) we fall back to the bundled
 *     copy in assets/, so the app always works offline.
 *
 *  2. APK OTA — we poll the Supabase `app_settings` table for a newer
 *     `app_build_number` / `app_version`. When one exists the user is
 *     prompted to download the new APK (the link comes from
 *     `apk_download_url`). `force_update` makes the prompt non-dismissable.
 */
public class MainActivity extends Activity {

    private static final String TAG = "Tejarat";

    private static final String LOCAL_ASSET_URL = "file:///android_asset/index.html";
    private static final String LIVE_OTA_URL = "https://hoorfahim916-lang.github.io/tejarat/";

    private static final String SUPABASE_URL = "https://xdsxmgzcfihkohsbzszq.supabase.co";
    private static final String SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inhkc3htZ3pjZmloa29oc2J6c3pxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTM3MDA2NzUsImV4cCI6MjEwOTI3NjY3NX0.kDUmA2E1BGl-oja9aosoBO4KQWCl7wxTRrOzxIiR-7g";
    private static final String SETTINGS_ENDPOINT = SUPABASE_URL + "/rest/v1/app_settings?select=app_version,app_build_number,force_update,apk_download_url,update_notes&id=eq.global";

    // Must match AndroidManifest.xml
    private static final int APP_VERSION_CODE = 37;
    private static final String APP_VERSION_NAME = "3.7.0";

    private WebView webView;
    private boolean isLoadedFallback = false;
    private boolean updateDialogShown = false;

    private final Handler mainHandler = new Handler(Looper.getMainLooper());

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        requestWindowFeature(Window.FEATURE_NO_TITLE);
        Window window = getWindow();
        window.addFlags(WindowManager.LayoutParams.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS);
        window.setStatusBarColor(Color.parseColor("#02704D"));
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            window.setNavigationBarColor(Color.parseColor("#FFFFFF"));
            window.getDecorView().setSystemUiVisibility(View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR);
        }

        window.setFlags(
                WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED,
                WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED
        );

        webView = new WebView(this);
        webView.setScrollBarStyle(View.SCROLLBARS_INSIDE_OVERLAY);
        webView.setVerticalScrollBarEnabled(false);
        webView.setHorizontalScrollBarEnabled(false);
        webView.setOverScrollMode(View.OVER_SCROLL_NEVER);
        webView.setBackgroundColor(Color.parseColor("#F3F4F5"));
        webView.setFitsSystemWindows(true);
        setContentView(webView);

        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setDatabaseEnabled(true);
        settings.setAllowFileAccess(true);
        settings.setAllowContentAccess(true);
        settings.setLoadWithOverviewMode(true);
        settings.setUseWideViewPort(true);
        settings.setSupportZoom(false);
        settings.setBuiltInZoomControls(false);
        settings.setDisplayZoomControls(false);
        settings.setCacheMode(WebSettings.LOAD_DEFAULT);
        settings.setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);

        webView.setWebChromeClient(new WebChromeClient() {
            @Override
            public boolean onConsoleMessage(ConsoleMessage consoleMessage) {
                return super.onConsoleMessage(consoleMessage);
            }
        });

        webView.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                if (url == null) return false;

                // Open WhatsApp, dialer, email, Google accounts externally
                if (url.startsWith("whatsapp://")
                        || url.contains("wa.me/")
                        || url.contains("api.whatsapp.com")
                        || url.startsWith("tel:")
                        || url.startsWith("mailto:")
                        || url.contains("accounts.google.com")
                        || url.contains("myaccount.google.com")
                        || url.contains("/auth/v1/authorize")) {
                    try {
                        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
                        startActivity(intent);
                        return true;
                    } catch (Exception e) {
                        return false;
                    }
                }

                // Keep internal app navigation inside the webview
                if (url.startsWith("file://")
                        || url.contains("github.io")
                        || url.contains("supabase.co")) {
                    return false;
                }

                try {
                    Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
                    startActivity(intent);
                    return true;
                } catch (Exception ignored) {
                    return false;
                }
            }

            @Override
            public void onReceivedError(WebView view, int errorCode, String description, String failingUrl) {
                super.onReceivedError(view, errorCode, description, failingUrl);
                // If the live OTA url failed, gracefully load the bundled offline asset
                if (!isLoadedFallback) {
                    isLoadedFallback = true;
                    view.loadUrl(LOCAL_ASSET_URL);
                }
            }
        });

        // Smart OTA auto-update: online -> live GitHub Pages build, offline -> bundled asset
        if (isNetworkAvailable()) {
            webView.loadUrl(LIVE_OTA_URL);
            checkForApkUpdate();
        } else {
            isLoadedFallback = true;
            webView.loadUrl(LOCAL_ASSET_URL);
        }
    }

    // ------------------------------------------------------------------
    // APK OTA — polls Supabase app_settings for a newer build
    // ------------------------------------------------------------------
    private void checkForApkUpdate() {
        new Thread(new Runnable() {
            @Override
            public void run() {
                final JSONObject remote = fetchRemoteSettings();
                if (remote == null) return;

                final int remoteBuild = remote.optInt("app_build_number", 0);
                final String remoteVersion = remote.optString("app_version", "");
                final boolean forceUpdate = remote.optBoolean("force_update", false);
                final String apkUrl = remote.optString("apk_download_url", "");
                final String notes = remote.optString("update_notes", "");

                if (remoteBuild <= APP_VERSION_CODE && !(forceUpdate && remoteBuild > 0)) {
                    return;
                }
                if (apkUrl.length() == 0) {
                    Log.i(TAG, "Update available (" + remoteVersion + ") but no APK url configured");
                    return;
                }

                mainHandler.post(new Runnable() {
                    @Override
                    public void run() {
                        showUpdateDialog(remoteVersion, notes, apkUrl, forceUpdate);
                    }
                });
            }
        }).start();
    }

    private JSONObject fetchRemoteSettings() {
        HttpURLConnection conn = null;
        try {
            conn = (HttpURLConnection) new URL(SETTINGS_ENDPOINT).openConnection();
            conn.setRequestMethod("GET");
            conn.setConnectTimeout(8000);
            conn.setReadTimeout(8000);
            conn.setRequestProperty("apikey", SUPABASE_ANON_KEY);
            conn.setRequestProperty("Authorization", "Bearer " + SUPABASE_ANON_KEY);
            conn.setRequestProperty("Accept", "application/json");

            if (conn.getResponseCode() != 200) {
                Log.w(TAG, "app_settings fetch returned " + conn.getResponseCode());
                return null;
            }

            BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            StringBuilder sb = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) sb.append(line);
            reader.close();

            JSONArrayWrapper wrapper = JSONArrayWrapper.first(sb.toString());
            return wrapper != null ? wrapper.object : null;
        } catch (Exception e) {
            Log.w(TAG, "app_settings fetch failed: " + e.getMessage());
            return null;
        } finally {
            if (conn != null) conn.disconnect();
        }
    }

    /** Tiny helper that pulls the first object out of a PostgREST array response. */
    private static class JSONArrayWrapper {
        final JSONObject object;

        JSONArrayWrapper(JSONObject object) {
            this.object = object;
        }

        static JSONArrayWrapper first(String json) {
            try {
                int start = json.indexOf('{');
                int end = json.lastIndexOf('}');
                if (start < 0 || end <= start) return null;
                return new JSONArrayWrapper(new JSONObject(json.substring(start, end + 1)));
            } catch (Exception e) {
                return null;
            }
        }
    }

    private void showUpdateDialog(String version, String notes, final String apkUrl, boolean forceUpdate) {
        if (updateDialogShown || isFinishing()) return;
        updateDialogShown = true;

        String message = "Tejarat App ki nayi version (" + version + ") aa gayi hai.\n\n"
                + (notes.length() > 0 ? notes + "\n\n" : "")
                + "Update abhi install karein taake naye features foran mil jayein.";
        if (forceUpdate) {
            message = "Update zaroori hai — app istemal karne ke liye version update karna zaroori hai.\n\n" + message;
        }

        AlertDialog.Builder builder = new AlertDialog.Builder(this)
                .setTitle("📲 Tejarat App Update")
                .setMessage(message)
                .setCancelable(false)
                .setPositiveButton("Update Now", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        downloadApk(apkUrl);
                    }
                });

        if (!forceUpdate) {
            builder.setNegativeButton("Abhi Nahi", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    updateDialogShown = false;
                }
            });
        }

        builder.show();
    }

    private void downloadApk(String apkUrl) {
        try {
            Uri uri = Uri.parse(apkUrl);
            Intent intent = new Intent(Intent.ACTION_VIEW, uri);
            startActivity(intent);
        } catch (Exception e) {
            try {
                DownloadManager dm = (DownloadManager) getSystemService(Context.DOWNLOAD_SERVICE);
                dm.enqueue(new DownloadManager.Request(Uri.parse(apkUrl))
                        .setTitle("Tejarat App Update")
                        .setDescription("Naya version download ho raha hai…")
                        .setNotificationVisibility(DownloadManager.Request.VISIBILITY_VISIBLE_NOTIFY_COMPLETED)
                        .setDestinationInExternalPublicDir(android.os.Environment.DIRECTORY_DOWNLOADS, "Tejarat-App-Update.apk"));
                Toast("Update download ho raha hai — notification check karein.");
            } catch (Exception e2) {
                Toast("Update link open nahi ho saka.");
            }
        }
    }

    private void Toast(String msg) {
        android.widget.Toast.makeText(this, msg, android.widget.Toast.LENGTH_LONG).show();
    }

    private boolean isNetworkAvailable() {
        try {
            ConnectivityManager cm = (ConnectivityManager) getSystemService(Context.CONNECTIVITY_SERVICE);
            NetworkInfo activeNetwork = cm.getActiveNetworkInfo();
            return activeNetwork != null && activeNetwork.isConnectedOrConnecting();
        } catch (Exception e) {
            return false;
        }
    }

    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        if (keyCode == KeyEvent.KEYCODE_BACK && webView != null && webView.canGoBack()) {
            webView.goBack();
            return true;
        }
        return super.onKeyDown(keyCode, event);
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (webView != null) webView.onResume();
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (webView != null) webView.onPause();
    }

    @Override
    protected void onDestroy() {
        if (webView != null) {
            webView.destroy();
            webView = null;
        }
        super.onDestroy();
    }
}
