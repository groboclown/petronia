# Tips and Tricks

## Multiple Work Groups and Application Positions

If you have multiple work groups due to different screen sizes or
configurations, then configuring your applications to start in the right
portal can be tricky.

For setup 1, you want your IDE to appear full screen in the left monitor,
but in setup 2 you want it to be in the center of the only monitor.

The secret sauce here is in listing a priority of matching portal names
for the application position.


## Quick Movement Between Common Portals

A common use case is to have two different windows in two different
portals that you need to quickly switch between.
<kbd>Alt</kbd><kbd>Tab &#x21b9;</kbd> and <kbd>Alt</kbd><kbd>Esc</kbd> can
end up looping through too many intermediate windows to be efficient.

Instead, you can use a combination of the commands
[create-current-portal-alias](user-commands.md#create-current-portal-alias-alias_name)
and [focus-portal-by-alias](user-commands.md#focus-portal-by-alias-alias_name)
with 2 different aliases.

1. Switch to Window A
2. Press the hotkey for `create-current-portal-alias windowA`
3. Switch to Window B
4. Press the hotkey for `create-current-portal-alias windowB`

From that point, you can use the hotkeys setup for
`focus-portal-by-alias windowA` and `focus-portal-by-alias windowB` to swap
between the two portals.

For this, I find the keys
<kbd>&#x2756; Win</kbd><kbd>&#x21e7; Shift</kbd><kbd>1</kbd> to create the
alias, and <kbd>&#x2756; Win</kbd><kbd>1</kbd> to focus on the alias,
to be effective tools.  Note that base Windows provides a similar
functionality, but these are auto-assigned to the Window's position in the
task bar.
