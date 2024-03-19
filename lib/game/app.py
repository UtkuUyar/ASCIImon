import threading
from pynput import keyboard

from lib.utils import AppStatus

from lib.game import screen, display
from lib.screens.CounterScreen import CounterScreen
from lib.screens.MainScreen import MainScreen


class ASCIImon:
    def __init__(self, resolution = (151, 40)):
        self.screen_contexts = screen.ScreenContextStack()
        self.screen_contexts.push("main", CounterScreen(app=self))

        self.status = AppStatus.Running
        self.resolution = resolution

    @property
    def current_screen(self):
        return self.screen_contexts.top().screen

    def __displayThreadHandler(self):
        while True:
            if self.status == AppStatus.Terminated:
                break

            if self.status == AppStatus.Running and self.current_screen.updated:
                # Very lazy implementation of a stateful screen
                display.clearDisplay()
                self.current_screen.display()
                self.current_screen.updated = False
    
    def __keyPressHandler(self, key: keyboard.Key):
        if self.status != AppStatus.Running:
            return
        
        try:
            kstr = key.char
        except:
            kstr = key.name

        self.current_screen.controlsHandler(kstr)
    
    def run(self):
        display_thread = threading.Thread(
            target=self.__displayThreadHandler,
            args=tuple()    
        )

        event_thread = keyboard.Listener(
            on_press=self.__keyPressHandler
        )

        display.setResolution(*self.resolution)

        display_thread.start()
        event_thread.start()

        display_thread.join()

        display.clearDisplay()