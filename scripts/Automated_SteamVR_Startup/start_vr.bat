@echo off

cd /d "...\Steam\" REM Make sure to replace '...' with your path leading up to \Steam\!
start Steam.exe

timeout /T 15 /nobreak >nul REM 15 second timer to allow Steam to fully start up.

REM These lines check if Steam is open, and if so, VR is started.
tasklist /fi "imagename eq steam.exe" |find ":" > nul
if errorlevel 1 (
cd /d "...\Steam\steamapps\Common\SteamVR\bin\win64" REM Make sure to replace '...' with your path leading up to \Steam\!
start vrstartup.exe
)
