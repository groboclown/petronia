
"""
Constants defined by Windows.
"""

from typing import Dict
# from typing import cast as t_cast
from ctypes.wintypes import (
    HANDLE, HWND,
)

# Well, this isn't, but it's global for Petronia <-> Windows interaction.
PETRONIA_CREATED_WINDOW__CLASS_PREFIX = "Petronia__"


GW_OWNER = 4  # c_int
GWL_EXSTYLE = -20  # c_int
GWL_STYLE = -16  # c_int

MAX_PATH = 260  # c_int
MAX_CLASS_NAME_LENGTH = 4096  # c_int, just an arbitrarily big buffer
MAX_FILENAME_LENGTH = 4096  # c_int, just an arbitrarily big buffer

PROCESS_QUERY_INFORMATION = 0x400  # c_int
PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
PROCESS_ALL_ACCESS = (0xF0000 | 0x100000 | 0xFFF)  # c_long
READ_CONTROL = 0x20000
PROCESS_VM_READ = 0x10  # c_int
STILL_ACTIVE = 259  # c_int
PROCESS_NAME_NATIVE = 1  # c_int
MAX_PROCESS_COUNT = 4096  # just something big

MONITORINFOF_PRIMARY = 1  # c_int

HWND_MESSAGE = HWND(-3)
HWND_BOTTOM = HWND(1)
HWND_NOTOPMOST = HWND(-2)
HWND_TOP = HWND(0)
HWND_TOPMOST = HWND(-1)
HWND_DESKTOP = HWND(0)
INVALID_HANDLE_VALUE = HANDLE(-1)

HWND_ZORDER_MAP = {
    "message": HWND_MESSAGE,
    "bottom": HWND_BOTTOM,
    "no-topmost": HWND_NOTOPMOST,
    "top": HWND_TOP,
    "topmost": HWND_TOPMOST,
}


# https://msdn.microsoft.com/en-us/library/windows/desktop/ms682489(v=vs.85).aspx
TH32CS_SNAPTHREAD = 0x00000004

BM_CLICK = 245  # c_int

SW_HIDE = 0  # c_int
SW_SHOWNORMAL = 1  # c_int
SW_SHOWMINIMIZED = 2  # c_int
SW_MAXIMIZE = 3  # c_int
SW_SHOWMAXIMIZED = 3  # c_int
SW_SHOWNOACTIVATE = 4  # c_int
SW_SHOW = 5  # c_int
SW_MINIMIZE = 6  # c_int
SW_SHOWMINNOACTIVE = 7  # c_int
SW_SHOWNA = 8  # c_int
SW_RESTORE = 9  # c_int

GUI_CARETBLINKING = 1  # c_int
GUI_INMOVESIZE = 2  # c_int
GUI_INMENUMODE = 4  # c_int
GUI_SYSTEMMENUMODE = 8  # c_int
GUI_POPUPMENUMODE = 16  # c_int

LWA_COLORKEY = 1  # c_int
LWA_ALPHA = 2  # c_int

# Brush Style
BS_SOLID = 0  # c_int
BS_NULL = 1  # c_int
BS_HATCHED = 2  # c_int
BS_PATTERN = 3  # c_int
BS_INDEXED = 4  # c_int
BS_DIBPATTERN = 5  # c_int
BS_DIBPATTERNPT = 6  # c_int
BS_PATTERN8X8 = 7  # c_int
BS_DIBPATTERN8X8 = 8  # c_int
BS_MONOPATTERN = 9  # c_int

# Pen Style
PS_TYPE_MASK = 983040  # c_int
PS_STYLE_MASK = 15  # c_int
PS_SOLID = 0  # c_int
PS_COSMETIC = 0  # c_int
PS_DASH = 1  # c_int
PS_DOT = 2  # c_int
PS_DASHDOT = 3  # c_int
PS_DASHDOTDOT = 4  # c_int
PS_NULL = 5  # c_int
PS_INSIDEFRAME = 6  # c_int
PS_USERSTYLE = 7  # c_int
PS_ALTERNATE = 8  # c_int
PS_ENDCAP_MASK = 3840  # c_int
PS_ENDCAP_FLAT = 512  # c_int
PS_ENDCAP_ROUND = 0  # c_int
PS_ENDCAP_SQUARE = 256  # c_int
PS_JOIN_MASK = 61440  # c_int
PS_JOIN_ROUND = 0  # c_int
PS_JOIN_BEVEL = 4096  # c_int
PS_JOIN_MITER = 8192  # c_int
PS_GEOMETRIC = 65536  # c_int

HS_DIAGCROSS = 5  # c_int

WH_KEYBOARD_LL = 0x0d
WH_MOUSE_LL = 0x0e
WH_SHELL = 10

# A good reference for these:
# https://wiki.winehq.org/List_Of_Windows_Messages
WM_KEYDOWN = 0x100
WM_KEYUP = 0x101
WM_SYSKEYDOWN = 0x104
WM_SYSKEYUP = 0x105
WM_CLOSE = 16  # c_int
WM_DESTROY = 2
WM_QUIT = 0x12
WM_DISPLAYCHANGE = 0x7e
WM_SETTINGCHANGE = 0x1a
WM_PAINT = 15
WM_CREATE = 1
WM_SETFONT = 48
WM_SETREDRAW = 11
WM_LBUTTONDOWN = 0x0201
WM_NCACTIVATE = 0x86
WM_NCCALCSIZE = 0x83
WM_NCHITTEST = 0x84
WM_POWERBROADCAST = 0x218
WM_DEVICECHANGE = 0x219
WM_WTSSESSION_CHANGE = 0x02B1
WM_USER = 0x0400
WM_APP = 0x8000




