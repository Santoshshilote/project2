from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
driver=webdriver.Chrome("C:\Program Files\chromedriver\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()
time.sleep(15)

#username Admin
username=driver.find_element(By.XPATH,"//input[@name='username']")
username.send_keys("Admin")

#password Admin123
password=driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys("admin123")

#login_btn
login_btn=driver.find_element(By.XPATH,"//button[@type='submit']")
login_btn.click()
time.sleep(10)
#Title of the page
print(driver.title)

#admin page
time.sleep(10)
admin_page=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
admin_page.click()
time.sleep(10)
driver.close()

