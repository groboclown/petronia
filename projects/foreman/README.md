# Notes about Foreman

Foreman is a very special project for Petronia.  It's the entry-program for starting up Petronia, and keeps it going.


## For Developers

As Foreman is critical to keeping the primary security, safety, and reliability of Petronia, it must be carefully updated.

* Where possible, it should minimize platform knowledge.
* It is the root of all events and runs outside of extensions.  It can have no explicit knowledge of other extensions except the extension loader. 
    * Because of this, Foreman must be extremely careful about using the `py-extension-lib` project.  Logging, timer, data store, and other normally "just there" extensions can't be assumed to be running, and these events cannot be used.
