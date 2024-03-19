from lib.game.screen import Screen

class CounterScreen(Screen):
    def __init__(self, app=None) -> None:
        super().__init__(app)

        self.count = 0

    def display(self) -> None:
        print(f"I am a counter, the current count is: {self.count}")

    def update(self) -> None:
        self.count += 1
        self.updated = True