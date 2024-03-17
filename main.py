from pynput.keyboard import Controller, Key

from lib.game.app import ASCIImon

if __name__ == "__main__":
    app = ASCIImon()
    app.run()

    c = Controller()
    c.press(Key.esc)
    c.release(Key.esc)