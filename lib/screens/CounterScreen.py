from lib.utils import AppStatus
from lib.game.screen import Screen

class CounterScreen(Screen):
    def __init__(self, app=None) -> None:
        super().__init__(app)

        self.count = 0

    def display(self) -> None:
        print(f"I am a counter, the current count is: {self.count}")

    def controlsHandler(self, key: str) -> None:
        if key == "q":
            self.app.status = AppStatus.Terminated
        
        if key == "u":
            self.update()

    def update(self) -> None:
        super().update()
        self.count += 1