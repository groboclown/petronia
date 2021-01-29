# Standard Event Data Types

The event data objects allow for very flexible but strict data typing.  However, at the time of this writing, the types are not shareable between extension metadata files.  This document describes those common data types, written to allow for easy pasting into the `references` section of the metadata file.


## Unique Identifier

Request / response event chains sometimes require a unique identifier to help with constructing a matching response.

```yaml
references:
  response-identifier:
    description: >
      An identifier, created by the sender, that is included in the response so the sender matches the
      response to the sent message.  Combined with the sender's ID (for requests) or target's ID
      (for responses) creates a unique identifier.
    type: int
    min-value: -999999
    max-value: 9999999
```


## Localizable Message

Text messages may need to be passed to the user to for various informative usages, and these must be localizable.

```yaml
references:
  localizable-message:
    description: A localizable message for user display.
    type: structure
    fields:
      catalog:
        description: >
          The name of the translation file, or "domain", that contains
          the translations.
        type: string
        min-length: 2
        max-length: 300
      message:
        description: >
          The message ID to look up in the catalog.  If the message
          has no translation, this is directly displayed to the user.
        type: string
        min-length: 1
        max-length: 10000
      arguments:
        description: >
          List of arguments to be inserted into the translated message.
          Each argument should have a distinct name from all the other
          arguments in this message; the name is how the message references
          the arguments.
        type: array
        min-length: 0
        max-length: 100
        optional: true
        value-type:
          type: reference
          ref: message-argument
  message-argument:
    description: An argument to be inserted into the localizable message.
    type: structure
    fields:
      name:
        description: Name of the arugment, referenced by the message.
        type: string
        min-length: 1
        max-length: 50
      value:
        description: Value of the argument.  It must be a simple type.
        type: reference
        ref: message-argument-value
  message-argument-value:
    description: A replacement value for a named argument in the message.
    type: selector
    type-mapping:
      string:
        type: string
        min-length: 0
        max-length: 10000
      int:
        type: int
      float:
        type: float
      bool:
        type: bool
      datetime:
        type: datetime
      string_list:
        type: array
        min-length: 0
        max-length: 100
        value-type:
          type: string
          min-length: 0
          max-length: 10000
      int_list:
        type: array
        min-length: 0
        max-length: 100
        value-type:
          type: int
      float_list:
        type: array
        min-length: 0
        max-length: 100
        value-type:
          type: float
      bool_list:
        type: array
        min-length: 0
        max-length: 100
        value-type:
          type: bool
      datetime_list:
        type: array
        min-length: 0
        max-length: 100
        value-type:
          type: datetime
  ```


## Errors

Request / Response style event chaining usually entails having the response either be a success or error response.  Logging and other extensions can have additional uses for the error message.

```yaml
references:
  error:
    type: structure
    description: A description of a failure.
    fields:
      identifier:
        description: >
          The identifier that uniquely defines this error.  Useful for
          automation that needs to perform operations based on specific
          error messages.
        type: string
        min-length: 5
        max-length: 600
      categories:
        description: >
          A collection of general categories that define the error.
          Useful for automation that can act differently depending on
          the contents.
        type: array
        min-length: 1
        max-length: 100
        value-type:
          description: General error category.
          type: enum
          values:
            - file
            - os
            - configuration
            - network
            - access-restriction
            - invalid-user-action
            - internal
      source:
        description: The source of the error, if known.
        type: string
        min-length: 2
        max-length: 300
        optional: true
      corrective_action:
        description: >
          If given, informs the user approaches for fixing the issue.
        type: reference
        optional: true
        ref: localizable-message
      error_message:
        description: The localizable error message.
        type: reference
        ref: localizable-message
```


## Extension Information

For many of the core projects, information about extensions is required to be passed in events.

```yaml
references:
  extension-name:
    description: Standard name requirements for an extension.
    type: string
    min-length: 3
    max-length: 200
  extension-version:
    description: Version number for an extension.  It must be a three part number.
    type: array
    min-length: 3
    max-length: 3
    value-type:
      type: int
      min-value: 0
      max-value: 999999
  
```


## Event Information

Some extensions require use of standard event metadata values included in the event data body.  Event IDs and target IDs use the base extension name as the prefix, so the minimum and maximum lengths incorporate that information.

```yaml
references:
  event-id:
    description: ID of an event.
    type: string
    min-length: 5
    max-length: 600
  event-target-id:
    description: ID of an event listener.
    type: string
    min-length: 5
    max-length: 600
```


## JSON Data

Some extensions require a parameter to contain JSON-like data.  The event structure does not allow for arbitrarily formatted data, so this must be encoded in an additional way.  Where possible, this should be avoided in favor of precisely declared data types.

```yaml
references:
  embedded-json-data:
    description: Arbitrary JSON data embedded inside the event structure.
    type: string
    min-length: 2
    max-length: 60000
```
