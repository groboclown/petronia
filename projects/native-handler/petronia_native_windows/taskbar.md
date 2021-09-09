# Notes on creating a Custom Taskbar

https://docs.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/notification-listener

https://docs.microsoft.com/en-us/windows/win32/shell/taskbar-extensions#notification-area

https://docs.microsoft.com/en-us/windows/win32/api/shobjidl_core/nn-shobjidl_core-itaskbarlist

https://docs.microsoft.com/en-us/windows/win32/shell/appids


## Taskbar Notification Area Stuff

https://docs.microsoft.com/en-us/windows/win32/shell/notification-area

* Shell hooks that need to be registered: https://docs.microsoft.com/en-us/windows/win32/shell/notification-area#add-a-notification-icon
* Hook to listen for notify icon events: https://docs.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shell_notifyiconw 
* Sending mouse events for notification area icons: https://docs.microsoft.com/en-us/windows/win32/shell/taskbar#receiving-mouse-events
* API for telling applications where the icon is: https://docs.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shell_notifyicongetrect

## Application Desktop Toolbar

https://docs.microsoft.com/en-us/windows/win32/shell/application-desktop-toolbars

* Adding a new app bar: https://docs.microsoft.com/en-us/windows/win32/shell/abm-new

## General Shell Stuff

https://docs.microsoft.com/en-us/windows/win32/shell/messages
