#Import All the Prerequisites And Libraries
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import random
# drpath variable is for giving the driver path
drpath = "C:\Program Files (x86)\chromedriver.exe"
#paths that code tries to reach
paths = ['https://www.instagram.com/']
# This is the name of the Page
keyword = "example"
driver = webdriver.Chrome(drpath)
try:
    driver.get(paths[0])
    time.sleep(5)

except:
    print('Url Not Found')

username = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
password = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))
username.send_keys("<ENTER YOUR USERNAME>") #here insert your username
password.send_keys("<ENTER YOUR PASSWORD>") #and here your password
login = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']")))
login.send_keys(Keys.RETURN)
notnow = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Not Now')]")))
notnow.send_keys(Keys.RETURN)
notnow2 = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Not Now')]")))
notnow2.send_keys(Keys.RETURN)

driver.get("https://www.instagram.com/"+keyword+"/followers/")
driver.find_element_by_partial_link_text("follower").click()
pop_up_window = WebDriverWait(
    driver, 2).until(EC.element_to_be_clickable(
    (By.XPATH, "//div[@class='isgrP']")))

writer = open("followers.csv", "a", encoding='UTF-16')
tes = []
x = 0
while x<20:
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
      pop_up_window)
    z = driver.find_elements_by_class_name('notranslate')
    for f in z:
        tes.append(f.text)
    time.sleep(random.randint(2, 10))
    x = x+1

tes = list(set(tes))
for i in tes:
    writer.write(str(i)+'\n')