WM_MESSAGE_NAMES: Dict[str, int] = {
    'keydown': WM_KEYDOWN,
    'keyup': WM_KEYUP,
    'syskeydown': WM_SYSKEYDOWN,
    'syskeyup': WM_SYSKEYUP,
    'close': WM_CLOSE,
    # 'destroy': WM_DESTROY,
    'quit': WM_QUIT,
    'displaychange': WM_DISPLAYCHANGE,
    'settingchange': WM_SETTINGCHANGE,
    'paint': WM_PAINT,
    'setfont': WM_SETFONT,
    'setredraw': WM_SETREDRAW,
}


# https://msdn.microsoft.com/en-us/library/windows/desktop/ms645607(v=vs.85).aspx
MK_LBUTTON = 0x0001


CS_BYTEALIGNCLIENT = 4096
CS_BYTEALIGNWINDOW = 8192
CS_KEYCVTWINDOW = 4
CS_NOKEYCVT = 256
CS_CLASSDC = 64
CS_DBLCLKS = 8
CS_GLOBALCLASS = 16384
CS_HREDRAW = 2
CS_NOCLOSE = 512
CS_OWNDC = 32
CS_PARENTDC = 128
CS_SAVEBITS = 2048
CS_VREDRAW = 1
CS_IME = 0x10000


LLKHF_EXTENDED = 0x1
LLKHF_LOWER_IL_INJECTED = 0x2
LLKHF_INJECTED = 0x10
LLHKF_ALTDOWN = 0x20
LLHKF_UP = 0x80


CW_USEDEFAULT = 0x80000000

WHITE_BRUSH = 0


# System Parameter Info
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms724947(v=vs.85).asp
SPI_GETACCESSTIMEOUT = 0x3c
SPI_GETAUDIODESCRIPTION = 0x74  # Not supported in Windows XP/2000
SPI_GETCLIENTAREAANIMATION = 0x1042  # Not supported in Windows XP/2000
SPI_GETDISABLEOVERLAPPEDCONTENT = 0x1040  # Not supported in Windows XP/2000
SPI_GETFILTERKEYS = 0x32
SPI_GETFOCUSBORDERHEIGHT = 0x2010  # Not supported in Windows 2000
SPI_GETFOCUSBORDERWIDTH = 0x200e  # Not supported in Windows 2000
SPI_GETHIGHCONTRAST = 0x42
SPI_GETLOGICALDPIOVERRIDE = 0x9e
SPI_GETMESSAGEDURATION = 0x2016  # Not supported in Windows 2000/XP
SPI_GETMOUSECLICKLOCK = 0x101e  # Not supported in Windows 2000
SPI_GETMOUSECLICKLOCKTIME = 0x2008  # Not supported in Windows 2000
SPI_GETMOUSEKEYS = 0x36
SPI_GETMOUSESONAR = 0x101c  # Not supported in Windows 2000
SPI_GETMOUSEVANISH = 0x1020  # Not supported in Windows 2000
SPI_GETSCREENREADER = 0x46
SPI_GETSHOWSOUNDS = 0x38
SPI_GETSOUNDSENTRY = 0x40
SPI_GETSTICKYKEYS = 0x3a
SPI_GETTOGGLEKEYS = 0X34

SPI_SETACCESSTIMEOUT = 0x3d
SPI_SETAUDIODESCRIPTION = 0x75  # Not supported in Windows XP/2000
SPI_SETCLIENTAREAANIMATION = 0x1043  # Not supported in Windows XP/2000
SPI_SETDISABLEOVERLAPPEDCONTENT = 0x1041  # Not supported in Windows XP/2000
SPI_SETFILTERKEYS = 0x33
SPI_SETFOCUSBORDERHEIGHT = 0x2011  # Not supported in Windows 2000
SPI_SETFOCUSBORDERWIDTH = 0x200f  # Not supported in Windows 2000
SPI_SETHIGHCONTRAST = 0x43
SPI_SETLOGICALDPIOVERRIDE = 0x9f
SPI_SETMESSAGEDURATION = 0x2017  # Not supported in Windows 2000/XP
SPI_SETMOUSECLICKLOCK = 0x101f  # Not supported in Windows 2000
SPI_SETMOUSECLICKLOCKTIME = 0x2009  # Not supported in Windows 2000
SPI_SETMOUSEKEYS = 0x37
SPI_SETMOUSESONAR = 0x101d  # Not supported in Windows 2000
SPI_SETMOUSEVANISH = 0x1021  # Not supported in Windows 2000
SPI_SETSCREENREADER = 0x47
SPI_SETSERIALKEYS = 0x3f  # Windows 2000/XP - should be set by user in control panel
SPI_SETSHOWSOUNDS = 0x39
SPI_SETSOUNDSENTRY = 0x41
SPI_SETSTICKYKEYS = 0x3b
SPI_SETTOGGLEKEYS = 0X35

SPI_GETCLEARTYPE = 0x1048
SPI_GETDESKWALLPAPER = 0x73
SPI_GETDROPSHADOW = 0x1024  # Not supported in Windows 2000
SPI_GETFLATMENU = 0x1022  # Not supported in Windows 2000
SPI_GETFONTSMOOTHING = 0x4a
SPI_GETFONTSMOOTHINGCONTRAST = 0x200c  # Not supported in Windows 2000
SPI_GETFONTSMOOTHINGGRADIENTATION = 0x2012  # Not supported in Windows 2000
SPI_GETFONTSMOOTHINGTYPE = 0x200a  # Not supported in Windows 2000
SPI_GETWORKAREA = 0x30  # Use GetMonitorInfo instead

