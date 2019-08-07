# Version 3

Petronia Version 3 is a rewrite to attempt to support multiple operating systems.  We'll start with Windows 10 and Linux X-based UI.

This will build on some of the lessons learned from the previous versions.


# Goals

## Focus on Usability

The first versions were "what can we do"?  Now that this is better understood, usage patterns must be the focus for this version.

The major missing functionality in the previous versions were around live-portal manipulation.  This mostly stems from a poor understanding of how to tell the end-user what an action will do.  Because of the recursive portal system, the user would need to be able to select which part of the tree to inject the split.  In most use cases, though, the portal tree won't be too deep.  In extreme cases, the end user could configure the part of the tree that has the split.

## Easy Extending

Based on my research with other shells, it's important to allow the end-users to be able to pull in additional functionality (e.g. download something off the Internet) and use it in their configuration.

This means we need to be able to split things apart into separate files, if desired.

For example, layout trees are easily shared between people, and are independent (fairly) of the rest of the configuration.  These can be split into their own file.  Likewise, key maps to commands can be their own configuration.  It may be helpful to allow directly specifying the command in the key map (one less indirection for people to keep in their head).  Utility functions for those key maps are also helpful to be independently packaged.

## Abstract Away The OS Where Possible

Wherever possible, the interactions between the OS and the user side should be abstracted as much as possible.  Note that this puts restrictions around what can be done by the end user.

## Cross-Platform Configurations

The layout functionality, for portals, chrome, keyboard commands, and "most" command scripts, should be cross-platform.

## Code Safety

The code should be written defensively to protect against mistakes or attacks.

## Flexibility

The system needs to be flexible.  By making component parts interchangeable and replaceable, the core system can grow and change without breaking other components.  End-users can swap out functionality to suit their needs.

# Architecture

## Platform-Specific

All platform specific code is in the [arch](src/petronia3/arch) source directory.  Each supported platform is in the top level directory, and must conform to the spec laid out by the [generic](src/petronia3/arch/generic) tree.

The platform acts as the main program.  It knows how to start up, shut down, and mingle itself into the running OS to do what needs to be done.  The platform calls out to the rest of the Petronia system on operating system events.

# TODO

The current to-do list.

## Really Basic Infrastructure Work

* APIs that do not have implementations (they provide a way things can work, and multiple things can use it) must be allowed, so that any extension that claims to implement it is rejected.
* add capability of the extension loader to force any API loaded to also have exactly one implementation also loaded.
* add proper extension definitions to `petronia_ext` modules.
* localization and internationalization.  This should follow the Python standards as much as possible, but it still needs to be documented and have utilities written.  It's mostly `locale` and `gettext`.
    * An event allows user configuration of the language locale.  This will trigger a singleton listener to run:
      ```python
      locale.setlocale(locale.LC_ALL, loc)
      language = gettext.translation('petronia', languages=[lang])
      language.install()
      ```
    * That same component publishes a state of the available locales and translations.
    * The platform is probably the right source to discover the available translations.  Or it's based on the platform published configuration paths state.
    * Need to figure out how extensions publish translations.  They probably use `(mymodule).__file__` to find its install location, and get the directory from there.
* timer helper should include an implementation that uses the time event.
* basic definition of platform responsibilities.
* Create theme extension API that is a layer on top of the platform.  It provides better components that are themed.  With this, make sure the platform stuff isn't themed and is as low-level as possible.
* Implement secure module.  It should allow different implementations to check the PGP signature.  Implementations can be swapped out whenever, because enforcing a "only once" policy is silly due to the limitations in securing python.  [OpenPGP-Python](https://github.com/singpolyma/OpenPGP-Python) looks promising, but doesn't provide an easy way to access the GPG key store, and depends on several other libraries that most likely require compilation.  [`python-gnupg`](https://pythonhosted.org/python-gnupg/) may be the easiest and safest - it relies upon the `gnupg` program to do everything, it's one file, and is under the BSD-3 clause license.  [openpgp-python](https://github.com/diafygi/openpgp-python) and [python-pgp](https://github.com/mitchellrj/python-pgp) are 100% python, but are under the GPL.  Probably just want to go with [pycrypto](https://github.com/dlitz/pycrypto), as it's under the public domain, but it requires compilation sadface.  To [verify a PKCS#5 v1.5 signature in Python](https://stackoverflow.com/a/19551810/4580538) / PyCrypto, use:
    ```python
    from Crypto.PublicKey import RSA
    from Crypto.Signature import PKCS1_v1_5
    from Crypto.Hash import SHA

    rsa_key = RSA.importKey(open(verification_key_file, "rb").read())
    verifier = PKCS1_v1_5.new(rsa_key)
    h = SHA.new(data_to_verify)
    if verifier.verify(h, signature_received_with_the_data):
        print "OK"
    else:
        print "Invalid"
    ```
    Probably would have two parts - a file-based one (for extensions) and one for in-memory signatures (for events).
* configuration from a file.  Need standards for configuration events (generic format?).  Need INI file reader and writer.  Configuration usage also needs to be standardized.  External storage backed configuration requires a specific configuration object that is generic.  This kind of configuration is more akin to "persistent state", which would allow for saving off session information.
* create the "validation" extension.  It defines state, and allows changes to the state which is hooked up to a listener that will change the global validation state.
* module helpers (`ext_help` for now).  Things like:
    * event listener thread safety.  With event listeners running in any number of threads, developers must take care to make sure their code is thread safe.  Some simple helpers can make life so much easier.
    * event chaining with promise-like API. **Implemented, needs tests.**
    * shutdown handling.  Include shutdown in the listeners.
* Document extension patterns.
* add proper zip support in the extension module loader.
    * add PGP and checksum to zip loader.
* Add the external execution w/ event bus code.
    * The local end that launches the process and marshals state across the wire must keep track of which events are listened to by the process.  This acts for two purposes - one, that only the necessary events are passed across the wire, and two, if the process dies, then the launcher can deregister those event listeners correctly.
