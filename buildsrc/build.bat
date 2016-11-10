@echo off
setlocal

rem Note that "pyinstaller.exe" must be in the Path.
rem Usually, you'll find it in your Python directory, under Scripts.

set HERE=%~dp0
cd %HERE%\..
rmdir buildsrc\work\build /s /q > NUL 2>&1
rmdir buildsrc\work\dist /s /q > NUL 2>&1
del buildsrc\work\*.spec /q > NUL 2>&1
mkdir buildsrc\work > NUL 2>&1
for %%i in (check_layout cmd detect_apps detect_keys detect_monitors main) do (
    echo Building %%i ...
    type buildsrc\%%i.header buildsrc\base.spec > buildsrc\work\%%i.spec 2> NUL
    rmdir buildsrc\work\build\%%i /s /q > NUL 2>&1
    pyinstaller --distpath=buildsrc/work/dist --workpath=buildsrc/work/build buildsrc/work/%%i.spec > NUL 2>&1
)

python buildsrc/bundle.py buildsrc/work/dist

endlocal
