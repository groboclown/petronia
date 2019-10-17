
"""
Parsing up the initial configuration.

Note that extension configuration should be handled separately, because that
requires structured definitions.
"""

from typing import Dict, Mapping, Iterable, Optional, Tuple, Union, overload
import configparser
from ....base.util import (
    readonly_dict,
    STRING_EMPTY_TUPLE,
    EMPTY_TUPLE,
)


def create_ini_config() -> configparser.ConfigParser:
    """
    Standard configuration.
    """
    ret = configparser.ConfigParser(
        interpolation=configparser.ExtendedInterpolation()
    )
    return ret


def load_ini_config_from_file(filename: str) -> configparser.ConfigParser:
    """Trivial helper."""
    ret = create_ini_config()
    ret.read(filename)
    return ret


def load_ini_config_from_text(contents: str) -> configparser.ConfigParser:
    """Trivial helper."""
    ret = create_ini_config()
    ret.read_string(contents)
    return ret


class LayeredConfig:
    """
    A ConfigParser style construct that allows for:

    * A lowest level dictionary of section -> key,val mappings
        for built-in values.
    * An ordered list of ConfigParser objects.  If the top level
        provides a section, then none of the others are checked.
        So, last one wins.

    The boolean translation of the config parsers is ignored, and a custom one
    is used instead.

    The config parser value replacement is only used within the context of its
    own file.  It doesn't reach outside into the other config files passed in,
    in order to follow the rule of least surprises.

    The default section of the config parsers is only used for the value
    replacement.
    """
    __slots__ = ('_sections',)
    _sections: Mapping[str, Mapping[str, str]]

    def __init__(
            self,
            defaults: Dict[str, Dict[str, str]],
            configs: Iterable[configparser.ConfigParser],
            overlap: bool = False
    ) -> None:
        sections: Dict[str, Dict[str, str]] = {}
        cfgs = list(configs)
        cfgs.reverse()
        for cfg in cfgs:
            for sec in cfg.sections():
                if sec not in sections:
                    sections[sec] = _extract_options(cfg, sec)
                elif overlap:
                    for key, val in _extract_options(cfg, sec).items():
                        sections[sec][key] = val
        for sec, opts in defaults.items():
            if sec not in sections:
                sections[sec] = opts
            elif overlap:
                # FIXME this is a bug.  "cfg" is the wrong variable here.
                for key, val in _extract_options(cfg, sec).items():
                    sections[sec][key] = val
        # TODO each section's options needs to be made read-only.
        self._sections = readonly_dict(sections)

    def sections(self) -> Iterable[str]:
        return self._sections.keys()

    def has_section(self, name: str) -> bool:
        return name in self._sections

    def options(self, section: str) -> Iterable[str]:
        if section in self._sections:
            return self._sections.keys()
        return STRING_EMPTY_TUPLE

    def has_option(self, section: str, option: str) -> bool:
        return option in self.options(section)

    def get(
            self, section: str, option: str, fallback: Optional[str] = None
    ) -> Optional[str]:
        if section in self._sections:
            sec = self._sections[section]
            if option in sec:
                return sec[option]
        return fallback

    def getint(
        self, section: str, option: str, fallback: Optional[int] = None
    ) -> Optional[int]:
        if section in self._sections:
            sec = self._sections[section]
            if option in sec:
                return int(sec[option])
        return fallback

    def getfloat(
        self, section: str, option: str, fallback: Optional[float] = None
    ) -> Optional[float]:
        if section in self._sections:
            sec = self._sections[section]
            if option in sec:
                return float(sec[option])
        return fallback

    def getboolean(
        self, section: str, option: str, fallback: Optional[bool] = None
    ) -> Optional[bool]:
        val = self.get(section, option, None)
        if val is None:
            return fallback
        lval = val.lower()
        if lval in ('1', 'yes', 'true', 'on',):
            return True
        if lval in ('0', 'no', 'false', 'off',):
            return False
        raise ValueError(val)

    @overload
    def items(self) -> Iterable[Tuple[str, Iterable[Tuple[str, str]]]]: ...
    @overload
    def items(self, section: str) -> Iterable[Tuple[str, str]]: ...

    def items(
            self,
            section: Optional[str] = None
    ) -> Iterable[Union[
        Tuple[str, Iterable[Tuple[str, str]]],
        Tuple[str, str],
    ]]:
        if section is None:
            for name, opts in self._sections.items():
                yield (name, opts.items(),)
        elif section in self._sections:
            return self._sections[section].items()
        else:
            return EMPTY_TUPLE # type: ignore


def _extract_options(config: configparser.ConfigParser, section: str) -> Dict[str, str]:
    ret: Dict[str, str] = {}
    for opt in config.options(section):
        ret[opt] = config.get(section, opt)
    return ret
