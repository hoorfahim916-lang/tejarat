$baseDir = "C:\Users\LENOVO\Downloads\TEJARAT APP"
$srcDir = Join-Path $baseDir "android_source"
$buildDir = Join-Path $srcDir "build"
$aapt = "E:\tools\android-sdk\build-tools\35.0.0\aapt.exe"
$d8 = "E:\tools\android-sdk\build-tools\35.0.0\d8.bat"
$zipalign = "E:\tools\android-sdk\build-tools\35.0.0\zipalign.exe"
$apksigner = "E:\tools\android-sdk\build-tools\35.0.0\apksigner.bat"
$androidJar = "E:\tools\android-sdk\platforms\android-35\android.jar"
$javac = "E:\tools\jdk21\bin\javac.exe"
$keystore = Join-Path $baseDir "tejarat-release.keystore"

Set-Location $srcDir

if (Test-Path $buildDir) { 
    Remove-Item -Recurse -Force $buildDir 
}
$null = New-Item -ItemType Directory -Path (Join-Path $buildDir "gen") -Force
$null = New-Item -ItemType Directory -Path (Join-Path $buildDir "classes") -Force
$null = New-Item -ItemType Directory -Path (Join-Path $buildDir "dex") -Force

Write-Host "Step 1: Generating R.java and package resource unaligned.apk..."
& $aapt package -f -m -J (Join-Path $buildDir "gen") -M AndroidManifest.xml -S res -A assets -I $androidJar -F (Join-Path $buildDir "unaligned.apk")
if ($LASTEXITCODE -ne 0) { throw "aapt package failed with code $LASTEXITCODE" }

Write-Host "Step 2: Compiling Java source..."
$javaFiles = @(
    (Join-Path $srcDir "java\com\tejarat\reseller\app\MainActivity.java"),
    (Join-Path $buildDir "gen\com\tejarat\reseller\app\R.java")
)
& $javac -nowarn -source 1.8 -target 1.8 -bootclasspath $androidJar -d (Join-Path $buildDir "classes") $javaFiles
if ($LASTEXITCODE -ne 0) { throw "javac failed with code $LASTEXITCODE" }

Write-Host "Step 3: Compiling classes to DEX..."
$dexOut = Join-Path $buildDir "dex"
$classFiles = (Get-ChildItem (Join-Path $buildDir "classes\com\tejarat\reseller\app\*.class")).FullName
$d8Args = @("--release", "--min-api", "24", "--lib", $androidJar, "--output", $dexOut) + $classFiles
& cmd /c "$d8" $d8Args
if ($LASTEXITCODE -ne 0) { throw "d8 failed with code $LASTEXITCODE" }

Write-Host "Step 4: Adding classes.dex to APK..."
$apkPath = Join-Path $buildDir "unaligned.apk"
$dexPath = Join-Path $buildDir "dex\classes.dex"
Set-Location (Join-Path $buildDir "dex")
& $aapt add $apkPath "classes.dex"
Set-Location $srcDir
if ($LASTEXITCODE -ne 0) { throw "aapt add failed with code $LASTEXITCODE" }

Write-Host "Step 5: Zipalign APK..."
$alignedApk = Join-Path $buildDir "aligned.apk"
& $zipalign -f -p 4 $apkPath $alignedApk
if ($LASTEXITCODE -ne 0) { throw "zipalign failed with code $LASTEXITCODE" }

Write-Host "Step 6: Signing APK with release keystore..."
$outApk = Join-Path $baseDir "Tejarat-App-v3.3-PRO.apk"
& cmd /c "$apksigner" sign --ks $keystore --ks-pass pass:tejarat123 --out "$outApk" "$alignedApk"
if ($LASTEXITCODE -ne 0) { throw "apksigner failed with code $LASTEXITCODE" }

Write-Host "Step 7: Verifying signed APK..."
& cmd /c "$apksigner" verify "$outApk"
if ($LASTEXITCODE -ne 0) { throw "apksigner verify failed with code $LASTEXITCODE" }

# Also sync other filenames
Copy-Item "$outApk" (Join-Path $baseDir "Tejarat-App-v3.2-PRO.apk") -Force
Copy-Item "$outApk" (Join-Path $baseDir "Tejarat-App-v3.1-MidnightGold.apk") -Force

Write-Host "SUCCESS! Output APK generated at: $outApk"
