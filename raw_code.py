import os
import pandas as pd
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from datetime import datetime


driver = webdriver.Chrome()
driver.maximize_window()
file_path = r"D:\HPB_Testcase\logindetails\login info.xlsx"
df = pd.read_excel(file_path)
url = df.iloc[0, 1]
stm1_userid = df.iloc[4, 1]
stm1_pass = df.iloc[4, 2]
otp = df.iloc[4, 3]
user = df.iloc[10, 1]
driver.get(url)
driver.implicitly_wait(100)
driver.find_element(By.XPATH, "//div[@class='login-form']//div[1]//label[1]").send_keys(stm1_userid)
driver.find_element(By.XPATH, "//div[@class='divisions']//div[2]//label[1]//input[1]").send_keys(stm1_pass)
driver.find_element(By.XPATH, "//input[@value='Sign In']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='inp']").send_keys(otp)
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(user)
driver.find_element(By.XPATH, "//div[@class='p-element blurry-text']").click()
time.sleep(3)


"""Wellness PLan"""
driver.find_element(By.XPATH, "//a[@id='Wellness Plan']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Generate Plan']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//label[normalize-space()='High-normal blood pressure']//span[@class='checkmark']").click()
driver.find_element(By.XPATH, "//label[normalize-space()='High-normal blood pressure']//span[@class='checkmark']").click()
driver.find_element(By.XPATH, "//div[@class='checkbox-group']//div[@class='checkbox-container']//div[1]//label[1]//span[1]").click()
driver.find_element(By.XPATH, "//div[@class='checkbox-group']//div[@class='checkbox-container']//div[1]//label[1]//span[1]").click()
driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']//div[1]//div[1]//div[1]//label[1]//span[1]").click()
driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']//div[1]//div[1]//div[1]//label[1]//span[1]").click()
time.sleep(2)
assessment_date = str(datetime.now().day)
driver.find_element(By.XPATH, "//input[@placeholder='Select date']").send_keys(assessment_date)
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Sign Off & Share']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Confirm']").click()
time.sleep(7)



# driver.find_element(By.XPATH, "").click()
# driver.find_element(By.XPATH, "").click()
# driver.find_element(By.XPATH, "").click()
# driver.find_element(By.XPATH, "").click()
# driver.find_element(By.XPATH, "").click()
# driver.find_element(By.XPATH, "").click()
# driver.find_element(By.XPATH, "").click()
# driver.find_element(By.XPATH, "").click()
# driver.find_element(By.XPATH, "").click()