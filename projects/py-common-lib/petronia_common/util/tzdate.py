"""Helper utilities for dealing with datetime, forcing the timezone."""

import datetime


def tznow() -> datetime.datetime:
    """Create the current datetime, making sure the correct timezone information is
    included."""
    return datetime.datetime.now(datetime.timezone.utc)
