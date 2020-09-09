import pyautogui
import autopy
from os import system
import sys

def main():
    while True:
        # pyautogui.FAILSAFE = False
        print("enter how many times you want to wite crackhead to eugene")
        n = int(input(">> "))
        if n > 50:
            print("are you sure?")
            inp = input(">> ")
            if inp in ["yes", "YES", "Yes", "y", "y"]:
                # print("enter how fast you want it to be")
                # print("fastest : 0.01")
                # f = input(">> ")
                autopy.mouse.move(431,921)
                pyautogui.click()
                for i in range(0, n):
                    # autopy.mouse.move(431,921)
                    # pyautogui.move(431, 921)
                    # pyautogui.click()
                    pyautogui.write("crackhead",interval = 0.01)
                    pyautogui.press("enter")
            else:
                system("Cls")
                print("exiting")
                sys.exit()
        else:
            autopy.mouse.move(431,921)
            pyautogui.click()
            for i in range(0, n):
                # autopy.mouse.move(431,921)
                # pyautogui.move(431, 921)
                # pyautogui.click()
                pyautogui.write("crackhead",interval = 0.01)
                pyautogui.press("enter")

if __name__ == "__main__":
    main(