from enum import Enum, StrEnum

class BgColor(StrEnum):
    WHITE = "white"
    BLACK = "black"

class AppStatus(Enum):
    Terminated = -1
    Sleeping = 0
    Running = 1