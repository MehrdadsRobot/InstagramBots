from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import random

drpath = "C:\Program Files (x86)\chromedriver.exe"
paths = ['https://www.instagram.com/']
driver2 = webdriver.Chrome(drpath)
try:
    driver2.get(paths[0])
    time.sleep(5)
except:
    print('Url Not Found')
    pass

username = WebDriverWait(driver2,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
password = WebDriverWait(driver2,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))
username.send_keys("<ENTER YOUR USERNAME>") #here insert your username
password.send_keys("<ENTER YOUR PASSWORD>") #and here your password
login = WebDriverWait(driver2,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']")))
login.send_keys(Keys.RETURN)
notnow = WebDriverWait(driver2,5).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Not Now')]")))
notnow.send_keys(Keys.RETURN)
notnow2 = WebDriverWait(driver2,5).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Not Now')]")))
notnow2.send_keys(Keys.RETURN)

####NOTE####
#Give the followers.txt outputfile to the open method.it is designed to increase the pace.
file = open('followers.csv','r')
bio = ''
bios = []
writer2 = open("Bios.csv", "a", encoding='UTF-16')
# Use The followers.txt or followers.csv to get the respective Url.
for user in file:
    user2 = user.replace('\x00','')
    try:
        driver2.get(paths[0] + str(user2) + '/')

    except:
        pass
    try:
        time.sleep(2)
        bio = driver2.find_element_by_xpath("//div[contains(@class, '-vDIg')]/span").text
        bios.append(str(bio))

    except:
        pass

    time.sleep(random.randint(2,8))

for i in bios:
    writer2.write(i + '\n')