

import ctypes

# typedef uint8_t xcb_keycode_t;
xcb_keycode_t = ctypes.c_uint8
# typedef uint32_t xcb_window_t;
xcb_window_t = ctypes.c_uint32
# typedef uint32_t xcb_colormap_t;
xcb_colormap_t = ctypes.c_uint32
# typedef uint32_t xcb_visualid_t;
xcb_visualid_t = ctypes.c_uint32


# noinspection PyPep8Naming
class xcb_setup_t(ctypes.Structure):
    _fields_ = [
        # uint8_t 	status
        ("status", ctypes.c_uint8),
        # uint8_t 	pad0
        ("pad0", ctypes.c_uint8),
        # uint16_t 	protocol_major_version
        ("protocol_major_version", ctypes.c_uint16),
        # uint16_t 	protocol_minor_version
        ("protocol_minor_version", ctypes.c_uint16),
        # uint16_t 	length
        ("length", ctypes.c_uint16),
        # uint32_t 	release_number
        ("release_number", ctypes.c_uint32),
        # uint32_t 	resource_id_base
        ("resource_id_base", ctypes.c_uint32),
        # uint32_t 	resource_id_mask
        ("resource_id_mask", ctypes.c_uint32),
        # uint32_t 	motion_buffer_size
        ("motion_buffer_size", ctypes.c_uint32),
        # uint16_t 	vendor_len
        ("vendor_len", ctypes.c_uint16),
        # uint16_t 	maximum_request_length
        ("maximum_request_length", ctypes.c_uint16),
        # uint8_t 	roots_len
        ("roots_len", ctypes.c_uint8),
        # uint8_t 	pixmap_formats_len
        ("pixmap_formats_len", ctypes.c_uint8),
        # uint8_t 	image_byte_order
        ("image_byte_order", ctypes.c_uint8),
        # uint8_t 	bitmap_format_bit_order
        ("bitmap_format_bit_order", ctypes.c_uint8),
        # uint8_t 	bitmap_format_scanline_unit
        ("bitmap_format_scanline_unit", ctypes.c_uint8),
        # uint8_t 	bitmap_format_scanline_pad
        ("bitmap_format_scanline_pad", ctypes.c_uint8),
        # xcb_keycode_t 	min_keycode
        ("min_keycode", xcb_keycode_t),
        # xcb_keycode_t 	max_keycode
        ("max_keycode", xcb_keycode_t),
        # uint8_t 	pad1 [4]
        ("pad1_0", ctypes.c_uint8),
        ("pad1_1", ctypes.c_uint8),
        ("pad1_2", ctypes.c_uint8),
        ("pad1_3", ctypes.c_uint8),
    ]


# noinspection PyPep8Naming
class xcb_screen_t(ctypes.Structure):
    _fields_ = [
        # xcb_window_t   root;
        ('root', xcb_window_t),
        # xcb_colormap_t default_colormap;
        ('default_colormap', xcb_colormap_t),
        # uint32_t       white_pixel;
        ('white_pixel', ctypes.c_uint32),
        # uint32_t       black_pixel;
        ('black_pixel', ctypes.c_uint32),
        # uint32_t       current_input_masks;
        ('current_input_masks', ctypes.c_uint32),
        # uint16_t       width_in_pixels;
        ('width_in_pixels', ctypes.c_uint16),
        # uint16_t       height_in_pixels;
        ('height_in_pixels', ctypes.c_uint16),
        # uint16_t       width_in_millimeters;
        ('width_in_millimeters', ctypes.c_uint16),
        # uint16_t       height_in_millimeters;
        ('height_in_millimeters', ctypes.c_uint16),
        # uint16_t       min_installed_maps;
        ('min_installed_maps', ctypes.c_uint16),
        # uint16_t       max_installed_maps;
        ('max_installed_maps', ctypes.c_uint16),
        # xcb_visualid_t root_visual;
        ('root_visual', xcb_visualid_t),
        # uint8_t        backing_stores;
        ('backing_stores', ctypes.c_uint8),
        # uint8_t        save_unders;
        ('save_unders', ctypes.c_uint8),
        # uint8_t        root_depth;
        ('root_depth', ctypes.c_uint8),
        # uint8_t        allowed_depths_len;
        ('allowed_depths_len', ctypes.c_uint8),
    ]


# noinspection PyPep8Naming
class xcb_screen_iterator_t(ctypes.Structure):
    _fields_ = [
        # xcb_screen_t *data;
        ('data', ctypes.POINTER(xcb_screen_t)),
        # int rem;
        ('rem', ctypes.c_int),
        # int index;
        ('index', ctypes.c_int),
    ]
