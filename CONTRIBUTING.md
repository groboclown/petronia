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
python bin/build.py projects

(Bash)
python3 bin/build.py projects
```

If your changes include updates to localization strings, the translation files will also need updates.


## Translations

...

## Documentation

...