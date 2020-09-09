import pyautogui
from time import sleep
from os import system
import sys

while True:
    print("press q to quit")
    print("press s to start")
    inp = input(">> ")
    if inp in ["q", "Q"]:
        system("cls")
        sys.exit()
    else:
        for i in range(0, 10):
            print(pyautogui.position())
            sleep(0.5)
            system("cls")