SPI_SETCLEARTYPE = 0x1049
SPI_SETCURSORS = 0x57
SPI_SETDESKPATTERN = 0x15
SPI_SETDESKWALLPAPER = 0x14
SPI_SETDROPSHADOW = 0x1025  # Not supported in Windows 2000
SPI_SETFLATMENU = 0x1023  # Not supported in Windows 2000
SPI_SETFONTSMOOTHING = 0x4b
SPI_SETFONTSMOOTHINGCONTRAST = 0x200d  # Not supported in Windows 2000
SPI_SETFONTSMOOTHINGGRADIENTATION = 0x2013  # Not supported in Windows 2000
SPI_SETFONTSMOOTHINGTYPE = 0x200b  # Not supported in Windows 2000
SPI_SETWORKAREA = 0x2f

SPI_GETICONMETRICS = 0x2d
SPI_GETICONTTILELOGFONT = 0x1f
SPI_GETICONTITLEWRAP = 0x19
SPI_ICONHORIZONTALSPACING = 0xd
SPI_ICONVERTICALSPACING = 0x18
SPI_SETICONMETRICS = 0x2e
SPI_SETICONS = 0x58
SPI_SETICONTITLELOGFONT = 0x22
SPI_SETICONTITLEWRAP = 0x1a

SPI_GETBEEP = 0x1
SPI_GETBLOCKSENDINPUTRESETS = 0x1026
SPI_GETCONTACTVISUALIZATION = 0x2018
SPI_GETDEFAULTINPUTLANG = 0x59
SPI_GETGESTUREVISUALIZATION = 0x201a
SPI_GETKEYBOARDCUES = 0x100a
SPI_GETKEYBOARDPREF = 0x44
SPI_GETKEYBOARDSPEED = 0xa  # Key repeat speed
SPI_GETMOUSE = 0x3
SPI_GETMOUSEHOVERHEIGHT = 0x64
SPI_GETMOUSEHOVERTIME = 0x66
SPI_GETMOUSEHOVERWIDTH = 0x62
SPI_GETMOUSESPEED = 0x70
SPI_GETMOUSETRAILS = 0x5e  # Not supported in Windows 2000
SPI_GETMOUSEWHEELROTATING = 0x201c
SPI_GETPENVISUALIZATION = 0x201e
SPI_GETSNAPTODEFBUTTON = 0x5f
SPI_GETSYSTEMLANGUAGEBAR = 0x1050
SPI_GETTHREADLOCALINPUTSETTIGNS = 0x104e
SPI_GETWHEELSCROLLCHARS = 0x6c
SPI_GETWHEELSCROLLLINES = 0x68

SPI_SETBEEP = 0x2
SPI_SETBLOCKSENDINPUTRESETS = 0x1027
SPI_SETCONTACTVISUALIZATION = 0x2019
SPI_SETDEFAULTINPUTLANG = 0x5a
SPI_SETDOUBLECLICKTIME = 0x20
SPI_SETDOUBLECLICKHEIGHT = 0x1e
SPI_SETDOUBLECLICKWIDTH = 0x1d
SPI_SETGESTUREVISUALIZATION = 0x201b
SPI_SETKEYBOARDCUES = 0x100b
SPI_SETKEYBOARDDELAY = 0x17
SPI_SETKEYBOARDPREF = 0x45
SPI_SETKEYBOARDSPEED = 0xb  # Key repeat speed
SPI_SETLANGTOGGLE = 0x5b
SPI_SETMOUSE = 0x4
SPI_SETMOUSEBUTTONSWAP = 0x21
SPI_SETMOUSEHOVERHEIGHT = 0x65
SPI_SETMOUSEHOVERTIME = 0x67
SPI_SETMOUSEHOVERWIDTH = 0x63
SPI_SETMOUSESPEED = 0x71
SPI_SETMOUSETRAILS = 0x5d  # Not supported in Windows 2000
SPI_SETMOUSEWHEELROTATING = 0x201d
SPI_SETPENVISUALIZATION = 0x201f
SPI_SETSNAPTODEFBUTTON = 0x60
SPI_SETSYSTEMLANGUAGEBAR = 0x1051
SPI_SETTHREADLOCALINPUTSETTIGNS = 0x104f
SPI_SETWHEELSCROLLCHARS = 0x6d
SPI_SETWHEELSCROLLLINES = 0x69

SPI_GETMENUDROPALIGNMENT = 0x1b
SPI_GETMENUFADE = 0x1012
SPI_GETMENUSHOWDELAY = 0x6a

SPI_SETMENUDROPALIGNMENT = 0x1c
SPI_SETMENUFADE = 0x1013
SPI_SETMENUSHOWDELAY = 0x6d

SPI_GETCOMBOBOXANIMATION = 0x1004
SPI_GETCURSORSHADOW = 0x101a
SPI_GETGRADIENTCAPTIONS = 0x1008
SPI_GETHOTTRACKING = 0x100e
SPI_GETLISTBOXSMOOTHSCROLLING = 0x1006
SPI_GETMENUANIMATION = 0x102
SPI_GETMENUUNDERLINES = 0x100a
SPI_GETSELECTIONFADE = 0x1014
SPI_GETTOOLTIPANIMATION = 0x1016
SPI_GETTOOLTIPFADE = 0x1018
SPI_GETUIEFFECTS = 0x103e

SPI_SETCOMBOBOXANIMATION = 0x1005
SPI_SETCURSORSHADOW = 0x101b
SPI_SETGRADIENTCAPTIONS = 0x1009
SPI_SETHOTTRACKING = 0x100f
SPI_SETLISTBOXSMOOTHSCROLLING = 0x1007
SPI_SETMENUANIMATION = 0x103
SPI_SETMENUUNDERLINES = 0x100b
SPI_SETSELECTIONFADE = 0x1015
SPI_SETTOOLTIPANIMATION = 0x1019
SPI_SETTOOLTIPFADE = 0x1019
SPI_SETUIEFFECTS = 0x103f

