from os import removedirs, startfile
from bs4 import BeautifulSoup
from selenium import webdriver    
import time
import pyautogui


def removecommas(number):
    newnumber = [i for i in number if not i == ","]
    return "".join(newnumber)

options = webdriver.ChromeOptions()
options.add_argument('--headless')

browser = webdriver.Chrome(options=options, executable_path="C:\Program Files (x86)\chromedriver.exe")
total =  100

browser.get("https://teamseas.org/")
pyautogui.press('t')
pyautogui.typewrite('/tp slipperee_slime ~ ~ ~ 180 65')
pyautogui.press('enter')


while True:


    time.sleep(2)
    html = browser.page_source
    soup = BeautifulSoup(html, features='lxml')

    numbers = soup.find('div', class_='container text-center')

    actualnumbers = numbers.h1.text
    print(actualnumbers)

    #browser.quit()

    #open



    with open('savenumbertome.txt', 'r') as file:  
        number = file.read()
    
    
    blocks = (int(removecommas(actualnumbers)) - (int(removecommas(number))))//100


    print(f'{actualnumbers} is the number now')
    print(f'{number} was the number')
    print(blocks)
    if int(removecommas(actualnumbers)) - 100 >= int(removecommas(number)):
        with open('savenumbertome.txt', 'w') as file:  
            file.write(actualnumbers)
    if blocks != 0:
        time.sleep(3)

        for i in range(blocks):
            
            pyautogui.leftClick()

            #add signplacement here
            #rightclick
            pyautogui.rightClick()
            #typewrite
            pyautogui.typewrite(f'{total} ')
            pyautogui.press('enter')
            pyautogui.typewrite(f'pounds removed')
            pyautogui.press('enter')
            pyautogui.typewrite(f'since start')
            pyautogui.press('enter')
            pyautogui.typewrite(f'of stream')
            total += 100
            #enter
            pyautogui.press('escape')


            #resume

            pyautogui.keyDown("w")
            time.sleep(0.2)
            
            pyautogui.keyUp("w")
            pyautogui.press('t')
            time.sleep(0.1)
            pyautogui.typewrite('/fill ~ ~-1 ~-1 ~ ~ ~-2 diamond_ore')
            pyautogui.press('enter')
            time.sleep(1)
    else:
        pyautogui.press('t')
        pyautogui.typewrite(f'We currently have donated {actualnumbers} dollars to Team Seas.')
        pyautogui.press('enter')
        browser.refresh()
        time.sleep(3)
    