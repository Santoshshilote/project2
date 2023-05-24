from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
driver=webdriver.Chrome("C:\Program Files\chromedriver\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(10)
#forgot password
FOr_link=driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
FOr_link.click()
time.sleep(10)
#Username
Username=driver.find_element(By.XPATH,'//input[@placeholder="Username"]')
Username.send_keys("Admin")
time.sleep(5)
#Submit button
Sub_button=driver.find_element(By.XPATH,'//button[@type="submit"]')
Sub_button.click()
driver.close()