SPI_GETACTIVEWINDOWTRACKING = 0x1000
SPI_GETACTIVEWNDTRKZORDER = 0x100c
SPI_GETACTIVEWNDTRKTIMEOUT = 0x2002
SPI_GETANIMATION = 0x48
SPI_GETBORDER = 0x5
SPI_GETCARETWIDTH = 0x2006
SPI_GETDOCKMOVING = 0x90  # Not supported in Windows 2000/XP/Vista
SPI_GETDRAGFROMMAXIMIZE = 0x8c  # Not supported in Windows 2000/XP/Vista
SPI_GETDRAGFULLWINDOWS = 0x26
SPI_GETFOREGROUNDFLASHCOUNT = 0x2004
SPI_GETFOREGROUNDLOCKTIMEOUT = 0x2000
SPI_GETMINIMIZEDMETRICS = 0x2b
SPI_GETMOUSEDOCKERTHRESHOLD = 0x7e  # Not supported in Windows 2000/XP/Vista
SPI_GETMOUSEDRAGOUTTHRESHOLD = 0x84  # Not supported in Windows 2000/XP/Vista
SPI_GETMOUSESIDEMOVETHRESHOLD = 0x88  # Not supported in Windows 2000/XP/Vista
SPI_GETNONCLIENTMETRICS = 0x29
SPI_GETPENDOCKTHRESHOLD = 0x80  # Not supported in Windows 2000/XP/Vista
SPI_GETPENDRAGOUTTHRESHOLD = 0x86  # Not supported in Windows 2000/XP/Vista
SPI_GETPENSIDEMOVETHRESHOLD = 0x8a  # Not supported in Windows 2000/XP/Vista
SPI_GETSHOWIMEUI = 0x6e
SPI_GETSNAPSIZING = 0x8e  # Not supported in Windows 2000/XP/Vista
SPI_GETWINARRANGING = 0x82  # Not supported in Windows 2000/XP/Vista

SPI_SETACTIVEWINDOWTRACKING = 0x1001
SPI_SETACTIVEWNDTRKZORDER = 0x100d
SPI_SETACTIVEWNDTRKTIMEOUT = 0x2003
SPI_SETANIMATION = 0x49
SPI_SETBORDER = 0x6
SPI_SETCARETWIDTH = 0x2007
SPI_SETDOCKMOVING = 0x91  # Not supported in Windows 2000/XP/Vista
SPI_SETDRAGFROMMAXIMIZE = 0x8d  # Not supported in Windows 2000/XP/Vista
SPI_SETDRAGFULLWINDOWS = 0x25
SPI_SETDRAGHEIGHT = 0x4d
SPI_SETDRAGWIDTH = 0x4c
SPI_SETFOREGROUNDFLASHCOUNT = 0x2005
SPI_SETFOREGROUNDLOCKTIMEOUT = 0x2001
SPI_SETMINIMIZEDMETRICS = 0x2c
SPI_SETMOUSEDOCKERTHRESHOLD = 0x7f  # Not supported in Windows 2000/XP/Vista
SPI_SETMOUSEDRAGOUTTHRESHOLD = 0x85  # Not supported in Windows 2000/XP/Vista
SPI_SETMOUSESIDEMOVETHRESHOLD = 0x89  # Not supported in Windows 2000/XP/Vista
SPI_SETNONCLIENTMETRICS = 0x2a
SPI_SETPENDOCKTHRESHOLD = 0x81  # Not supported in Windows 2000/XP/Vista
SPI_SETPENDRAGOUTTHRESHOLD = 0x87  # Not supported in Windows 2000/XP/Vista
SPI_SETPENSIDEMOVETHRESHOLD = 0x8b  # Not supported in Windows 2000/XP/Vista
SPI_SETSHOWIMEUI = 0x6f
SPI_SETSNAPSIZING = 0x8f  # Not supported in Windows 2000/XP/Vista
SPI_SETWINARRANGING = 0x83  # Not supported in Windows 2000/XP/Vista

SPIF_UPDATEINIFILE = 0x01  # Writes the new system-wide parameter setting to the user profile.
SPIF_SENDCHANGE = 0x02  # Broadcasts the WM_SETTINGCHANGE message after updating the user profile.
SPIF_SENDWININICHANGE = 0x02  # Same as SPIF_SENDCHANGE.

# https://msdn.microsoft.com/en-us/library/windows/desktop/ms632600(v=vs.85).aspx
WS_BORDER = 0x800000
WS_CHILD = 0x40000000
WS_CHILDWINDOW = 0x40000000
WS_CLIPCHILDREN = 0x2000000
WS_CLIPSIBLINGS = 0x4000000
WS_DISABLED = 0x8000000
WS_DLGFRAME = 0x400000
WS_GROUP = 0x20000
WS_HSCROLL = 0x100000
WS_ICONIC = 0x20000000
WS_MAXIMIZE = 0x1000000
WS_MAXIMIZEBOX = 0x10000
WS_MINIMIZE = 0x20000000
WS_MINIMIZEBOX = 0x20000
WS_OVERLAPPED = 0x00000000
WS_POPUP = 0x80000000
WS_SIZEBOX = 0x40000
WS_SYSMENU = 0x80000
WS_TABSTOP = 0x10000
WS_THICKFRAME = 0x40000
WS_TILED = 0x00000000
WS_VISIBLE = 0x10000000
WS_VSCROLL = 0x200000
WS_CAPTION = WS_BORDER | WS_DLGFRAME  # = 0xC00000
WS_TILEDWINDOW = (
        WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU | WS_THICKFRAME | WS_MINIMIZEBOX | WS_MAXIMIZEBOX
)
WS_OVERLAPPEDWINDOW = (
        WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU | WS_THICKFRAME | WS_MINIMIZEBOX | WS_MAXIMIZEBOX
)
WS_POPUPWINDOW = (WS_POPUP | WS_BORDER | WS_SYSMENU)

