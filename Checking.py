import pytest
import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os
from datetime import datetime



driver = webdriver.Chrome()
driver.maximize_window()
file_path = r"D:\userinfo\login info.xlsx"
df = pd.read_excel(file_path)
url = df.iloc[0, 1]
org_userid = df.iloc[1, 1]
org_pass = df.iloc[1, 2]
driver.get(url)
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//div[@class='login-form']//div[1]//label[1]").send_keys(org_userid)
driver.find_element(By.XPATH, "//div[@class='divisions']//div[2]//label[1]//input[1]").send_keys(org_pass)
driver.find_element(By.XPATH, "//input[@value='Sign In']").click()
time.sleep(5)
otp = df.iloc[1, 3]
driver.find_element(By.XPATH, "//input[@id='inp']").send_keys(otp)
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
time.sleep(5)


# driver.find_element(By.XPATH,"//span[normalize-space()='Organisation (W+)']").click()
# driver.find_element(By.XPATH, "//*[@id='admin']/ul/li[2]").click()
time.sleep(2)

time.sleep(1)




fake = Faker()
global facility_name
facility_name = fake.name()
facility_address = fake.address()
driver.find_element(By.XPATH, "//button[normalize-space()='+ Add New Facility']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@id='edit-department']//div[@class='content-body']//div[1]//label[1]//input[1]").send_keys(facility_name)
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[2]/div[1]/div/div/div/div/"
                             "app-facility-operations/div/div[2]/div/form/div[2]/label/input").send_keys(facility_address)
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[2]/div[1]/div/div/div/div/"
                             "app-facility-operations/div/div[2]/div/form/div[3]/div").click()
time.sleep(3)

time.sleep(4)



fake = Faker()
global department_name
department_name = fake.name()
driver.find_element(By.XPATH,"//button[normalize-space()='+ Add New Department']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='close-dept']//div//label[@class='inp']//input[@id='inp']").send_keys(department_name)
driver.find_element(By.XPATH, "//img[@src='./assets/images/downarrow.png']").click()
facility_names = driver.find_elements(By.XPATH,"//*[@id='edit-department']/div/div/div/div/app-department-operations/div/div[2]/div/form/div[1]/div/div/div[2]/div/div/ul/li")
for p_facility_name in facility_names:
    if p_facility_name.text == facility_name:
        p_facility_name.click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='next-btn'][normalize-space()='Add']").click()
time.sleep(3)

time.sleep(7)
driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-organization-view/div[1]/div[1]/img").click()
time.sleep(4)


driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(department_name)
time.sleep(2)




driver.find_element(By.XPATH, "//tr[@class='facility-row']")
time.sleep(2)
driver.find_element(By.XPATH, "//img[@class='collapse-btn']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//tbody/tr[2]/td[4]/div/img[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@id='all-departMent']//div[@class='left-wrap']//div[1]//label[1]//span[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='modal-body']//div//app-assign-dept-list//button[@class='success-btn'][normalize-space()='Confirm']").click()
time.sleep(3)

time.sleep(7)
driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-organization-view/div[1]/div[1]/img").click()
time.sleep(4)


driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(department_name)
time.sleep(2)
driver.find_element(By.XPATH, "//img[@class='collapse-btn']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//img[@data-target='#all-departMent']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@id='all-departMent']//div[@class='left-wrap']//div[1]//label[1]//span[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='modal-body']//div//app-assign-dept-list//button[@class='success-btn'][normalize-space()='Confirm']").click()
time.sleep(3)

time.sleep(7)
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[1]/div[1]/img").click()
time.sleep(4)



fake = Faker()
global edepartment_name
edepartment_name = fake.name()
driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(facility_name)
time.sleep(2)
driver.find_element(By.XPATH, "//img[@class='collapse-btn']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//tbody/tr[2]/td[4]/div[1]/img[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[2]/div[1]/div/div/div/div/app-department-operations/div/div[2]/div/form/div[1]/label/input").clear()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[2]/div[1]/div/div/div/div/app-department-operations/div/div[2]/div/form/div[1]/label/input").send_keys(edepartment_name)
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[2]/div[1]/div/div/div/div/app-department-operations/div/div[2]/div/form/div[2]/div/div/div/img").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[2]/div[1]/div/div/div/div/app-department-operations/div/div[2]/div/form/div[2]/div/div/ul/li[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[2]/div[1]/div/div/div/div/app-department-operations/div/div[2]/div/form/div[3]/div").click()
time.sleep(3)

time.sleep(7)
driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-organization-view/div[1]/div[1]/img").click()
time.sleep(4)


driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(edepartment_name)
time.sleep(2)
driver.find_element(By.XPATH, "//img[@class='collapse-btn']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//tbody/tr[2]/td[4]/div[1]/img[3]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[4]/div/div/div/div/div[3]/button[2]").click()
time.sleep(3)

time.sleep(7)
driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-organization-view/div[1]/div[1]/img").click()
time.sleep(4)


driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
time.sleep(2)



driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(facility_name)
time.sleep(2)



time.sleep(2)
driver.find_element(By.XPATH, "//img[@src='./assets/images/assign.png']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='all-facility']//div[@class='left-wrap']//div[1]//label[1]//span[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[10]/div[1]/div/div/div/div/app-assign-facility-list/div/div[4]/button").click()
time.sleep(3)

time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-organization-view/div[1]/div[1]/img").click()
time.sleep(4)


driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(facility_name)
time.sleep(2)
driver.find_element(By.XPATH, "//img[@src='./assets/images/assign.png']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='all-facility']//div[@class='left-wrap']//div[1]//label[1]//span[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[10]/div[1]/div/div/div/div/app-assign-facility-list/div/div[4]/button").click()
time.sleep(3)

time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-organization-view/div[1]/div[1]/img").click()
time.sleep(4)


driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(facility_name)
time.sleep(2)
driver.find_element(By.XPATH,"//tbody/tr[1]/td[4]/div/img[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[2]/div[1]/div/div/div/div/app-facility-operations/div/div[2]/div/form/div[1]/label/input").clear()
time.sleep(2)
fake = Faker()
global efacility_name
efacility_name = fake.name()
facility_address = fake.address()
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[2]/div[1]/div/div/div/div/app-facility-operations/div/div[2]/div/form/div[1]/label/input").send_keys(efacility_name)
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[2]/div[1]/div/div/div/div/app-facility-operations/div/div[2]/div/form/div[2]/label/input").clear()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[2]/div[1]/div/div/div/div/app-facility-operations/div/div[2]/div/form/div[2]/label/input").send_keys(facility_address)
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[2]/div[1]/div/div/div/div/app-facility-operations/div/div[2]/div/form/div[3]/div").click()
time.sleep(3)

time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-organization-view/div[1]/div[1]/img").click()
time.sleep(4)


driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(efacility_name)
time.sleep(2)
driver.find_element(By.XPATH,"//img[@src='./assets/images/delete.png']").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-organization-view/div[3]/div/div/div/div/div[3]/button[2]").click()
time.sleep(3)

time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-organization-view/div[1]/div[1]/img").click()
time.sleep(4)

