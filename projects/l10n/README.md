# About

Contains the message catalog source files and translations that originated from the source code.


## Code

Text that should be localizable (meaning displayed for normal user consumption) must follow these guidelines.

Include an import statement like:

```python
from petronia_common.util import i18n as _
```

The translation tool looks for the function call `_('some string')` to extract into the message catalog.  The string argument to the `_` function is the message key, and is used to look up the translation in the localized message catalog.

Arguments to the translatable string are put in curly braces, just like the Python "f-string" and string formatter.  Take care to *not* make the `_` string argument an f-string (e.g. `_(f'error in {filename}')`); doing so makes the string argument dynamic, which breaks the localized message catalog key, and will also probably break the message extraction program.

A fully defined, localizable message is contained in a `UserMessage`, which includes the translation catalog, the message key (the string in the `_` call), and the key/value arguments for the message.

If you need to use a `UserMessage` but not put the translation string in the message catalog, then use the original `i18n` function.  This is useful if you need to use one of these messages for unit tests.


## Code -> Catalog

Messages originate by first declaring an import of the `i18n` function as the name `_`, and the use of `_('some text')` marks that text as a translatable message.

The command [extract-message-catalog.sh](../../bin/extract-message-catalog.sh) scans the source files and extracts the messages into the tree.  These, then, will need manual translation.

The source code messages are expected to be all in US English.  With this expectation, the extraction automatically creates the English and US English locales.


## File Layout

The expected layout of this project is:

* `templates/(project-name).pot` - the template message file, extracted from the project's source by the `extract-message-catalog.sh` script.  These files are generated and should not be manually changed.
* `translations/(locale)/LC_MESSAGES/(project-name).po` - locale-specific manual translation of the project's messages.  Tools such as [poedit](https://poedit.net/) can help with this.
* `compiled/(locale)/LC_MESSAGES/(project-name).po`

The build script compiles these `.pot` files into the appropriate machine object in the correct directory layout.


## Translator Comments

*(Taken from [Babel Docs](http://babel.pocoo.org/en/latest/messages.html), but updated for how Petronia uses it.)*

First of all what are comments tags. Comments tags are excerpts of text to search for in comments, only comments, right before the python gettext calls, as shown on the following example:

```python
# I18N: This is a comment about "Foo Bar"
_('Foo Bar')
```

The comments tag for the above example would be `I18N:`, and the translator comment for that tag would be `This is a comment about "Foo Bar"`.

The resulting output in the catalog template would be something like:

```
#. This is a comment about `Foo Bar`
#: main.py:2
msgid "Foo Bar"
msgstr ""
```


## Events

Localizable messages (the message key + message arguments) can be passed between extensions through events and states by a [standard convention](../../docs/event_standard_data_types.md#localizable-message).

The `petronia_ext_lib.standard.localizable_message` module provides helper functions for transforming a `UserMessage` object into an event localizable message structure.  Due to the independence of the extensions, each extension's message structure is a different class, so the event object construction must be handled separately.

```python
from petronia_common.util import UserMessage
from petronia_ext_lib.standard import localizable_message
from petronia_ext_lib.events import logging as logging_event


def create_logging_message(
        message: UserMessage,
) -> logging_event.LocalizableMessage:
    """Creates a localized logging message"""
    return localizable_message.create_localizable_message(
        logging_event.LocalizableMessage,
        logging_event.MessageArgument,
        logging_event.MessageArgumentValue,
        message,
    )
```

As long as the event uses the standard definition for messages, this easy invocation will work.
