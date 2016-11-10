# So Frustrating!  Why Is This Happening?


### There's A Stupid Blue Box Around Stuff.  And Now I'm Hearing Voices.

You've activated the annoying Narrator program.  You *might* be able to close
it normally.  <kbd>&#x21ea; Caps Lock</kbd><kbd>Esc</kbd> is supposed to turn
it off once it starts running.  To keep it from running, you can use several
tricks to keep it from running.  The Internet has some "friendly" advice.

But then, you know, Internet.


### The Win Key Gets Stuck

If you block the Windows key from being processed, the <kbd>&#x2756; Win</kbd>
key can get stuck.  This is particularly troublesome with the lock desktop
key sequence <kbd>&#x2756; Win</kbd><kbd>L</kbd> and the ease of access center
key sequence <kbd>&#x2756; Win</kbd><kbd>U</kbd>.  For these two, Windows
intercepts the key sequence before anything else can run.

If you do get in a position where it's stuck, here's a few things to try:

* Tapping the <kbd>&#x2756; Win</kbd> can unstick it.
* If you have the [open-start-menu](user-commands.md#open-start-menu)
    action, I've noticed that sometimes, if it's open and active when
    you hibernate your computer, it can cause the windows key to get stuck.
    Try closing the start menu and see if that helps.  If that isn't enough,
    use the `open-start-menu` command several times.
* If the key is still really stuck, you can open the Windows on-screen
    keyboard app, and click on the <kbd>&#x2756; Win</kbd> key.  This seems
    to get it unstuck.  You may need to play around with it.


### A Window Won't Move To Another Monitor

Sometimes, one window can move freely between monitors, while others seem to
get stuck in a single one.

A good way to get past this is to include
[hotkeys](user-configuration.md#hotkey-configuration) for the
[move-window-to-other-portal](user-commands.md#move-window-to-other-portal-direction)
command with arguments `next` and `previous`.  This bypasses the layout's idea
of what directions mean, and instead just moves through each portal.
