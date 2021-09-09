# How To Contribute

## Questions


## Bugs, Feature Requests


## Pull Requests

...


## Code

To contribute code, you must follow the [coding guidelines](docs/coding_standards.md).  Additionally, your code must pass all checks.

To set up your environment, run:

```bash
(Windows PowerShell)
python -m venv .venv/windows
.venv\windows\Scripts\activate.ps1
python -m pip install -r bin\requirements.txt
python -m pip install -r bin\test-requirements.txt

(Bash)
python3 -m venv .venv/linux
. .venv/linux/bin/acivate
python3 -m pip install -r bin/requirements.txt
python3 -m pip install -r bin/test-requirements.txt
```

To run the coding style and test checks, make sure your environment is setup, and run:

```bash
(Windows)
.venv/windows/
python bin/build.py

(Bash)
python3 bin/build.py
```

The Travis build will run on both Windows and Linux, so this will need to pass on both.

If your changes include updates to localization strings, the translation files will also need updates.  This can be done by running the script [extract-message-catalog.sh](bin/extract-message-catalog.sh).

You can run a sub-set of the projects by passing the project name (not directory) as an argument to the `build.py` script.

## Translations

Details around writing localizations and translatable code are in the [l10n](projects/l10n/README.md) project.

## Documentation

...
