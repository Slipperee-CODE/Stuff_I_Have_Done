from os import replace
import pyautogui,time

with open('othercommands.txt') as f:
    lines = f.read()

allstuff = lines.split("\n")




time.sleep(10)
for i in allstuff:
    pyautogui.press('t')
    pyautogui.typewrite(i)
    pyautogui.press('enter')
