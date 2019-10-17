# Running In Windows

1. Create a virtual environment for Petronia.
1. Import the `requirements.txt` for the developer requirements.
1. Run the "activate.ps1" script in that environment to start using it.
1. Unless otherwise noted, all these commands are run while in the `src` directory.

## Run Petronia

```bat
> clear ; python -m petronia.boot --config-dir ..\example-setup\win10
```


## Run the MyPy Linter

```bat
> clear ; python -m mypy --warn-unused-configs --no-incremental --package petronia
```


## Run Unit Tests

```bat
> clear ; python -m coverage run --source . -m unittest discover -s . -p "*_test.py"

# To view the generated coverage report
> python -m coverage report -m
```


## Generate Documentation

```bat
> python ../bin/mk_docs.py
```
