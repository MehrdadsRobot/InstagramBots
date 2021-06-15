from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class Captions:
    def __init__(self,driverPath,URL):
        self.path = driverPath
        self.url = URL
        driver = webdriver.Chrome(self.path)
    def Login(self,username,password):
        self.driver.get(self.url)
        Username = WebDriverWait(self.driver,8).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        Password = WebDriverWait(self.driver,8).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        try:
            Username.send_keys(username)
            Password.send_keys(password)
        except Exception as e:
            print("An Exception Occured",e)
        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        login.send_keys(Keys.RETURN)
    def getCaptions(self,cap_number):
        image = self.driver.find_element_by_class_name("_9AhH0")
        image.click()
        for i in range(0, cap_number):
            forward = self.driver.find_element_by_class_name("coreSpriteRightPaginationArrow")
            forward.click()
            time.sleep(6)
            capt = self.driver.find_element_by_class_name("C4VMK").text
            f = open(str(i) + ".txt", "a", encoding='UTF-16')
            f.write(capt)
            f.close()