import os
import os

SYSTEM = os.name


def clearDisplay():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def setResolution(cols = 151, lines = 22):
    if os.name == "nt":
        os.system(f"mode con: cols={cols} lines={lines}")
    else:
        os.system(f"printf '\\033[8;{lines};{cols}t'")

def setFullscreen():
    if os.name == "nt":
        os.system("mode con: cols=9999 lines=9999")
    else:
        os.system("printf '\\033[8;9999;9999t'")

    return os.get_terminal_size()