import os

def clearDisplay():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")