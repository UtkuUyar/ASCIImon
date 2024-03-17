from collections import namedtuple

ScreenContext = namedtuple("ScreenContext", ["name", "screen"])

class Screen:
    def __init__(self, app=None) -> None:
        self.app = app
        self.updated = True

class EmptyStackException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = "The stack is empty!"

class ScreenContextStack:
    def __init__(self) -> None:
        self.contexts = []

    def push(self, key: str, s: Screen) -> None:
        self.contexts.append(ScreenContext(key, s))

    def top(self) -> ScreenContext:
        if len(self.contexts) == 0:
            raise EmptyStackException()
        
        return self.contexts[-1]
    
    def pop(self, ret=True) -> ScreenContext:
        if len(self.contexts) == 0:
            raise EmptyStackException()
        
        context = self.contexts.pop(-1)
        if ret:
            return context

class MainScreen(Screen):
    def __init__(self, app=None) -> None:
        super().__init__(app)

    def display(self) -> None:
        pass

class CounterScreen(Screen):
    def __init__(self, app=None) -> None:
        super().__init__(app)

        self.count = 0

    def display(self) -> None:
        print(f"I am a counter, the current count is: {self.count}")

    def update(self) -> None:
        self.count += 1
        self.updated = True