# Should not technically be in this file, but it's shared by multiple files.
WS_STYLE_BIT_MAP: Dict[str, int] = {
    'border': WS_BORDER,
    'child-window': WS_CHILDWINDOW,
    'clip-children': WS_CLIPCHILDREN,
    'clip-siblings': WS_CLIPSIBLINGS,
    'disabled': WS_DISABLED,
    'dialog-frame': WS_DLGFRAME,
    'group': WS_GROUP,
    'hscroll': WS_HSCROLL,
    'iconic': WS_ICONIC,
    'start-maximized': WS_MAXIMIZE,
    'maximize-button': WS_MAXIMIZEBOX,
    'start-minimized': WS_MINIMIZE,
    'minimize-button': WS_MINIMIZEBOX,
    'popup': WS_POPUP,
    'size-border': WS_SIZEBOX,
    'sysmenu-button': WS_SYSMENU,
    'tabstop': WS_TABSTOP,
    'visible': WS_VISIBLE,
    'vscroll': WS_VSCROLL,
}


# https://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
WS_EX_LEFT = 0x00000000
WS_EX_LTRREADING = 0x00000000
WS_EX_RIGHTSCROLLBAR = 0x00000000
WS_EX_DLGMODALFRAME = 0x1
WS_EX_NOPARENTNOTIFY = 0x4
WS_EX_TOPMOST = 0x8  # Set with SetWindowPos
WS_EX_ACCEPTFILES = 0x10
WS_EX_TRANSPARENT = 0x20
WS_EX_MDICHILD = 0x40
WS_EX_TOOLWINDOW = 0x80
WS_EX_WINDOWEDGE = 0x100  # raised edge border
WS_EX_CLIENTEDGE = 0x200  # window has sunken border
WS_EX_CONTEXTHELP = 0x400
WS_EX_RTLREADING = 0x2000
WS_EX_RIGHT = 0x1000
WS_EX_LEFTSCROLLBAR = 0x4000
WS_EX_CONTROLPARENT = 0x10000  # dialog manager recurses into children
WS_EX_STATICEDGE = 0x20000  # non-user input dialog border
WS_EX_APPWINDOW = 0x40000  # forces a top-level window onto the taskbar
WS_EX_LAYERED = 0x80000  # Before Windows 8, this was only supported for top-level windows
WS_EX_NOREDIRECTIONBITMAP = 0x200000
WS_EX_LAYOUTRTL = 0x400000
WS_EX_NOINHERITLAYOUT = 0x100000
WS_EX_COMPOSITED = 0x2000000  # Not supported by Windows 2000
WS_EX_NOACTIVATE = 0x8000000
WS_EX_OVERLAPPEDWINDOW = (WS_EX_WINDOWEDGE | WS_EX_CLIENTEDGE)
WS_EX_PALETTEWINDOW = (WS_EX_WINDOWEDGE | WS_EX_TOOLWINDOW | WS_EX_TOPMOST)

# Should not technically be in this file, but it's shared by multiple files.
WS_EX_STYLE_BIT_MAP: Dict[str, int] = {
    "double-border": WS_EX_DLGMODALFRAME,
    "no-parent-notify": WS_EX_NOPARENTNOTIFY,
    "topmost": WS_EX_TOPMOST,
    "file-dnd-target": WS_EX_ACCEPTFILES,
    "transparent": WS_EX_TRANSPARENT,
    "mdi-child": WS_EX_MDICHILD,
    "tool-window": WS_EX_TOOLWINDOW,
    "window-edge": WS_EX_WINDOWEDGE,
    "client-edge": WS_EX_CLIENTEDGE,
    "context-help": WS_EX_CONTEXTHELP,
    "right-aligned": WS_EX_RIGHT,
    "right-to-left": WS_EX_RTLREADING,
    "left-scrollbar": WS_EX_LEFTSCROLLBAR,
    "control-parent": WS_EX_CONTROLPARENT,
    "static-edge": WS_EX_STATICEDGE,
    "app-window": WS_EX_APPWINDOW,
    "layered": WS_EX_LAYERED,
    "no-inherit-layout": WS_EX_NOINHERITLAYOUT,
    "no-redirection-bitmap": WS_EX_NOREDIRECTIONBITMAP,
    "layout-right-to-left": WS_EX_LAYOUTRTL,
    "composited": WS_EX_COMPOSITED,
    "no-activate": WS_EX_NOACTIVATE,
}


# https://msdn.microsoft.com/en-us/library/windows/desktop/ms633545(v=vs.85).aspx
SWP_ASYNCWINDOWPOS = 0x4000
SWP_DEFERERASE = 0x2000
SWP_DRAWFRAME = 0x0020
SWP_FRAMECHANGED = 0x0020
SWP_HIDEWINDOW = 0x0080
SWP_NOACTIVATE = 0x0010
SWP_NOCOPYBITS = 0x0100
SWP_NOMOVE = 0x0002
SWP_NOOWNERZORDER = 0x0200
SWP_NOREPOSITION = 0x0200
SWP_NOREDRAW = 0x0008
SWP_NOSENDCHANGING = 0x0400
SWP_NOSIZE = 0x0001
SWP_NOZORDER = 0x0004
SWP_SHOWWINDOW = 0x0040

