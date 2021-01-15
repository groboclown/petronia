# Petronia Events

Events, being the heart of Petronia, require specific details about how they work.

Events are defined within the extension definition of an API.  The schema is fully defined in the [extension-schema.yaml](extension-schema.yaml), and described below.  The extension tool [`gen_marshal`](../projects/extension-tools/petronia_extension_tools/gen_marshal/__init__.py) can generate the code to contain event data and encode/decode it.  The generation of the output files will need to be done per project that needs it (it is not done in a shared place).  The script [`bin/generate-events.sh`](../bin/generate-events.sh) makes running it easier.

## Guidelines

Any activity that requires one participant of the system to interact with another requires the communication to be done through events.

The nature of events requires them to only exist when they have a specific participant identity that is the target of the event.  In most cases, this corresponds to the intended receiver of the event.  In a few cases, it indicates a participant that had an action act upon it, but may not receive the event.


## Event Id, Source, Target

Each event has a unique ID that is a combination of the declaring API extension name and a "short" name.  This takes the form `ExtensionName:ShortName`.

Each generated event provides a Source and Target ID.  These identifiers take the form of `ExtensionName:InternalId`, where the extension is free to choose the internal ID.  Because Petronia loads one of each extension name at a time, security in asserting the validity of the source and target is better enforced.  It also means there doesn't need to be a central name registration service.


## Simulating RPC With Events

In general, events should be considered "fire and forget."  On a rare occasion, an event requires a response, such as registering a portal and receiving the portal ID or an error response if something didn't go right.

In these cases, the general mechanism is to have the initiating event have the form "(RequestName):Request", and the result usually have two events, "(RequestName):Failed" and "(RequestName):Success".

## Schema

When an event is registered, it must provide the schema for the events.  These are based upon the standard JSON schema, but highly simplified.  These are embedded in the API extension metadata.  The event name provided is the "simple name"; internally, the fully qualified name will be used instead, which is in the form "ExtensionName:EventName".

The event declaration of the API extension looks like this:

```javascript
{
    "events": {
        // TODO document event name format.
        "one-event-name": {
            // The priority in which the event is handled.
            // Valid values are "high", "user", "normal", and "io".
            "priority": "normal",

            // Describes which extensions have permissions to send
            // this event.
            // Valid values are "public" and "implementations".  Some
            // core, internal extensions can use the "internal" access level.
            "send-access": "public",

            // Describes which extensions have permissions to receive
            // this event.
            // Valid values are "public", "implementations", and "target".
            "receive-access": "public",

            // An optional description of the event.  It can be 0 to 32767 characters long.
            "description": "",

            // A list of fields allowed in the event.  This takes the form of the
            // "fields" in a formal structure (see below).
            "fields": {}
        },
        "another-event-name": {
            // ...
        },
        "a-binary-event": {
            // binary events are very special types.  They allow for transmitting
            // binary blobs of data without needing special escaping.  However, for
            // binary events, the entire event is a binary blob, and it does not
            // have fields.  This should be used for actions like sending audio to
            // play or images.
            "priority": "normal",
            "description": "blah",
            "binary": true
        }
    },
    "references": {
        "AStructureDefinition": {
            // A data definition.  See below for details.
        },
        "AnotherStructure": {}
    }
}
```

Each data definition in the `references` section must be of a specific type.  The supported types are:


### string

```javascript
{
    "references": {
        "a_string_type": {
            "type": "string",

            // Every reference type can have a description.  Descriptions
            // are 0 to 32767 character long strings.
            "description": "blah",

            // Strings have a limited number of restrictions that can
            // be defined for them.
            
            // A maximum length value.
            // The default value is 255.  The absolute maximum value is 65535.
            // The minimum value is 1.
            "max-length": 10,

            // A minimum length.  This must be less than or equal to the maximum length.
            // The default value is 0.  The absolute maximum is the value of the
            // "max-length" value.
            "min-length": 1
        }
    }
}
```

### integer


```javascript
{
    "references": {
        "an_integer_type": {
            "type": "int",

            // Maximum value is 9223372036854775807, minimum value is -9223372036854775808.
            // Default is 9223372036854775807
            "max-value": 1000,

            // Minimum integer value.  Minimum value is -9223372036854775808,
            // maximum value is "max-value" value.
            // Default is -9223372036854775808
            "min-value": 0,
        }
    }
}
```


### float

```javascript
{
    "references": {
        "a_float_type": {
            "type": "float",
            "max-value": 100.1,
            "min-value": 10.0
        }
    }
}
```


### boolean

```javascript
{
    "references": {
        "a_boolean_type": {
            "type": "bool",
        }
    }
}
```


### enum

```javascript
{
    "references": {
        "an_enum_type": {
            "type": "enum",

            // Value must be a string with a length must be between 1 and 255.
            "values": [
                "value-1",
                "value-2",
                "some other value"
            ]
        }
    }
}
```


