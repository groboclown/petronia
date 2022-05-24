"""Basic usage of the library."""

from typing import Any
import ctypes
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.util import i18n as _
from petronia_native.common import user_messages
from . import defs


class Xcb:
    __slots__ = (
        '__dll', '__connection',
        '__screen', '__default_visual',
    )

    def __init__(self) -> None:
        self.__dll = ctypes.cdll.LoadLibrary('libxcb.so')
        self.__connection: defs.XcbConnectionPtr = defs.XcbConnectionPtr()
        self.__screen: defs.XcbScreenP = defs.XcbScreenP()
        self.__default_visual: defs.XcbVisualtypeP = defs.XcbVisualtypeP()

    def connect(self) -> StdRet[None]:
        xcb_connect = self.__dll.xcb_connect
        xcb_connect.restype = defs.XcbConnectionPtr
        xcb_connect.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
        xcb_connection_has_error = self.__dll.xcb_connection_has_error
        xcb_connection_has_error.restype = ctypes.c_int
        xcb_connection_has_error.argtypes = [defs.XcbConnectionPtr]

        print("Connecting")
        if self.__connection.value is not None:
            return StdRet.pass_errmsg(
                user_messages.TRANSLATION_CATALOG,
                _('already connected to server'),
            )
        default_screen = ctypes.c_int(0)
        print("connecting to default screen")
        self.__connection = xcb_connect(None, ctypes.byref(default_screen))
        print("check if connection has error (" + repr(self.__connection) + ")")
        # This causes a core dump
        error_code: int = xcb_connection_has_error(self.__connection)
        print("error code " + repr(error_code))
        if error_code != 0:
            return StdRet.pass_errmsg(
                user_messages.TRANSLATION_CATALOG,
                _('cannot open X11 display (error {error_code}'),
                error_code=error_code,
            )
        print("get screen")
        self.__screen = self.__dll.xcb_aux_get_screen(self.__connection, default_screen)
        self.__default_visual = _draw_find_visual(
            self.__dll, self.__screen, self.__screen.value.root_visual,
        )

        # globalconf.default_visual = draw_default_visual(globalconf.screen);
        #     if(default_init_flags & INIT_FLAG_ARGB)
        #         globalconf.visual = draw_argb_visual(globalconf.screen);
        #     if(!globalconf.visual)
        #         globalconf.visual = globalconf.default_visual;
        #     globalconf.default_depth = draw_visual_depth(globalconf.screen, globalconf.visual->visual_id);
        #     globalconf.default_cmap = globalconf.screen->default_colormap;
        #     if(globalconf.default_depth != globalconf.screen->root_depth)
        #     {
        #         // We need our own color map if we aren't using the default depth
        #         globalconf.default_cmap = xcb_generate_id(globalconf.connection);
        #         xcb_create_colormap(globalconf.connection, XCB_COLORMAP_ALLOC_NONE,
        #                 globalconf.default_cmap, globalconf.screen->root,
        #                 globalconf.visual->visual_id);
        #     }
        #
        # #ifdef WITH_XCB_ERRORS
        #     if (xcb_errors_context_new(globalconf.connection, &globalconf.errors_ctx) < 0)
        #         fatal("Failed to initialize xcb-errors");
        # #endif
        #
        #     /* Get a recent timestamp */
        #     acquire_timestamp();
        #
        #     /* Prefetch all the extensions we might need */
        #     xcb_prefetch_extension_data(globalconf.connection, &xcb_big_requests_id);
        #     xcb_prefetch_extension_data(globalconf.connection, &xcb_test_id);
        #     xcb_prefetch_extension_data(globalconf.connection, &xcb_randr_id);
        #     xcb_prefetch_extension_data(globalconf.connection, &xcb_xinerama_id);
        #     xcb_prefetch_extension_data(globalconf.connection, &xcb_shape_id);
        #     xcb_prefetch_extension_data(globalconf.connection, &xcb_xfixes_id);
        #
        #     if (xcb_cursor_context_new(globalconf.connection, globalconf.screen, &globalconf.cursor_ctx) < 0)
        #         fatal("Failed to initialize xcb-cursor");
        #     globalconf.xrmdb = xcb_xrm_database_from_default(globalconf.connection);
        #     if (globalconf.xrmdb == NULL)
        #         globalconf.xrmdb = xcb_xrm_database_from_string("");
        #     if (globalconf.xrmdb == NULL)
        #         fatal("Failed to initialize xcb-xrm");
        #
        #     /* Did we get some usable data from the above X11 setup? */
        #     draw_test_cairo_xcb();
        #
        #     /* Acquire the WM_Sn selection */
        #     acquire_WM_Sn(default_init_flags & INIT_FLAG_REPLACE_WM);
        #
        #     /* initialize dbus */
        #     a_dbus_init();
        #
        #     /* Get the file descriptor corresponding to the X connection */
        #     xfd = xcb_get_file_descriptor(globalconf.connection);
        #     GIOChannel *channel = g_io_channel_unix_new(xfd);
        #     g_io_add_watch(channel, G_IO_IN, a_xcb_io_cb, NULL);
        #     g_io_channel_unref(channel);
        #
        #     /* Grab server */
        #     xcb_grab_server(globalconf.connection);
        #
        #     {
        #         const uint32_t select_input_val = XCB_EVENT_MASK_SUBSTRUCTURE_REDIRECT;
        #         xcb_void_cookie_t cookie;
        #
        #         /* This causes an error if some other window manager is running */
        #         cookie = xcb_change_window_attributes_checked(globalconf.connection,
        #                                                       globalconf.screen->root,
        #                                                       XCB_CW_EVENT_MASK, &select_input_val);
        #         if (xcb_request_check(globalconf.connection, cookie))
        #             fatal("another window manager is already running (can't select SubstructureRedirect)");
        #     }
        #
        #     /* Prefetch the maximum request length */
        #     xcb_prefetch_maximum_request_length(globalconf.connection);
        #
        #     /* check for xtest extension */
        #     const xcb_query_extension_reply_t *query;
        #     query = xcb_get_extension_data(globalconf.connection, &xcb_test_id);
        #     globalconf.have_xtest = query && query->present;
        #
        #     /* check for shape extension */
        #     query = xcb_get_extension_data(globalconf.connection, &xcb_shape_id);
        #     globalconf.have_shape = query && query->present;
        #     if (globalconf.have_shape)
        #     {
        #         xcb_shape_query_version_reply_t *reply =
        #             xcb_shape_query_version_reply(globalconf.connection,
        #                     xcb_shape_query_version_unchecked(globalconf.connection),
        #                     NULL);
        #         globalconf.have_input_shape = reply && (reply->major_version > 1 ||
        #                 (reply->major_version == 1 && reply->minor_version >= 1));
        #         p_delete(&reply);
        #     }
        #
        #     /* check for xfixes extension */
        #     query = xcb_get_extension_data(globalconf.connection, &xcb_xfixes_id);
        #     globalconf.have_xfixes = query && query->present;
        #     if (globalconf.have_xfixes)
        #         xcb_discard_reply(globalconf.connection,
        #                 xcb_xfixes_query_version(globalconf.connection, 1, 0).sequence);
        #
        #     event_init();
        #
        #     /* Allocate the key symbols */
        #     globalconf.keysyms = xcb_key_symbols_alloc(globalconf.connection);
        #
        #     /* init atom cache */
        #     atoms_init(globalconf.connection);
        #
        #     ewmh_init();
        #     systray_init();
        #
        #     /* init spawn (sn) */
        #     spawn_init();
        #
        #     /* init xkb */
        #     xkb_init();
        #
        #     /* The default GC is just a newly created associated with a window with
        #      * depth globalconf.default_depth.
        #      * The window_no_focus is used for "nothing has the input focus". */
        #     globalconf.focus.window_no_focus = xcb_generate_id(globalconf.connection);
        #     globalconf.gc = xcb_generate_id(globalconf.connection);
        #     xcb_create_window(globalconf.connection, globalconf.default_depth,
        #                       globalconf.focus.window_no_focus, globalconf.screen->root,
        #                       -1, -1, 1, 1, 0,
        #                       XCB_COPY_FROM_PARENT, globalconf.visual->visual_id,
        #                       XCB_CW_BACK_PIXEL | XCB_CW_BORDER_PIXEL |
        #                       XCB_CW_OVERRIDE_REDIRECT | XCB_CW_COLORMAP,
        #                       (const uint32_t [])
        #                       {
        #                           globalconf.screen->black_pixel,
        #                           globalconf.screen->black_pixel,
        #                           1,
        #                           globalconf.default_cmap
        #                       });
        #     xwindow_set_class_instance(globalconf.focus.window_no_focus);
        #     xwindow_set_name_static(globalconf.focus.window_no_focus, "Awesome no input window");
        #     xcb_map_window(globalconf.connection, globalconf.focus.window_no_focus);
        #     xcb_create_gc(globalconf.connection, globalconf.gc, globalconf.focus.window_no_focus,
        #                   XCB_GC_FOREGROUND | XCB_GC_BACKGROUND,
        #                   (const uint32_t[]) { globalconf.screen->black_pixel, globalconf.screen->white_pixel });
        #
        #     /* Get the window tree associated to this screen */
        #     tree_c = xcb_query_tree_unchecked(globalconf.connection,
        #                                       globalconf.screen->root);
        #
        #     xcb_change_window_attributes(globalconf.connection,
        #                                  globalconf.screen->root,
        #                                  XCB_CW_EVENT_MASK,
        #                                  ROOT_WINDOW_EVENT_MASK);
        #
        #     /* we will receive events, stop grabbing server */
        #     xutil_ungrab_server(globalconf.connection);
        #
        #     /* get the current wallpaper, from now on we are informed when it changes */
        #     root_update_wallpaper();
        #
        #     /* init lua */
        #     luaA_init(&xdg, &searchpath);
        #     string_array_wipe(&searchpath);
        #     init_rng();
        #
        #     ewmh_init_lua();
        #
        #     /* Parse and run configuration file before adding the screens */
        #     if (globalconf.no_auto_screen)
        #     {
        #         /* Disable automatic screen creation, awful.screen has a fallback */
        #         globalconf.ignore_screens = true;
        #
        #         if(!luaA_parserc(&xdg, confpath))
        #             fatal("couldn't find any rc file");
        #     }
        #
        #     /* init screens information */
        #     screen_scan();
        #
        #     /* Parse and run configuration file after adding the screens */
        #     if (((!globalconf.no_auto_screen) && !luaA_parserc(&xdg, confpath)))
        #         fatal("couldn't find any rc file");
        #
        #     p_delete(&confpath);
        #
        #     xdgWipeHandle(&xdg);
        #
        #     /* Both screen scanning mode have this signal, it cannot be in screen_scan
        #        since the automatic screen generation don't have executed rc.lua yet. */
        #     screen_emit_scanned();
        #
        #     /* Exit if the user doesn't read the instructions properly */
        #     if (globalconf.no_auto_screen && !globalconf.screens.len)
        #         fatal("When -m/--screen is set to \"off\", you **must** create a "
        #               "screen object before or inside the screen \"scanned\" "
        #               " signal. Using AwesomeWM with no screen is **not supported**.");
        #
        #     client_emit_scanning();
        #
        #     /* scan existing windows */
        #     scan(tree_c);
        #
        #     client_emit_scanned();
        #
        #     luaA_emit_startup();
        #
        #     /* Setup the main context */
        #     g_main_context_set_poll_func(g_main_context_default(), &a_glib_poll);
        #     gettimeofday(&last_wakeup, NULL);
        #
        #     /* main event loop (if not NULL, awesome.quit() was already called) */
        #     if (globalconf.loop == NULL)
        #     {
        #         globalconf.loop = g_main_loop_new(NULL, FALSE);
        #         g_main_loop_run(globalconf.loop);
        #     }
        #     g_main_loop_unref(globalconf.loop);
        #     globalconf.loop = NULL;
        #
        #     awesome_atexit(false);

        return RET_OK_NONE


def _draw_find_visual(
        dll: Any,
        screen: defs.XcbScreenP, visual: defs.XcbVisualid,
) -> defs.XcbVisualtypeP:
    """Find the visual type for the screen."""
    print("getting allowed screen depths")
    depth_iter: defs.XcbDepthIterator = dll.xcb_screen_allowed_depths_iterator(screen)
    if depth_iter.value is not None:
        while depth_iter.rem != 0:
            print("Getting depth visuals")
            visual_iter: defs.XcbVisualtypeIterator = \
                dll.xcb_depth_visuals_iterator(depth_iter.data)
            while visual_iter.rem != 0:
                print("Found visual id " + repr(visual_iter.data.value.visual_id))
                if visual_iter.data.value.visual_id == visual:
                    return visual_iter.data
                print("Getting next visual type")
                dll.xcb_visualtype_next(ctypes.byref(visual_iter))
            print("getting next depth")
            dll.xcb_depth_next(ctypes.byref(depth_iter))