SWP_FLAG_MAP: Dict[str, int] = {
    "async-window-pos": SWP_ASYNCWINDOWPOS,
    "defer-erase": SWP_DEFERERASE,
    "draw-frame": SWP_DRAWFRAME,
    "frame-changed": SWP_FRAMECHANGED,
    "hide-window": SWP_HIDEWINDOW,
    "no-activate": SWP_NOACTIVATE,
    "no-copy-bits": SWP_NOCOPYBITS,
    "no-move": SWP_NOMOVE,
    "no-owner-zorder": SWP_NOOWNERZORDER,
    "no-reposition": SWP_NOREPOSITION,
    "no-redraw": SWP_NOREDRAW,
    "no-send-changing": SWP_NOSENDCHANGING,
    "no-size": SWP_NOSIZE,
    "no-zorder": SWP_NOZORDER,
    "show-window": SWP_SHOWWINDOW,
}


SC_MANAGER_ENUMERATE_SERVICE = 0x4
SC_MANAGER_CONNECT = 0x1
SC_ENUM_PROCESS_INFO = 0

SERVICE_DRIVER = 0xb
SERVICE_FILE_SYSTEM_DRIVER = 0x2
SERVICE_KERNEL_DRIVER = 0x1
SERVICE_WIN32_OWN_PROCESS = 0x10
SERVICE_WIN32_SHARE_PROCESS = 0x20
SERVICE_WIN32 = SERVICE_WIN32_OWN_PROCESS | SERVICE_WIN32_SHARE_PROCESS

SERVICE_ACTIVE = 1
SERVICE_INACTIVE = 2
SERVICE_STATE_ALL = SERVICE_ACTIVE | SERVICE_INACTIVE

SERVICE_ACCEPT_NETBINDCHANGE = 0x00000010
SERVICE_ACCEPT_PARAMCHANGE = 0x00000008
SERVICE_ACCEPT_PAUSE_CONTINUE = 0x00000002
SERVICE_ACCEPT_PRESHUTDOWN = 0x00000100
SERVICE_ACCEPT_SHUTDOWN = 0x00000004
SERVICE_ACCEPT_STOP = 0x00000001

LF_FACESIZE = 32

ERROR_MORE_DATA = 0xea

# https://msdn.microsoft.com/en-us/library/windows/desktop/dd162911(v=vs.85).aspx
RDW_INVALIDATE = 1
RDW_INTERNALPAINT = 2
RDW_ERASE = 4
RDW_VALIDATE = 8
RDW_NOINTERNALPAINT = 16
RDW_NOERASE = 32
RDW_NOCHILDREN = 64
RDW_ALLCHILDREN = 128
RDW_UPDATENOW = 256
RDW_ERASENOW = 512
RDW_FRAME = 1024
RDW_NOFRAME = 2048

MAX_USERNAME_LENGTH = 256

TOKEN_QUERY = 0x8

# https://msdn.microsoft.com/en-us/library/aa379626(v=vs.85).aspx
TOKEN_INFORMATION__TOKEN_USER = 1

# https://msdn.microsoft.com/en-us/library/ms646270(v=vs.85).aspx
INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

# https://msdn.microsoft.com/en-us/library/ms646271(v=vs.85).aspx
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_UNICODE = 0x0004
KEYEVENTF_SCANCODE = 0x0008

ANSI_CHARSET = 0
ARABIC_CHARSET = 178
BALTIC_CHARSET = 186
CHINESEBIG5_CHARSET = 136
DEFAULT_CHARSET = 1
EASTEUROPE_CHARSET = 238
GB2312_CHARSET = 134
GREEK_CHARSET = 161
HANGEUL_CHARSET = 129
HEBREW_CHARSET = 177
JOHAB_CHARSET = 130
MAC_CHARSET = 77
OEM_CHARSET = 255
RUSSIAN_CHARSET = 204
SHIFTJIS_CHARSET = 128
SYMBOL_CHARSET = 2
THAI_CHARSET = 222
TURKISH_CHARSET = 162
VIETNAMESE_CHARSET = 163

# font family
MWLF_FAMILY_DEFAULT = (0 << 4)  # any family
MWLF_FAMILY_SERIF = (1 << 4)  # variable stroke width, serif
MWLF_FAMILY_SANSSERIF = (2 << 4)  # variable stroke width, sans-serif
MWLF_FAMILY_MODERN = (3 << 4)  # constant stroke width
FF_DONTCARE = MWLF_FAMILY_DEFAULT
FF_ROMAN = MWLF_FAMILY_SERIF
FF_SWISS = MWLF_FAMILY_SANSSERIF
FF_MODERN = MWLF_FAMILY_MODERN
FF_SCRIPT = (4 << 4)  # ` Cursive, etc.
FF_DECORATIVE = (5 << 4)  # Old English, etc.

# font weights
MWLF_WEIGHT_DEFAULT = 0  # any weight
MWLF_WEIGHT_THIN = 100  # thin
MWLF_WEIGHT_EXTRALIGHT = 200
MWLF_WEIGHT_LIGHT = 300  # light
MWLF_WEIGHT_NORMAL = 400  # regular
MWLF_WEIGHT_REGULAR = 400
MWLF_WEIGHT_MEDIUM = 500  # medium
MWLF_WEIGHT_DEMIBOLD = 600
MWLF_WEIGHT_BOLD = 700  # bold
MWLF_WEIGHT_EXTRABOLD = 800
MWLF_WEIGHT_BLACK = 900  # black
FW_DONTCARE = MWLF_WEIGHT_DEFAULT
FW_THIN = MWLF_WEIGHT_THIN
FW_EXTRALIGHT = MWLF_WEIGHT_EXTRALIGHT
FW_LIGHT = MWLF_WEIGHT_LIGHT
FW_NORMAL = MWLF_WEIGHT_NORMAL
FW_MEDIUM = MWLF_WEIGHT_MEDIUM
FW_SEMIBOLD = MWLF_WEIGHT_DEMIBOLD
FW_BOLD = MWLF_WEIGHT_BOLD
FW_EXTRABOLD = MWLF_WEIGHT_EXTRABOLD
FW_HEAVY = MWLF_WEIGHT_BLACK
FW_ULTRALIGHT = FW_EXTRALIGHT
FW_REGULAR = FW_NORMAL
FW_DEMIBOLD = FW_SEMIBOLD
FW_ULTRABOLD = FW_EXTRABOLD
FW_BLACK = FW_HEAVY

