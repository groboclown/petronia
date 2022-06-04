#!/usr/bin/python3

# https://xcb.freedesktop.org/XmlXcb/
# About:
#   https://cgit.freedesktop.org/xcb/proto/plain/doc/xml-xcb.txt

from typing import Sequence, Dict, List, Tuple, Optional
import os
import sys
import subprocess
import tempfile
import shutil
import xml.dom.minidom


def pull_repo(outdir: str) -> int:
    try:
        subprocess.run([
            "git", "clone", "https://gitlab.freedesktop.org/xorg/proto/xcbproto.git", outdir,
        ], check=True)
        return 0
    except subprocess.CalledProcessError as err:
        return err.returncode


def find_xcb_src(src_dir: str) -> Sequence[str]:
    ret: List[str] = []
    basedir = os.path.join(src_dir, 'src')
    for fn in os.listdir(basedir):
        fqn = os.path.join(basedir, fn)
        if os.path.isfile(fqn) and fn.endswith('.xml'):
            ret.append(fqn)
    return ret


class FieldType:
    """Details about a field.  Not only the type, but also restrictions around it."""
    def __init__(self) -> None:
        self.name = ''
        self.count = 1  # 1 == A single value, > 1 a fixed array of these values, 0 == variable list
        self.min_val: Optional[int] = None
        self.max_val: Optional[int] = None


class Structure:
    """A structure"""
    def __init__(self) -> None:
        # list of entries, name, type
        self.name = ''
        self.records: List[Tuple[str, FieldType]] = []


class Call:
    """A call"""
    def __init__(self) -> None:
        self.name = ''
        self.args: List[Tuple[str, FieldType]] = []
        self.ret: Optional[FieldType] = None


class ProtoFile:
    """A structure."""
    def __init__(self) -> None:
        self.structures: Dict[str, Structure] = {}
        self.consts: Dict[str, int] = {}
        self.calls: Dict[str, Call] = {}


def parse_proto_file(filename: str) -> ProtoFile:
    pass


def main(args: Sequence[str]) -> int:
    if len(args) != 3 or '-h' in args or '--help' in args:
        print(f"Usage: {args[0]} (package name) (outdir)")
        return 0
    tmpdir = tempfile.mkdtemp()
    try:
        xcb_src = os.path.join(tmpdir, 'xcb')
        pull_repo(xcb_src)
        for src_file in find_xcb_src(xcb_src):
            pass
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
