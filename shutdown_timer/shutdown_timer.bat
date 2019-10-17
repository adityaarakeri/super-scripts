@echo off
color 0A

:start
set /p min=Time (in minutes) until shutting down - enter "a" to abort:

if not defined min (
  cls
  goto start
)

set /a test = %min%*1

if %test% LEQ 0 (
  if %min% == a (
    goto cancel
  )
  cls
  goto start
)

set /a zeit = %min%*60
echo Shutdown in %min% minutes
pause
shutdown.exe -s -t %zeit% -f
exit

:cancel
echo.
echo Abort Timer?
pause
shutdown.exe -a
