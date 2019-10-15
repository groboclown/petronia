@echo off
setlocal
if M%1M == MM goto error
goto run

:error
echo Must specify the Python installation to use as argument 1.
goto end

:run
set Path=%1;%Path%

python -m pip install pypiwin32
python -m pip install PyInstaller

rem PyInstaller is located in your Python directory, at Scripts\pyinstaller.exe

:end
endlocal