# output precision
MWLF_TYPE_DEFAULT = 0  # any font
MWLF_TYPE_SCALED = 4  # outlined font (tt or adobe)
MWLF_TYPE_RASTER = 5  # raster only
MWLF_TYPE_TRUETYPE = 7  # truetype only
MWLF_TYPE_ADOBE = 10  # adobe type 1 only
OUT_DEFAULT_PRECIS = MWLF_TYPE_DEFAULT
OUT_STRING_PRECIS = 1
OUT_CHARACTER_PRECIS = 2
OUT_STROKE_PRECIS = 3
OUT_TT_PRECIS = MWLF_TYPE_SCALED
OUT_DEVICE_PRECIS = MWLF_TYPE_RASTER
OUT_RASTER_PRECIS = MWLF_TYPE_RASTER
OUT_TT_ONLY_PRECIS = MWLF_TYPE_TRUETYPE
OUT_OUTLINE_PRECIS = 8
OUT_SCREEN_OUTLINE_PRECIS = 9

# clip precision
CLIP_DEFAULT_PRECIS = 0
CLIP_CHARACTER_PRECIS = 1
CLIP_STROKE_PRECIS = 2
CLIP_MASK = 0xf
CLIP_LH_ANGLES = (1 << 4)
CLIP_TT_ALWAYS = (2 << 4)
CLIP_EMBEDDED = (8 << 4)

# output quality
DEFAULT_QUALITY = 0
DRAFT_QUALITY = 1
PROOF_QUALITY = 2
NONANTIALIASED_QUALITY = 3
ANTIALIASED_QUALITY = 4

LOGPIXELSX = 88
LOGPIXELSY = 90
TWIPS_IN_CM = 567

OPAQUE = 0xFF
TRANSPARENT = 0

DT_BOTTOM = 8
DT_CALCRECT = 1024
DT_CENTER = 1
DT_EDITCONTROL = 8192
DT_END_ELLIPSIS = 32768
DT_PATH_ELLIPSIS = 16384
DT_WORD_ELLIPSIS = 0x40000
DT_EXPANDTABS = 64
DT_EXTERNALLEADING = 512
DT_LEFT = 0
DT_MODIFYSTRING = 65536
DT_NOCLIP = 256
DT_NOPREFIX = 2048
DT_RIGHT = 2
DT_RTLREADING = 131072
DT_SINGLELINE = 32
DT_TABSTOP = 128
DT_TOP = 0
DT_VCENTER = 4
DT_WORDBREAK = 16
DT_INTERNAL = 4096


COLOR_3DDKSHADOW = 21
COLOR_3DFACE = 15
COLOR_3DHILIGHT = 20
COLOR_3DHIGHLIGHT = 20
COLOR_3DLIGHT = 22
COLOR_BTNHILIGHT = 20
COLOR_3DSHADOW = 16
COLOR_ACTIVEBORDER = 10
COLOR_ACTIVECAPTION = 2
COLOR_APPWORKSPACE = 12
COLOR_BACKGROUND = 1
COLOR_DESKTOP = 1
COLOR_BTNFACE = 15
COLOR_BTNHIGHLIGHT = 20
COLOR_BTNSHADOW = 16
COLOR_BTNTEXT = 18
COLOR_CAPTIONTEXT = 9
COLOR_GRAYTEXT = 17
COLOR_HIGHLIGHT = 13
COLOR_HIGHLIGHTTEXT = 14
COLOR_INACTIVEBORDER = 11
COLOR_INACTIVECAPTION = 3
COLOR_INACTIVECAPTIONTEXT = 19
COLOR_INFOBK = 24
COLOR_INFOTEXT = 23
COLOR_MENU = 4
COLOR_MENUTEXT = 7
COLOR_SCROLLBAR = 0
COLOR_WINDOW = 5
COLOR_WINDOWFRAME = 6
COLOR_WINDOWTEXT = 8
COLOR_HOTLIGHT = 26
COLOR_GRADIENTACTIVECAPTION = 27
COLOR_GRADIENTINACTIVECAPTION = 28


IDI_APPLICATION = 32512
IDI_HAND = 32513
IDI_QUESTION = 32514
IDI_EXCLAMATION = 32515
IDI_ASTERISK = 32516
IDI_WINLOGO = 32517

IDC_ARROW = 32512
IDC_IBEAM = 32513
IDC_WAIT = 32514
IDC_CROSS = 32515
IDC_UPARROW = 32516
IDC_SIZENWSE = 32642
IDC_SIZENESW = 32643
IDC_SIZEWE = 32644
IDC_SIZENS = 32645
IDC_SIZEALL = 32646
IDC_NO = 32648
IDC_HAND = 32649
IDC_APPSTARTING = 32650
IDC_HELP = 32651
IDC_ICON = 32641
IDC_SIZE = 32640


