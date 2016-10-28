# User Guide: Getting Started with Petronia

Petronia is in an early stage of development, and thus is filled with all
kinds of warts and broken bones.  However, it still provides a magic that
allows for a streamlined Windows experience.


## Find the Stuff

First thing, you need to get the stuff that allows you to run Petronia.

1. Make sure you're running Windows.  Petronia is for Windows.
2. Download the [python.org](https://python.org) Python v3.5 distribution
    appropriate for your computer (64-bit or 32-bit).
3. Download the Petronia source.  Yeah, we're cookin' with gas here.
    Get it from gitub.  Clone the repo, or just download it.
    *TODO better instructions.*


## Install the Stuff

Put all the program things in the program places.


## Run the Stuff

Start up a command prompt.  If you don't know what this is, then you're
probably going to get in over your head later.

From a command prompt, add the installed Python 3.5 to your path (if it's not
already there), and run the main program from the `manager/src` directory.
 
```(cmd)
> set Path=(python directory);%Path%
> cd (petronia directory)\manager\src
> python -u -m petronia.main user_test_config.py
```

The `user_test_config.py` argument tells Petronia where to find your
configuration file.

Press <kbd>Enter</kbd> in the command prompt to stop it.


## What Just Happened?

If everything went well, Petronia tried to find the best match of your
computer's monitor resolution to what's in the configuration.  It then
shoved all your precious program windows into the first region.  It probably
also stripped off the borders and title bars, as well.  If things didn't
go well, then you're stuck staring at a Python stack trace.  *So it goes.
Those who are Great open bugs.  Those who are Strong fix it.   The Best do
both.*

You'll also notice that your trusty <kbd>win</kbd> key now doesn't work how
you're used to.  Instead, it gives you some control over your window layout. 

 * <kbd>&#x2756; Win</kbd><kbd>up arrow</kbd> Move the currently active window to
    the [portal](#Portal) *north* of where it's at now.
 * <kbd>&#x2756; Win</kbd><kbd>down arrow</kbd> Move the currently active window to
    the [portal](#Portal) *south* of where it's at now.
 * <kbd>&#x2756; Win</kbd><kbd>left arrow</kbd> Move the currently active window to
    the [portal](#Portal) *west* of where it's at now.
 * <kbd>&#x2756; Win</kbd><kbd>right arrow</kbd> Move the currently active window to
    the [portal](#Portal) *east* of where it's at now.
 * <kbd>&#x2756; Win</kbd><kbd>page up</kbd> Move the currently active window to
    the *next* [portal](#Portal).
 * <kbd>&#x2756; Win</kbd><kbd>page down</kbd> Move the currently active window to
    the *previous* [portal](#Portal).
 * <kbd>&#x2756; Win</kbd><kbd>Tab</kbd> Minimize the currently active window. 
 * <kbd>&#x2756; Win</kbd><kbd>Launch App 1</kbd> Start a command prompt window.
    This is usually the extra media button that looks like a computer.
 * <kbd>&#x2756; Win</kbd><kbd>Esc</kbd> Open up the Windows start menu.  Since the
    Windows key has been preempted, this explicit remapping of the
    functionality becomes necessary.
 * <kbd>&#x2756; Win</kbd><kbd>~</kbd> Switch over to Windows Classic mode.
 * <kbd>&#x2756; Win</kbd><kbd>F11</kbd> This is supposed to quit Petronia, but, you
    know, Alpha software and all that.  Yeah, it don't work too well.

If you press <kbd>&#x2756; Win</kbd><kbd>~</kbd>, the keyboard shortcuts will
switch over to the Windows Classic mode.  Here, you can use the Windows keys
as Microsoft wants you to.  This means that the only special key sequence that
Petronia recognizes now is another <kbd>&#x2756; Win</kbd><kbd>~</kbd> to put it back
into the default mode.


## Where To Go From Here

At this point, I bet you just can't wait to dive into the configuration to
get your computer working how you want.

[Go for it.](user-configuration.md)  Start writing your own configuration
now.

You'll have to shut down Petronia and restart it with the new configuration,
and restart it for each update.
