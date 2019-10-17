@echo off

set /p clear="Clean temporary folder (y/n): "
echo.
if "%clear%" == "y" (
	del /Q %USERPROFILE%\AppData\Local\Temp\*.*
	echo Temporary folder has been cleaned.
) else (
	echo Files remain in temporary folder.
)

pause