# https://msdn.microsoft.com/en-us/library/windows/desktop/ms645618(v=vs.85).aspx
HTBORDER = 18
HTBOTTOM = 15
HTBOTTOMLEFT = 16
HTBOTTOMRIGHT = 17
HTCAPTION = 2
HTCLIENT = 1
HTCLOSE = 20
HTERROR = -2
HTGROWBOX = 4
HTHELP = 21
HTHSCROLL = 6
HTLEFT = 10
HTMENU = 5
HTMAXBUTTON = 9
HTMINBUTTON = 8
HTNOWHERE = 0
HTREDUCE = 8
HTRIGHT = 11
HTSIZE = 4
HTSYSMENU = 3
HTTOP = 12
HTTOPLEFT = 13
HTTOPRIGHT = 14
HTTRANSPARENT = -1
HTVSCROLL = 7
HTZOOM = 9


# https://msdn.microsoft.com/en-us/library/windows/desktop/ms681381(v=vs.85).aspx

# https://msdn.microsoft.com/en-us/library/windows/desktop/ms681382(v=vs.85).aspx
ERROR_ACCESS_DENIED = 5
ERROR_INVALID_PARAMETER = 87
ERROR_INSUFFICIENT_BUFFER = 122


# See https://msdn.microsoft.com/en-us/library/windows/desktop/ms644991(v=vs.85).aspx
# wparam -> lparam meanings
HSHELL_WINDOWCREATED = 1  # -> A handle to the window being created.
HSHELL_WINDOWDESTROYED = 2  # -> A handle to the top-level window being destroyed.
HSHELL_ACTIVATESHELLWINDOW = 3  # -> Not used.  (shell window focused)
HSHELL_WINDOWACTIVATED = 4  # -> A handle to the activated window. (window focused)
HSHELL_GETMINRECT = 5  # -> A pointer to a SHELLHOOKINFO structure. (window minimized)
HSHELL_REDRAW = 6  # -> A handle to the window that needs to be redrawn.
HSHELL_TASKMAN = 7  # -> Can be ignored.
HSHELL_LANGUAGE = 8  # -> ???
HSHELL_SYSMENU = 9  # -> ???
HSHELL_ENDTASK = 10  # -> A handle to the window that should be forced to exit.
HSHELL_ACCESSIBILITYSTATE = 11  # -> ???
HSHELL_WINDOWREPLACED = 13  # A handle to the window being replaced.
HSHELL_WINDOWREPLACING = 14  # -> A handle to the window replacing the top-level window.
HSHELL_MONITORCHANGED = 16  # -> A handle to the window that moved to a different monitor.
HSHELL_HIGHBIT = 0x8000  # used to augment an existing message
HSHELL_RUDEAPPACTIVATED = 0x8004  # -> A handle to the activated window; treat as WINDOWACTIVATED.
HSHELL_FLASH = 0x8006  # -> A handle to the window that needs to be flashed.  One message per flash
HSHELL_APPCOMMAND = 12  # -> The APPCOMMAND which has been unhandled by the application
# or other hooks. See WM_APPCOMMAND and use the GET_APPCOMMAND_LPARAM macro to retrieve this
# parameter.
# We get shell message "0x35" and "0x36" when "alt-tab" or other methods for bringing up the
# on-screen window selector.  0x35 opens it, 0x36 closes it, it seems.
HSHELL_UNKNOWN_35 = 0x35
HSHELL_UNKNOWN_36 = 0x36

# See
# https://referencesource.microsoft.com/#System.Windows.Forms/winforms/Managed/System/WinForms/NativeMethods.cs,3d19d38cf9b246fa
CCHDEVICENAME = 32


S_OK = 0


# https://docs.microsoft.com/en-us/windows/win32/api/shellscalingapi/ne-shellscalingapi-process_dpi_awareness
PROCESS_DPI_UNAWARE = 0
PROCESS_SYSTEM_DPI_AWARE = 1
PROCESS_PER_MONITOR_DPI_AWARE = 2

# DEVICE_SCALE_FACTOR enum
SCALE_100_PERCENT = 100
SCALE_120_PERCENT = 120
SCALE_140_PERCENT = 140
SCALE_150_PERCENT = 150
SCALE_160_PERCENT = 160
SCALE_180_PERCENT = 180
SCALE_225_PERCENT = 225


# https://docs.microsoft.com/en-us/windows/win32/api/shellscalingapi/ne-shellscalingapi-monitor_dpi_type
MDT_EFFECTIVE_DPI = 0
MDT_ANGULAR_DPI = 1
MDT_RAW_DPI = 2
MDT_DEFAULT = MDT_EFFECTIVE_DPI


# https://docs.microsoft.com/en-us/windows/win32/power/wm-powerbroadcast
# Power status has changed.
PBT_APMPOWERSTATUSCHANGE = 10

# Operation is resuming automatically from a low-power state.  This message is sent every time the
# system resumes.
PBT_APMRESUMEAUTOMATIC = 18

# Operation is resuming from a low-power state. This message is sent after PBT_APMRESUMEAUTOMATIC
# if the resume is triggered by user input, such as pressing a key.
PBT_APMRESUMESUSPEND = 7

# System is suspending operation.
PBT_APMSUSPEND = 4

# A power setting change event has been received.
PBT_POWERSETTINGCHANGE = 32787


# https://docs.microsoft.com/en-us/windows/win32/termserv/wm-wtssession-change
NOTIFY_FOR_ALL_SESSIONS = 1
NOTIFY_FOR_THIS_SESSION = 0

WTS_CONSOLE_CONNECT = 0x1
WTS_CONSOLE_DISCONNECT = 0x2
WTS_REMOTE_CONNECT = 0x3
WTS_REMOTE_DISCONNECT = 0x4
WTS_SESSION_LOGON = 0x5
WTS_SESSION_LOGOFF = 0x6
WTS_SESSION_LOCK = 0x7
WTS_SESSION_UNLOCK = 0x8
WTS_SESSION_REMOTE_CONTROL = 0x9
WTS_SESSION_CREATE = 0xA
WTS_SESSION_TERMINATE = 0xB
