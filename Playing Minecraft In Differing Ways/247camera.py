import cv2
from pytesseract import pytesseract
import os
import pyautogui
import pygetwindow
import time
pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

framenumber = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 32:
        # ESC pressed
        print("Escape hit, closing...")
        break
    
    framenumber += 1
    if framenumber == 30:
        #cv2.imwrite("tempframe.png",frame)
        #img = cv2.imread("tempframe.png")
        grayimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blackandwhite = cv2.adaptiveThreshold(grayimg, 225, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,81,20)
        wordsinimage = pytesseract.image_to_string(blackandwhite, lang='eng', config='--psm 10')
        allwordslist = [i for i in wordsinimage.split("\n") if i != "\x0c" ]

        print(allwordslist)
        for i in allwordslist:
            print(i)
            for letter in i:
                print(letter)
                if letter == "W":
                    #pygetwindow.getWindowsWithTitle('Lunar Client (1.8.9-44c40d4/master)')[0].maximize()
                    #pyautogui.press("escape")
                    pyautogui.keyDown("w")
                else:
                    pyautogui.keyUp("w")
                if letter == "S":
                    pyautogui.keyDown("s")
                else:
                    pyautogui.keyUp("s")
                if letter == "A":
                    pyautogui.keyDown("a")
                else:
                    pyautogui.keyUp("a")
                if letter == "D":
                    pyautogui.keyDown("d")
                else:
                    pyautogui.keyUp("d")
                if letter == "M":
                    pyautogui.moveRel(25,0, duration=0.25)
                if letter == "O" or letter == "0":
                    pyautogui.moveRel(-25,0, duration=0.25)
                if letter == "L":
                    pyautogui.leftClick()
                if letter == "R":
                    pyautogui.rightClick()
                    
        framenumber = 0

cam.release()

cv2.destroyAllWindows()