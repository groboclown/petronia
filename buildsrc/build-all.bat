@echo off
setlocal

set _H=%~dp0

:start
if M%1M == MM goto end
echo Generating builds for %1
call %_H%\setup-build.bat %1
call %_H%\build-one.bat %1
shift
goto start

:end
endlocal
