import time
from selenium import webdriver
from transformers import pipeline
generator = pipeline('text-generation',model='EleutherAI/gpt-neo-2.7B')

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options, executable_path="C:\Program Files (x86)\chromedriver.exe")


driver.get("https://youtube.com")

time.sleep(3)


searchbar = driver.find_element_by_name('search_query')
  
searchbar.send_keys('minecraft')
searchbar.submit()

listofvideotitles = []
videoTitles = driver.find_elements_by_xpath('//*[@id="video-title"]')
print(videoTitles)
for i in videoTitles:
    listofvideotitles.append(i.text)


listofvideotitles.pop(0)
print(listofvideotitles)
with open('youtubetitles.txt',"w") as file:
    for i in listofvideotitles:
        file.write(i + '\n')




with open('youtubetitles.txt','r') as file:
    readfile = file.read()
    result = generator(readfile,max_length=1000, do_sample = True, temperature = 0.9)

with open("youtubetitlesbyai.txt", "w") as file:  
    file.write(result[0]['generated_text'])

driver.quit()