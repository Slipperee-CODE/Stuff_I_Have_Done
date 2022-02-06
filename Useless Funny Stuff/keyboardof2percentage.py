from re import A, U
import keyboard, pyautogui, string, time

keycount = -1
alphabet_string = string.ascii_lowercase
thekeys = list(alphabet_string)
#print(thekeys)

while True:
    if keyboard.is_pressed("shift"):
        pyautogui.press("backspace")
        if keycount == 26:
            keycount = -1
        keycount += 1
        pyautogui.press(thekeys[keycount])
        time.sleep(0.1)
    elif keyboard.is_pressed("control"):
        pyautogui.press(thekeys[keycount])
        keycount = -1
        time.sleep(0.1)
    elif keyboard.is_pressed("escape"):
        break