### date-time

```javascript
{
    "references": {
        "a_date_time_type": {
            "type": "datetime",

            // Values will be transmitted as strings in the format:
            // YYYYMMDD:hhmmss.sss:Z
            // YYYY: 4-digit year.
            // MM: 2-digit month (Jan = 01, Dec = 12)
            // DD: 2-digit day of the month (01 to 31)
            // hh: 2-digit hour (24-hour time)
            // mm: 2-digit minute of the hour (0-59)
            // ss: 2-digit second of the minute (0-61, for leap-seconds)
            // "." + sss: 1-6 fractional second time digits, which are optional
            // Z: timezone offset:
            //    4 digits for hours / minutes (-1259 to 1259)
            //    Optionally, can also include seconds (2-digits) and
            //    fractions of a second ("." + 1-6 digits).
        }
    }
}
```


### array

```javascript
{
    "references": {
        "an_array": {
            // An array is a uniform type definition; every entry in the
            // array has the same type.
            "type": "array",
            "value-type": {
                // A definition of a value type.  This is a recursive
                // data structure.
            },
            "min-length": 0,
            "max-length": 65535
        }
    }
}
```


### structure

```javascript
{
    "references": {
        "a_structure": {
            "type": "structure",

            "fields": {
                // Keys are the field names, which must be characters matching the regular expression:
                //   [a-z][a-z0-9_]*
                // The minimum length is 1, the maximum length is 255 characters.
                "a_field": {
                    // A field has the same form as a reference entry, but with
                    // one additional value: "optional".
                    // By default, all fields are required ("optional": false).
                    // If optional = true, then the field does not need to be present,
                    // or the value can be null.  Not-present fields have a null value.
                    "optional": false
                }
            }
        }
    }
}
```


### selector


```javascript
{
    "references": {
        "a_selector": {
            "type": "selector",

            // This is a special structure that allows containing a dynamically typed value.
            // However, the exact contents must be well defined, and not defined later.
            // The data form of a "selector" structure is:
            // { "^": "selector-name", "$": /* structure data */ }

            "type-mapping": {
                "key1": {
                    // A type definition.
                    // ...
                },
                "key2": {
                    // ...
                }
            }
        }
    }
}
```


### reference

```javascript
{
    "references": {
        "an_array_of_references": {
            "type": "array",
            "value-type": {
                // A reference can be anywhere, and can define a recursive data
                // structure.  However, they have the best use as a sub-type
                // within another type.

                "type": "reference",
                "ref:" "a_selector"
            }
        }
    }
}
```


### State Data Definitions

A common pattern for extensions has them store public data in the data-store extension.  This is so common that the extension metadata schema includes a top-level `state-data` section with definitions for the stored data.  The content of this section is a dictionary with the short name of the stored data as the key, and the value is a Structure, following the same pattern as the event Structure type.

This section is entirely optional, and is used to help users of the exension to better understand how its used, and also helps with code generation for parsing and formatting the state data.

This can also be used for defining configuration data, though that will be for documentation for the user instead of inter-extension helpers.

## Streaming Events

Event objects are sent one after the other.  The event stream must follow this specification.  The specification for the stream proper is in octets.

```
STREAM = (anything) (PACKET_SEPARATOR) (EVENT_PACKET)
PACKET_SEPARATOR = 0x00 0x00 0x91
EVENT_PACKET = (EVENT_ID_STRING) (SOURCE_ID_STRING) (TARGET_ID_STRING) (DATA_CONTENTS)
EVENT_ID_STRING = 0x65 (STRING) ; 'e'
SOURCE_ID_STRING = 0x73 (STRING) ; 's'
TARGET_ID_STRING = 0x74 (STRING) ; 't'
DATA_CONTENTS = (JSON_CONTENTS) or (BINARY_CONTENTS)
JSON_CONTENTS = 0x7b (STRING) ; '{'
BINARY_CONTENTS = 0x5b (BLOB) ; '['
STRING = (size octet 1) (size octet 2) (size number of octets)
BLOB = (size octect 1) (size octet 2) (size octet 3) (size number of octets)
```

The size value is a 16- or 24-bit big-endian integer, so the ordered octets "0xfe 0x94" would be 0xfe94, and the ordered octets "0xa0 0xfe 0x94" would be 0xa0fe94.

All string contents are encoded UTF-8 binary values.  The size value is the number of octets in the encoded binary format.

The event ID and target ID MUST have a length > 0 and < 2048 bytes (encoded UTF-8).  The JSON contents must have a length > 2 and < 65536 bytes (encoded UTF-8).  The binary blob can be zero length, but cannot exceed 10485760 bytes (10 mb).

Note that the source ID isn't required by the event objects themselves, but the brokers use this to validate the security privileges of the requestor.
 