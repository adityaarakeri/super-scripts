@echo off
taskkill /f /IM explorer.exe
CD /d %userprofile%\AppData\Local
DEL IconCache.db /a
Start explorer.exe
