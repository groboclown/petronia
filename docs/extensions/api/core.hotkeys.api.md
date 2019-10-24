# core.hotkeys.api (API)
**v1.0.0**

Standard API for registering hotkeys that perform generate events.


The API acts as a broker between applications that use hotkeys, and the low-
level platform hotkey registration.


The registration will associate a basic key combination to a target ID and
a basic data structure.  The event ID is fixed.

## Details


### Declared Events


### Event `core.hotkeys.api/trigger`

* Event Id: **`core.hotkeys.api/trigger`**
* Event Class: **`petronia.core.hotkeys.api.events.HotkeyEventTriggeredEvent`**
* Queue Priority: **normal**
* Only instance triggering permitted
* Public listening allowed

Notification that a hotkey event activated.

### Event `core.hotkeys.api/register`

* Event Id: **`core.hotkeys.api/register`**
* Event Class: **`petronia.core.hotkeys.api.events.RegisterHotkeyEventEvent`**
* Queue Priority: **normal**
* Public triggering allowed
* Only instance listening permitted

registered the schema bound to the action type.

### Event `core.hotkeys.api/remove`

* Event Id: **`core.hotkeys.api/remove`**
* Event Class: **`petronia.core.hotkeys.api.events.RemoveHotkeyEventEvent`**
* Queue Priority: **normal**
* Public triggering allowed
* Only instance listening permitted

Remove a registered hotkey.

### Event `core.hotkeys.api/master`

* Event Id: **`core.hotkeys.api/master`**
* Event Class: **`petronia.core.hotkeys.api.events.SetMasterHotkeySequenceEvent`**
* Queue Priority: **normal**
* Public triggering allowed
* Only instance listening permitted

Set the master hotkey sequence.  This may be rejected by the underlying platform.

### Event `core.hotkeys.api/announce`

* Event Id: **`core.hotkeys.api/announce`**
* Event Class: **`petronia.core.hotkeys.api.events.HotkeyBoundServiceAnnouncementEvent`**
* Queue Priority: **normal**
* Only instance triggering permitted
* Public listening allowed

of the expected values in the binding.

### Event `core.hotkeys.api/revoke-announce`

* Event Id: **`core.hotkeys.api/revoke-announce`**
* Event Class: **`petronia.core.hotkeys.api.events.HotkeyUnbindServiceAnnouncementEvent`**
* Queue Priority: **normal**
* Only instance triggering permitted
* Public listening allowed

of the expected values in the binding.








## Dependencies

* [core.platform.api](core.platform.api.md)
  no version restriction
* [core.state.api](core.state.api.md)
  no version restriction



### Default Implementations:
* [default.hotkeys](default.hotkeys.md)
  no version restriction


## Source

Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Oct-24.*
