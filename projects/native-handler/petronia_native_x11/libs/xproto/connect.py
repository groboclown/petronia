"""
Low-level X Protocol interaction.
"""

from typing import Tuple, Sequence, Optional, Any
import os
import sys
import socket
import struct
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.util import i18n as _
from petronia_native.common import user_messages


UNIX_SOCKET_PREFIX = (
    '/tmp/.X11-unix/X',
    '/usr/spool/sockets/X11/',
    '/var/tsol/doors/.X11-unix/X',
)
DEFAULT_DISPLAY_STR = ':0'
DISPLAY_ENV_NAME = 'DISPLAY'
X_TCP_PORT = 6000


class XConnection:
    """Interaction with the X server."""
    __slots__ = ('__conn',)

    def __init__(self, conn_fd: int) -> None:
        self.__conn: Optional[int] = conn_fd

    def send_struct(self, struct_format: str, data: Sequence[Any]) -> StdRet[None]:
        """Sends the structure using the struct pack formatted data"""
        if self.__conn is None:
            return StdRet.pass_errmsg(
                user_messages.TRANSLATION_CATALOG,
                _('Connection closed'),
            )
        res = struct.pack(self.__endian + struct_format, *data)
        os.write(self.__conn, res)
        return RET_OK_NONE

    def close(self) -> None:
        if self.__conn is not None:
            os.close(self.__conn)
            self.__conn = None


def xserver_connect(connection_str: Optional[str]) -> StdRet[XConnection]:
    """Connect to the x server."""
    fd_res = create_xserver_fd_screen(connection_str)
    if fd_res.has_error:
        return fd_res.forward()
    xfd, screen = fd_res.result
    conn = XConnection(xfd)

    try:
        # First byte: endianness
        if sys.byteorder.lower() == 'little':
            os.write(xfd, b'l')  # 154 == ascii lowercase l == least significant byte first
        else:
            os.write(xfd, b'B')  # 102 == ascii uppercase B == most significant byte first
    except OSError as err:
        os.close(xfd)
        return StdRet.pass_exception(
            user_messages.TRANSLATION_CATALOG,
            _('Failed to complete X server handshake: {exception}'),
            exception=err,
        )

    return StdRet.pass_ok(XConnection())


def handshake(conn: XConnection) -> StdRet[None]:

    #         write_setup(c, auth_info) &&
    #         read_setup(c) &&
    #         _xcb_ext_init(c) &&
    #         _xcb_xid_init(c)
    pass


def create_xserver_fd_screen(connection_str: Optional[str]) -> StdRet[Tuple[int, int]]:
    """Open a connection to the X server; returns the file descriptor, screen."""
    if connection_str is None:
        connection_str = os.environ.get(DISPLAY_ENV_NAME, DEFAULT_DISPLAY_STR).strip()
    display_str = connection_str
    protocol = 'none'
    host: Optional[str] = None
    display = 0
    screen = 0
    try:
        if os.path.exists(display_str):
            protocol = 'unix'
            host = display_str
        else:
            pos_p = display_str.rfind('.')
            if pos_p > 0 and os.path.exists(display_str[:pos_p]):
                # Unix socket
                screen = int(display_str[pos_p + 1:])
                protocol = 'unix'
                host = display_str[:pos_p]
            else:
                pos_s = display_str.find('/')
                if pos_s > 0:
                    protocol = display_str[:pos_s]
                    display_str = display_str[pos_s + 1:]
                    pos_p = display_str.rfind('.')
                pos_c = display_str.find(':')
                if pos_c < 0 or pos_c > pos_p:
                    raise ValueError
                if pos_c > 0:
                    host = display_str[:pos_c]
                    protocol = 'tcp'
                if pos_p > 0:
                    display = int(display_str[pos_c + 1:pos_p])
                    screen = int(display_str[pos_p + 1:])
                else:
                    display = int(display_str[pos_c + 1:])
                    screen = 0
    except ValueError:
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('invalid display {connection}'),
            connection=connection_str,
        )

    if protocol == 'none' and sys.platform.lower() not in ('windows',):
        for prefix in UNIX_SOCKET_PREFIX:
            socket_path = f'{prefix}{display}'
            if os.path.exists(socket_path):
                host = socket_path
                protocol = 'unix'
                break

    if protocol == 'unix':
        return create_xserver_unix(host, screen)
    if protocol in ('none', 'tcp', 'inet', 'inet6'):
        if host is None:
            host = 'localhost'
        return create_xserver_socket(protocol, host, display, screen)

    return StdRet.pass_errmsg(
        user_messages.TRANSLATION_CATALOG,
        _('invalid display {connection}'),
        connection=connection_str,
    )


def create_xserver_unix(socket_path: str, screen: int) -> StdRet[Tuple[int, int]]:
    """Open the unix socket."""
    try:
        sock = socket.socket(family=socket.AF_UNIX, type=socket.SOCK_STREAM, proto=0)
        raw_data = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        buffer_size, = struct.unpack('!i', raw_data)
        if buffer_size < 64 * 1024:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 64 * 1024)
        sock.connect(socket_path)
        sock.setblocking(False)
        ret_fd = sock.detach()
        try:
            # TODO should this be done for TCP/IP sockets, too?
            import fcntl
            fcntl.fcntl(ret_fd, fcntl.F_SETFD, fcntl.FD_CLOEXEC)
        except (ModuleNotFoundError, OSError):
            pass
        return StdRet.pass_ok((ret_fd, screen))
    except Exception as err:
        return StdRet.pass_exception(
            user_messages.TRANSLATION_CATALOG,
            _('Failed to connect to {socket_path}: {exception}'),
            exception=err,
            socket_path=socket_path,
        )


def create_xserver_socket(
        protocol: str, hostname: str, display: int, screen: int,
) -> StdRet[Tuple[int, int]]:
    """Create a TCP/IP socket to the X server."""
    try:
        sock = socket.socket(
            family=(
                socket.AF_INET6 if protocol == 'inet6'
                else socket.AF_INET
            ),
            type=socket.SOCK_STREAM,
            proto=0,
        )
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        sock.connect((hostname, display + X_TCP_PORT))
        sock.setblocking(False)
        ret_fd = sock.detach()
        return StdRet.pass_ok((ret_fd, screen))
    except Exception as err:
        return StdRet.pass_exception(
            user_messages.TRANSLATION_CATALOG,
            _('Failed to connect to {hostname}:{display}: {exception}'),
            exception=err,
            hostname=hostname,
            display=display,
        )
