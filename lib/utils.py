from enum import Enum

class AppStatus(Enum):
    Terminated = -1
    Sleeping = 0
    Running = 1