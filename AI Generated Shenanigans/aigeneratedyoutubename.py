import time
from selenium import webdriver
from transformers import pipeline
generator = pipeline('text-generation',model='EleutherAI/gpt-neo-2.7B')


PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://youtube.com")

time.sleep(3)


searchbar = driver.find_element_by_name('search_query')
  
searchbar.send_keys('minecraft')
searchbar.submit()





listofchannelnames = []
channelnames = driver.find_elements_by_xpath('//*[@id="channel-info"]')
print(channelnames)
for i in channelnames:
    listofchannelnames.append(i.text)


listofchannelnames.pop(0)
print(listofchannelnames)
with open('ayoutubernames.txt',"w") as file:
    for i in listofchannelnames:
        file.write(i + '\n')




with open('ayoutubernames.txt','r') as file:
    readfile = file.read()
    result = generator(readfile,max_length=250, do_sample = True, temperature = 0.9)

with open("aiyoutubernames.txt", "w") as file:  
    file.write(result[0]['generated_text'])

driver.quit()
