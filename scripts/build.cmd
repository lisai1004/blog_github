@echo off

set ZIM=C:\Program Files (x86)\Zim Desktop Wiki\zim.exe
if not exist "%ZIM%" set ZIM=C:\Program Files\Zim Desktop Wiki\zim.exe
if not exist "%ZIM%" set ZIM=zim.exe

cd /d "%~dp0"
cd ..

mkdir build 2>NUL
cd build
if exist _resources del /s /q *.* >NUL
cd ..
"%ZIM%" --export ^
  --format=html --template=Print ^
  --output=./build --index-page=sitemap ^
  cplus_class
