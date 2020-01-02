# default.logging.file (stand-alone)
**v1.0.0**

File-based logging.

## Details

Runs in elevated privileges

### User Configuration


(no documentation)

```yaml
# Top-level item is some name the user prefers.  Here, we call it "Configuration".
Configuration:
  extension: default.logging.file
  enabled: true
  properties:
    filename: "text"
    format: "text"
    continuation: "text"
    default: "text"
    category-levels:
      # one or more of these types
      -
        category: "text"
        cat: "text"
        level: "text"

```


**Configuration.properties.filename** : File path to write the log to, or '-' to send to stdout.

**Configuration.properties.format** : Log line output format.
        
        The format allows for these symbols:
            * `{LEVEL}`: 5 letters of the log level, in upper-case.
            * `{LONG_LEVEL}`: the full log level name, in upper-case.
            * `{level}`: 5 letters of hte log level, in lower-case. 
            * `{long_level}`: the full log level name, in upper-case.
            * `{src}`: the source of the message.
            * `{msg}`: the logged message.
        
        If date or time is required, use
        https://docs.python.org/3/library/time.html#time.strftime
        for the formatting of the time when the log was recorded.
        

**Configuration.properties.continuation** : Format for when a message continues over several lines.  It follows the same formatting rules as "format"

**Configuration.properties.default** : Default logging level for everything.  If a message does not match a category, then this log level is used.

**Configuration.properties.category-levels[].category** : Name of the category level to log.

**Configuration.properties.category-levels[].cat** : Name of the category level to log.

**Configuration.properties.category-levels[].level** : Lowest log level to allow reporting for this category.







## Dependencies

* [core.state.api](core.state.api.md)
  no version restriction






## Listens To Events

* Event Id **`core.state.api updated`**
  Target Id **`default.logging.file/setup-configuration`**



Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Dec-20.*
