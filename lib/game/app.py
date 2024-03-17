import threading
from enum import Enum
from pynput import keyboard

from lib.display import utils as disutils
from lib.game import screens

class AppStatus(Enum):
    Terminated = -1
    Sleeping = 0
    Running = 1


class ASCIImon:
    def __init__(self):
        self.screen_contexts = screens.ScreenContextStack()
        self.screen_contexts.push("main", screens.CounterScreen(app=self))

        self.status = AppStatus.Running

    @property
    def current_screen(self):
        return self.screen_contexts.top().screen

    def __displayThreadHandler(self):
        while True:
            if self.status == AppStatus.Terminated:
                break

            if self.status == AppStatus.Running and self.current_screen.updated:
                # Very lazy implementation of a stateful screen
                disutils.clearDisplay()
                self.current_screen.display()
                self.current_screen.updated = False
    
    def __keyPressHandler(self, key: keyboard.Key):
        if self.status != AppStatus.Running:
            return
        
        try:
            kstr = key.char
        except:
            kstr = key.name

        if kstr == "q":
            self.status = AppStatus.Terminated
        
        if kstr == "u":
            self.current_screen.update()
    
    def run(self):
        display_thread = threading.Thread(
            target=self.__displayThreadHandler,
            args=tuple()    
        )

        event_thread = keyboard.Listener(
            on_press=self.__keyPressHandler
        )

        display_thread.start()
        event_thread.start()

        display_thread.join()

        disutils.clearDisplay()