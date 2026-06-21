import pytest
import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os
from datetime import datetime



@pytest.fixture(scope="module")
def org_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    file_path = r"D:\HPB_Testcase\logindetails\login info.xlsx"
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
    yield driver  # Yielding the driver instance
    time.sleep(5)
    driver.quit()


@pytest.fixture
def take_screenshot(org_login, request):
    """Fixture to capture a screenshot at specific points in the test."""
    driver = org_login
    test_name = request.node.name
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshots_dir = r"D:\HPB_Testcase\screenshots/Invite_user"

    os.makedirs(screenshots_dir, exist_ok=True)

    def _screenshot():
        file_name = f"{test_name}_{timestamp}.png"
        file_path = os.path.join(screenshots_dir, file_name)
        driver.save_screenshot(file_path)
        print(f"Screenshot saved at {file_path}")

    return _screenshot


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture a screenshot if a test fails."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get('org_login')
        if driver:
            test_name = item.name
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            screenshots_dir = r"D:\HPB_Testcase\screenshots/Invite_user"
            os.makedirs(screenshots_dir, exist_ok=True)
            file_name = f"{test_name}_failed_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(file_path)
            print(f"Screenshot for failed test saved at {file_path}")

def test_invite_User_ORG(org_login, take_screenshot):
    driver = org_login
    fake = Faker()
    first_name = fake.first_name()
    last_name= fake.last_name()
    email =  fake.email()
    random_number = fake.random_number(digits=7)
    if len(str(random_number)) == 6:
        extra_digit = fake.phone_number(digits=1)
        phone = str(random_number) + str(extra_digit)
        phone = "6" + phone
    else:
        phone = "6" + str(random_number)
    driver.find_element(By.XPATH, "//span[normalize-space()='Organisation (W+)']").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Users']").click()
    driver.find_element(By.XPATH, "//a[@routerlink='/users']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-all-patients/div[1]/div[1]/div[1]").click()
    driver.find_element(By.XPATH,"//input[@formcontrolname='firstName']").send_keys(first_name)
    driver.find_element(By.XPATH,"//input[@formcontrolname='lastName']").send_keys(last_name)
    driver.find_element(By.XPATH,"//body[1]/app-root[1]/div[3]/app-all-patients[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/div[3]/label[1]/input[1]").send_keys(email)
    driver.find_element(By.XPATH, "//input[@id='phone']").clear()
    driver.find_element(By.XPATH,"//input[@id='phone']").send_keys(phone)
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='add-patient']/div/div/div/div/div[2]/div[2]/form/div[1]/div[2]/div[5]/div[2]/label[3]").click() #Email & SMS
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/downarrow.png']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//li[normalize-space()='Basic']").click()
    driver.find_element(By.XPATH, "//div[contains(text(),'Send Invitation')]").click()
    time.sleep(3)
    take_screenshot()
    time.sleep(1)
    time.sleep(1)
