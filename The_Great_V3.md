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

# TODO

The current to-do list.

## Really Basic Infrastructure Work

* Portal redux
    * add in portal component id, along with adding portals to the lifecycle.  Even though the portal
      creation call doesn't make much sense by itself (nothing outside the plugin can explicitly request a creation),
      the portal component ID and destruction do matter.
* Extension security enhancements:
    * API extensions:
        * Cannot listen to events.
        * Can only trigger the "register event" event.
        * Each registered event must be declared with:
            * trigger protection: public (anyone can trigger it) or private (only implementations of the API can trigger it).
            * listen protection: public (anyone can listen to it) or private (only implementations can listen to it)
    * Implementation extensions:
        * Can only listen to listen-public events declared by dependent API extensions.
        * Can listen to public or private events declared by the implemented API.
        * Can only trigger public events declared by dependent API extensions, and private event declared by the API extension it implements.
        * Cannot register any event.
        * Enforce only one implementation of an API loaded at a time.
    * Stand-alone extensions:
        * Can only listen to public events declared by dependent API extensions.
        * Can only trigger public events declared by dependent API extensions.
        * Cannot register any event.
* timer helper should include an implementation that uses the time event.
* Create theme extension API that is a layer on top of the platform.  It provides better components that are themed.  With this, make sure the platform stuff isn't themed and is as low-level as possible.
* create the "validation" extension.  It defines state, and allows changes to the state which is hooked up to a listener that will change the global validation state.
* add proper zip support in the extension module loader.
    * add PGP and checksum to zip loader.
* Document extension patterns.


## Tech Debt

Early development that caused rethinking of how things are done, but that code needs to be revisited to do over again.

* default.extension:
    * loading needs better error handling.
* default.state:
    * use new coding patterns.
* default.configuration.file:
    * needs correct locale usage for messages.
* default.logging.*
    * config file loading needs to be implemented.
* Switch to `ErrorReport` as the standard error reporting mechanism.
* All state providers should also provide a `create_(state)_state_watch(ListenerSet)` function which returns a
    `StateWatch`.  This allows encapsulation of the state ID and typing.
* Make key-down metas have a timeout.  If too much time between keystrokes elapses, then the hotkey combo is canceled.
* Hotkey meta-characters should be passed as still down after hotkey is processed.
* Unit tests everywhere.
* Bugs:
    * file logger category is not loading.


## Later On Features

* Provide a way to run an extension in a sandbox to extract its documentation. 
* Add the external execution w/ event bus code.
    * The local end that launches the process and marshals state across the wire must keep track of which events are listened to by the process.  This acts for two purposes - one, that only the necessary events are passed across the wire, and two, if the process dies, then the launcher can deregister those event listeners correctly.
* Implement secure module.  It should allow different implementations to check the PGP signature.  Implementations can be swapped out whenever, because enforcing a "only once" policy is silly due to the limitations in securing python.  [OpenPGP-Python](https://github.com/singpolyma/OpenPGP-Python) looks promising, but doesn't provide an easy way to access the GPG key store, and depends on several other libraries that most likely require compilation.  [`python-gnupg`](https://pythonhosted.org/python-gnupg/) may be the easiest and safest - it relies upon the `gnupg` program to do everything, it's one file, and is under the BSD-3 clause license.  [openpgp-python](https://github.com/diafygi/openpgp-python) and [python-pgp](https://github.com/mitchellrj/python-pgp) are 100% python, but are under the GPL.  Probably just want to go with [pycrypto](https://github.com/dlitz/pycrypto), as it's under the public domain, but it requires compilation sadface.  To [verify a PKCS#5 v1.5 signature in Python](https://stackoverflow.com/a/19551810/4580538) / PyCrypto, use:
    ```python
    from Crypto.PublicKey import RSA
    from Crypto.Signature import PKCS1_v1_5
    from Crypto.Hash import SHA

    rsa_key = RSA.importKey(open(verification_key_file, "rb").read())
    verifier = PKCS1_v1_5.new(rsa_key)
    h = SHA.new(data_to_verify)
    if verifier.verify(h, signature_received_with_the_data):
        print("OK")
    else:
        print("Invalid")
    ```
    Probably would have two parts - a file-based one (for extensions) and one for in-memory signatures (for events).
* Localization
    * If [Babel](http://babel.pocoo.org/en/latest/) is available, use that first.  Otherwise, use `locale` and `gettext`.
    * Uses the `UserMessage` class.
    * An event allows user configuration of the language locale.  This will trigger a singleton listener to run:
      ```python
      locale.setlocale(locale.LC_ALL, loc)
      language = gettext.translation('petronia', languages=[lang])
      language.install()
      ```
    * That same component publishes a state of the available locales and languages.
    * The platform is probably the right source to discover the available translations.  Or it's based on the platform published configuration paths state.
    * Extensions publish translation files by sending an event with the translation contents.  That allows all sandboxes to receive the new translations.
    * `atoi` and `atof` formatting needs to be supported right.  Configuration files that are exchangeable between users, and that have a well defined format, should have a single expected numeric format.  All end-user input should use the `locale.atoi` and `locale.atof`, which means the above `locale.setlocale` should be used.
        * Needs to be handled at a lower level.
