
import speech_recognition as sr
import pyautogui

running = True

r = sr.Recognizer()
with sr.Microphone() as source:
    while running:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            for index,word in enumerate(text.split()):
                print(word)
                if word == "space":
                    pyautogui.keyDown("space")
                else:
                    pyautogui.keyUp("space")
                if word == "forward":
                    pyautogui.keyDown("w")
                else:
                    pyautogui.keyUp("w")
                if word == "backward":
                    pyautogui.keyDown("s")
                else:
                    pyautogui.keyUp("s")
                if word == "mouse" or word == "Mouse":
                    if text.split()[index+1] == "right":
                        pyautogui.moveRel(25,0, duration=0.25)
                    if text.split()[index+1] == "left":
                        pyautogui.moveRel(-25,0, duration=0.25)
                    if text.split()[index+1] == "up":
                        pyautogui.moveRel(0,-25, duration=0.25)
                    if text.split()[index+1] == "down":
                        pyautogui.moveRel(0,25, duration=0.25)
                else:
                    if word == "left" and text.split()[index-1] != "mouse" or "Mouse":
                        pyautogui.keyDown("a")
                    else:
                        pyautogui.keyUp("a")
                    if word == "right" and text.split()[index-1] != "mouse" or "Mouse":
                        pyautogui.keyDown("d")
                    else:
                        pyautogui.keyUp("d")

                if word == "left-click":
                    pyautogui.leftClick()
                if word == "right-click":
                    pyautogui.rightClick()
                if word == "stop":
                    running = False
        except Exception:
            print("Sorry could not recognize what you said")
print("Program Ended") 
      