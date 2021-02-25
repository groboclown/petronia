# Important Notes

These are important notes to keep in mind when working with the Windows version of the native handler.

## Petronia Monitor / Screen Mapping and Windows

Windows OS can report the information on individual monitors, but the reporting for GUI windows is in terms of the virtual screen space.  Petronia, on the other hand, uses its own virtual screen space.  This means that Windows has an extra layer of indirection - Petronia virtual screen -> Windows virtual desktop -> monitor.

This is intended to be handled with the `windows_vd.py` module.


## Important General Guidelines With Windows Messages

Applications should send WM_SETTINGCHANGE to all top-level windows when they make changes to system parameters. (This message cannot be sent directly to a window.) To send the WM_SETTINGCHANGE message to all top-level windows, use the SendMessageTimeout function with the hwnd parameter set to HWND_BROADCAST.


## Making System Changes

*From [The Display-Aware Application](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ms695534(v=vs.85))*

Before performing actions that might interrupt a presentation in progress, check WM_SETTINGCHANGE to see if the user is working with presentation settings turned on.

People don't want disruptions when they're using their mobile PCs to give a presentation. Before displaying notifications, applications should check WM_SETTINGCHANGE to determine whether the user turned on presentation settings. This way, you avoid causing embarrassment and frustration for the user.

Users can turn on presentation settings in Windows Vista when they connect their mobile PC to a network projector, connect to an additional display, or use Windows Mobility Center. Turning on presentation settings changes several options to prevent disruptions; for example, the screen saver is turned off, the display remains on, the desktop background can be changed, and volume can be muted. Notifications are delayed until presentation settings are turned off.

You can call the SHQueryUserNotificationState function immediately before displaying any notification to determine whether the user has cancelled notifications by entering presentation mode.


## System Wake-Up Changes

*From [System Wake-up Events](https://docs.microsoft.com/en-us/windows/win32/power/system-wake-up-events)*

If the system wakes due to user activity, the system will first broadcast the PBT_APMRESUMEAUTOMATIC event followed by a PBT_APMRESUMESUSPEND event. In addition, the system will turn on the display. Your application should reopen files that it closed when the system entered sleep and prepare for user input.

A window receives the PBT_APMRESUMEAUTOMATIC event through the [WM_POWERBROADCAST](https://docs.microsoft.com/en-us/windows/win32/power/wm-powerbroadcast) message.
