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

There's a solution in the code, which doesn't block the windows key *release*.
This seems to do the trick.  If you do get in a position where it's stuck,
I found that you can open the on-screen keyboard app, and click on the
<kbd>&#x2756; Win</kbd> key.  This seems to get it unstuck.  You may need to
play around with it.


### A Window Won't Move To Another Monitor

Sometimes, one window can move freely between monitors, while others seem to
get stuck in a single one.

This is more of a bug that needs to be fixed.  It's probably an issue
somewhere in the root_layout.  My guess is once the root layout better
understands monitor geometry (how one monitor is positioned relative to
others), this will even itself out.
