@echo off
setlocal

set HERE=%~dp0
set PROJECTS=%HERE%projects
set SETUP=%HERE%example-setup\win10

REM need a way to default the language
set LANGUAGE=en_US

REM for now, because the system is split up between projects, the python path needs to be set.
set PYTHONPATH=%PROJECTS%\foreman;%PROJECTS%\py-common-lib;%PROJECTS%\py-extension-lib;%PROJECTS%\extension-loader;%PROJECTS%\extension-runner;%PROJECTS%\native-handler;%PROJECTS%\core-extensions;%PROJECTS%\portal

python -m petronia_foreman -c %SETUP%\petronia.ini --config-dir %SETUP%\system\config --config-dir %SETUP%\user --data-dir %SETUP%\system\data --data-dir %PROJECTS%\l10n\compiled %*

endlocal
