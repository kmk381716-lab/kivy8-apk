[app]

title = My Kivy App
package.name = mykivyapp
package.domain = org.kivy.mykivyapp
version = 0.1

source.include_exts = py,png,jpg,kv,atlas

source.dir = .

source.main = main.py

requirements = python3,kivy

android.api = 33
android.minapi = 21
android.target = 33
android.debug = 1

android.permissions = INTERNET

android.arch = armeabi-v7a

build.clean = 1
