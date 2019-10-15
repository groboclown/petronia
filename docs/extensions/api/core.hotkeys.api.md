# API Extension core.hotkeys.api v1.0.0

Standard API for registering hotkeys that perform generate events.

The API acts as a broker between applications that use hotkeys, and the low- level platform hotkey registration.


Depends On Extensions:
* [core.platform.api](core.platform.api.md)
  no version restriction
* [core.state.api](core.state.api.md)
  no version restriction



Default Implementations:
* [defimpl.hotkeys](defimpl.hotkeys.md)
  no version restriction



## Declared Events


### Event `core.hotkeys.api/trigger`

* Event Id: **`core.hotkeys.api/trigger`**
* Event Class: **petronia.core.hotkeys.api.events.HotkeyEventTriggeredEvent**
* Queue Priority: **normal**

Notification that a hotkey event activated.

### Event `core.hotkeys.api/register`

* Event Id: **`core.hotkeys.api/register`**
* Event Class: **petronia.core.hotkeys.api.events.RegisterHotkeyEventEvent**
* Queue Priority: **normal**

Register a hotkey to trigger an event.  The hotkey itself does not include the master sequence.  The event will be targeted to the service that registered the schema bound to the action type.

### Event `core.hotkeys.api/remove`

* Event Id: **`core.hotkeys.api/remove`**
* Event Class: **petronia.core.hotkeys.api.events.RemoveHotkeyEventEvent**
* Queue Priority: **normal**

Remove a registered hotkey.

### Event `core.hotkeys.api/master`

* Event Id: **`core.hotkeys.api/master`**
* Event Class: **petronia.core.hotkeys.api.events.SetMasterHotkeySequenceEvent**
* Queue Priority: **normal**

Set the master hotkey sequence.  This may be rejected by the underlying platform.

### Event `core.hotkeys.api/announce`

* Event Id: **`core.hotkeys.api/announce`**
* Event Class: **petronia.core.hotkeys.api.events.HotkeyBoundServiceAnnouncementEvent**
* Queue Priority: **normal**

Notification that a service can be bound to a hotkey, and a description of the expected values in the binding.

### Event `core.hotkeys.api/revoke-announce`

* Event Id: **`core.hotkeys.api/revoke-announce`**
* Event Class: **petronia.core.hotkeys.api.events.HotkeyUnbindServiceAnnouncementEvent**
* Queue Priority: **normal**

Notification that a service can be bound to a hotkey, and a description of the expected values in the binding.




