from bs4 import BeautifulSoup
from selenium import webdriver    
import time
import pyautogui



#options = webdriver.ChromeOptions()
#options.add_argument('--headless')

browser = webdriver.Chrome(options=None, executable_path="C:\Program Files (x86)\chromedriver.exe")
#options


pathtochat = input("Link to Chat : ")

browser.get(pathtochat)
lenoflistlasttime = 0
while True:

    thatmessagelistselenium = browser.find_elements_by_xpath("//span[@class='text-fragment']")
    thatmessagelist = [i.text for i in thatmessagelistselenium]
    

    for index,i in enumerate(thatmessagelist[lenoflistlasttime:]):
        for wordindex,word in enumerate(i.split()):
            if "forward" in word:
                pyautogui.keyDown("w")
                time.sleep(0.2)
                pyautogui.keyUp("w")
                #test if works tmr
            elif "leftclick" in word:
                pyautogui.leftClick()
            elif "rightclick" in word:
                pyautogui.rightClick()
            elif "space" in word:
                pyautogui.keyDown("space")
                time.sleep(0.2)
                pyautogui.keyUp("space")
            elif "mouseright" in word:
                pyautogui.moveRel(25,0, duration=0.25)
            elif "mouseleft" in word:
                pyautogui.moveRel(-25,0, duration=0.25)
            elif "mouseup" in word:
                pyautogui.moveRel(0,-25, duration=0.25)
            elif "mousedown" in word:
                pyautogui.moveRel(0,25, duration=0.25)
            elif "leftclick" in word:
                pyautogui.leftClick()
            elif "rightclick" in word:
                pyautogui.rightClick()
            else:
                print(f"WOO I DETECTED THE MESSAGE {i}")
            #ADD IN SPACEJUMP AND MULTIPLYING MOVEMENT
    lenoflistlasttime = len(thatmessagelist)
    time.sleep(0.1)

