from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import csv,codecs,random,pandas as pd
drpath = "C:\Program Files (x86)\chromedriver.exe"
paths = ['https://www.instagram.com/']
driver = webdriver.Chrome(drpath)
try:
    driver.get(paths[0])
    time.sleep(5)
except:
    print('Url Not Found')
    pass
#this chunk of code is for the login process
username = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
password = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))
username.send_keys("<ENTER YOUR USERNAME>")
password.send_keys("<ENTER YOUR PASSWORD>")
login = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']")))
login.send_keys(Keys.RETURN)
notnow = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Not Now')]")))
notnow.send_keys(Keys.RETURN)
notnow2 = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Not Now')]")))
notnow2.send_keys(Keys.RETURN)
keyword = 'example'
driver.get("https://www.instagram.com/"+keyword+"/")
writer = open("temps.csv", "a", encoding='UTF-16')
writerpr = open("Likers.csv", "a", encoding='UTF-16')
tes = []
links = []
postlinks = []
pop_up_window = WebDriverWait(
    driver, 2).until(EC.element_to_be_clickable(
    (By.XPATH, "//div[@class='v9tJq AAaSh ']")))

x = 0
while x<2:
    links.append(driver.find_elements_by_tag_name('a'))
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(random.randint(2,6))
    #driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
     #                     pop_up_window)
    x = x+1

for i in links:
    for j in i:
        try:
            refs = j.get_attribute('href')
        except:
            pass
        if "/p/" in str(refs):
          postlinks.append(str(refs))

for link in postlinks:
    driver.get(link)
    time.sleep(random.randint(2,5))
    try:
        likes = driver.find_element_by_partial_link_text("like")
        print(likes)
        likes.click()
        time.sleep(random.randint(1,3))
        #tic = str(likes.get_attribute('href')).replace('liked_by/','')

    except:
        pass
    x=0
    try:
        pop_up_window = WebDriverWait(
            driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@style='height: 356px; overflow: hidden auto;']")))
    except:
        print("its not found")
        pass
    while x < 5 :
        try:
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                              pop_up_window)
            z = driver.find_elements_by_class_name('notranslate')
        except:
            pass

        for f in z:
            try:
                tes.append(f.text)
            except:
                pass
        x = x + 1
        time.sleep(random.randint(2,7))
    tes = list(set(tes))
    for i in tes:
        writer.write(i + '\n')
    time.sleep(random.randint(2, 7))

setter=codecs.open("followers.csv","rb","utf-16")
csvread=csv.reader(setter,delimiter=',')
settes = list(set(csvread))
for s in settes:
    writerpr.write(i + '\n')