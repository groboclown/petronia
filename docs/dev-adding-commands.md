# Adding New Built-In Commands

## Location

Add the invoker function to `petronia.script.command_helper`.  Make sure
to include good function documentation.

Add the builder for that invoker in `petronia.script.command_builder`.

## Documentation Updates

After creating your new command, regenerate the documentation by running

```
> cd manager\src
> python -m petronia.script.command_builder > ..\..\docs\user-commands.md
```