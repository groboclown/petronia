# Components for Your Configuration

In order to allow Petronia to be extensible by end-users, the configurations
allow for defining components that add to the default functionality.


## Built-In Components

Petronia comes with some components that you can enable to add some extra
flair to Windows.

### `portal_chrome`

```yaml
  singletons:
    # In order to indicate which portal is focused, we add a bit of chrome to the
    # bottom of each portal that has a color when active.
    - factory: petronia.components.portal_chrome
      settings:
        position: bottom
        width: 12
        active-color: '#0070f0'
        inactive-color: '#404060'
```

Adds some color at the bottom of each portal.  It allows for showing which portal
is active, even if there aren't windows in that portal, or if the windows don't
have a border.



## Making Your Own Components

*Currently not covered here.  Maybe eventually this will be documented.*

Essentially, you want to create a Python module, have it be in the Python
path, and define the method `get_factory(settings)`.  It should return
a factory method.

Eventually, the configuration should allow for defining an extensions directory
where these files can be added.
