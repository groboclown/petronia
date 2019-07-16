# Create a Distribution

Petronia has been designed to be a simple to distribute project.

## Release Preparation

1. Make sure `version.py` is set to the right version number.
2. Make sure all commits are in github.
3. CHANGES.md has the change notes for the version.


## Source Release

Some users are okay with installing and running Python.  For those them, they
can just use the source release that github assembles on its own.  That will
provide them all the files necessary to run.

## Bin Release

Other uses would rather not have to go searching for the right Python binary
install and have to get the sources.  For them, we can build a binary release.

In order to create a binary release, you'll need to have access to a 64-bit
version of Windows, and install the full Python distribution (which includes
Pip) for both the 64-bit and 32-bit versions onto your computer.  For the
sake of this document, let's say that they are installed on your computer at
`c:\dev\python-35-32` (32-bit) and `c:\dev\python-35-64` (64-bit).  Let's
also say that you have the Petronia source installed at `c:\dev\petronia`.

In a command prompt, you would run:

```cmd
> c:
> cd \dev\petronia
> buildsrc\build-all.bat c:\dev\python-35-32 c:\dev\python-35-64
```

This will create the `buildsrc\work\petronia-x86.zip` and
`buildsrc\work\petronia-x64.zip` files.  Rename these to include the
version number (like `petronia-3.4-x64.zip`).
