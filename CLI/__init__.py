import os
import platform
import re
import time

from datetime import datetime
from typing import Any

_COLORS = {
    "PURPLE": "\033[95m",
    "BLUE": "\033[94m",
    "CYAN": "\033[96m",
    "SUCCESS": "\033[92m",
    "WARNING": "\033[93m",
    "FAIL": "\033[91m",
    "END": "\033[0m",
    "BOLD_": "\033[1m",
    "UNDERLINE_": "\033[4m",
}
_ALIASES = {
    "P": _COLORS["PURPLE"],
    "INFO": _COLORS["BLUE"],
    "I": _COLORS["BLUE"],
    "B": _COLORS["BLUE"],
    "C": _COLORS["CYAN"],
    "GREEN": _COLORS["SUCCESS"],
    "G": _COLORS["SUCCESS"],
    "S": _COLORS["SUCCESS"],
    "YELLOW": _COLORS["WARNING"],
    "Y": _COLORS["WARNING"],
    "W": _COLORS["WARNING"],
    "RED": _COLORS["FAIL"],
    "ERROR": _COLORS["FAIL"],
    "R": _COLORS["FAIL"],
    "F": _COLORS["FAIL"],
    "E": _COLORS["FAIL"],
    "BOLD": _COLORS["BOLD_"],
    "B_": _COLORS["BOLD_"],
    "UNDERLINE": _COLORS["UNDERLINE_"],
    "U_": _COLORS["UNDERLINE_"]
}

DISPLAY_WARNING = True


def clear_screen(delay: float = .5):
    time.sleep(delay)
    os.system('cls' if platform.system() == "Windows" else "clear")


def _replace_colors(colors: list[str], string: str, regx: list) -> str:
    """
    Replace a color name by the value corresponding in _COLORS or _ALIASES
    """
    _colors = []
    [_colors.append(_COLORS[c] if c in _COLORS else _ALIASES[c]) if c in _COLORS or c in _ALIASES else regx.remove(
        f"%{c}%") for c in colors]

    for i, v in enumerate(regx):
        string = string.replace(v, _colors[i])
    return string


def get_time(_format: str = "%H:%M:%S") -> str:
    """
    Get current time to log a message
    """
    now = datetime.now()
    return now.strftime(_format)


def replace_colors(string: str, regex: str = r"%\w+%") -> str:
    regx = re.findall(regex, string)
    return _replace_colors([c.split('%')[1].upper() for c in regx], string, regx)


def cprint(string: str, print_time: bool = False):
    """
    Just a colored print
    """
    print(f"{f'[{get_time()}] ' if print_time else ''}{replace_colors(_l(string) + '%END%')}")


def log_error(string: str, before: str = None, *args, **kwargs):
    """
    Print a red error message
    """
    cprint(f"{before if before else ''}%E%Error:%END% {string}", *args, **kwargs)


def log_info(string: str, before: str = None, *args, **kwargs):
    """
    Print a blue info message
    """
    cprint(f"{before if before else ''}%I%Info:%END% {string}", *args, **kwargs)


def log_warning(string: str, before: str = None, *args, **kwargs):
    """
    Print a yellow warning message
    """
    cprint(f"{before if before else ''}%w%Warning:%END% {string}", *args, **kwargs)


def log_success(string: str, before: str = None, *args, **kwargs):
    """
    Print a green success message
    """
    cprint(f"{before if before else ''}%S%Success:%END% {string}", *args, **kwargs)


try:
    import python_lang as lang

    _l = lang.get

    if os.path.exists("./CLIUtils/local"):
        [lang.add(f"CLIUtils/local/{file}", file[:2]) for file in os.listdir("CLIUtils/local/") if file.split('.')[-1] == "xml"]
    else:
        if DISPLAY_WARNING:
            log_warning("The local directory is not found. Create it in CLI/local for translation")


    def ls(code: str) -> bool:
        """
        Shortcut for lang.select() with security
        """
        try:
            return lang.select(code)
        except KeyError:
            if DISPLAY_WARNING:
                log_warning(f"{code}.xml is not found. Create it in CLIUtils/local/{code}.xml for translation")
            return False

    def lp(string: str):
        """
        Shortcut for print(lang.get())
        """
        print(_l(string))

except ModuleNotFoundError:
    _l = lambda x: x
    if DISPLAY_WARNING:
        log_warning("Translation are disabled because python-lang is missing. Try pip install python-lang or pip "
                    "install -r requirements.txt")

try:
    import questionary
    from questionary import Question

    q = questionary


    def qp(*args, **kwargs) -> Any:
        """
        Shortcut for questionary.path()
        """
        return q.path(*args, **kwargs)


    def qpa(*args, **kwargs) -> Question:
        """
        Shortcut for questionary.path().ask()
        """
        return qp(*args, **kwargs).ask()


    def qc(*args, **kwargs) -> Any:
        """
        Shortcut for questionary.confirm()
        """
        return q.confirm(*args, **kwargs)


    def qca(*args, **kwargs) -> Question:
        """
        Shortcut for questionary.confirm().ask()
        """
        return qc(*args, **kwargs).ask()


    def qt(*args, **kwargs) -> Any:
        """
        Shortcut for questionary.text()
        """
        return q.text(*args, **kwargs)


    def qta(*args, **kwargs) -> Question:
        """
        Shortcut for questionary.text().ask()
        """
        return qt(*args, **kwargs).ask()


    def qs(*args, **kwargs) -> Any:
        """
        Shortcut for questionary.select()
        """
        return q.select(*args, **kwargs)


    def qsa(*args, **kwargs) -> Question:
        """
        Shortcut for questionary.select().ask()
        """
        return qs(*args, **kwargs).ask()


    def qcheck(*args, **kwargs) -> Any:
        """
        Shortcut for questionary.checkbox()
        """
        return questionary.checkbox(*args, **kwargs)

    def qchecka(*args, **kwargs) -> Question:
        """
        Shortcut for questionary.checkbox().ask()
        """
        return qcheck(*args, **kwargs).ask()

    def qpass(*args, **kwargs) -> Any:
        """
        Shortcut for questionary.password()
        """
        return questionary.password(*args, **kwargs)

    def qpassa(*args, **kwargs) -> Question:
        """
        Shortcut for questionary.password().ask()
        """
        return qpass(*args, **kwargs).ask()
except ModuleNotFoundError:
    if DISPLAY_WARNING:
        log_warning("Questionary shortcuts are disabled because questionary is missing. Try pip install questionary "
                    "or pip install -r requirements.txt")