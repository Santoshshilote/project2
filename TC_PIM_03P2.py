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
#options
#Admin
Admin=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
Admin.click()
time.sleep(5)
#PIM
PIM=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
PIM.click()
time.sleep(5)
#Leave
Leave=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span')
Leave.click()
time.sleep(5)
#Time
Time=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a')
Time.click()
time.sleep(5)
#Recruitment
Req=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span')
Req.click()
time.sleep(5)
#My info
My_info=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a')
My_info.click()
time.sleep(5)
#Performance
Performance=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span')
Performance.click()
time.sleep(5)
#Dashboard
Dash=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span')
Dash.click()
time.sleep(5)
#Directory
Directory=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span')
Directory.click()
time.sleep(5)
#Maintance
Maintaince=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span')
Maintaince.click()
#Administrator access
time.sleep(10)
password=driver.find_element(By.XPATH,'//input[@name="password"]')
password.send_keys("admin123")
conf_cl=driver.find_element(By.XPATH,'//button[@type="submit"]')
conf_cl.click()
time.sleep(5)
#Buzz
Buzz=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span')
Buzz.click()

driver.close()