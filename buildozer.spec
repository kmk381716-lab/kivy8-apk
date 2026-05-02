[app]

# (اسم برنامه)
title = My Kivy App

# (نام بسته برنامه - باید یونیک باشه)
package.name = mykivyapp

# (شناسه منحصر به فرد برنامه - معمولا معادل معکوس دامنه)
package.domain = org.kivy.mykivyapp

# (نسخه برنامه)
version = 0.1

# (فایل ورودی برنامه)
source.include_exts = py,png,jpg,kv,atlas

# (فایل اصلی پایتون)
source.main = main.py

# (کتابخانه‌های لازم برای نصب در اندروید)
requirements = python3,kivy

# (نسخه SDK اندروید - Buildozer به طور خودکار می‌سازد)
android.api = 33

# (نسخه minSdk - حداقل نسخه اندروید)
android.minapi = 21

# (نسخه targetSdk)
android.target = 33

# (ساخت فایل APK بصورت debug - برای انتشار باید تغییر بدی)
android.debug = 1

# (درصورت نیاز به جاوا ۱۷)
android.gradle_dependencies =

# (حق دسترسی‌ها - اگر نیاز به اینترنت یا دوربین داری اینجا اضافه کن)
android.permissions = INTERNET

# (این خط باعث می‌شود بسته apk در خروجی bin ساخته شود)
android.arch = armeabi-v7a

# (پاکسازی فایل های موقت پس از ساخت)
build.clean = 1
