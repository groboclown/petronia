"""Type definitions for the cairo library."""

import ctypes


class CairoSurface(ctypes.Structure):
    """The opaque Cairo cairo_surface_t type"""
    _fields_ = []


CairoSurfaceP = ctypes.POINTER(CairoSurface)


CairoStatus = ctypes.c_int
