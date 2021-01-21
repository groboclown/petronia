# About

Contains the message catalog source files and translations that originated from the source code.


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

*(Taken from [Babel Docs](http://babel.pocoo.org/en/latest/messages.html))*

First of all what are comments tags. Comments tags are excerpts of text to search for in comments, only comments, right before the python gettext calls, as shown on the following example:

```python
# NOTE: This is a comment about "Foo Bar"
_('Foo Bar')
```

The comments tag for the above example would be `NOTE:`, and the translator comment for that tag would be `This is a comment about "Foo Bar"`.

The resulting output in the catalog template would be something like:

```
#. This is a comment about `Foo Bar`
#: main.py:2
msgid "Foo Bar"
msgstr ""
```
