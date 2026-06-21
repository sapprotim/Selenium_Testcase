import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import pandas as pd
import os
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="module")
def userprofile():
    driver = webdriver.Chrome()
    driver.maximize_window()
    file_path = r"D:\HPB_Testcase\logindetails\login info.xlsx"
    df = pd.read_excel(file_path)
    url = df.iloc[0, 1]
    stm1_userid = df.iloc[4, 1]
    stm1_pass = df.iloc[4, 2]
    otp = df.iloc[4, 3]
    driver.get(url)
    driver.implicitly_wait(100)
    driver.find_element(By.XPATH, "//div[@class='login-form']//div[1]//label[1]").send_keys(stm1_userid)
    driver.find_element(By.XPATH, "//div[@class='divisions']//div[2]//label[1]//input[1]").send_keys(stm1_pass)
    driver.find_element(By.XPATH, "//input[@value='Sign In']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='inp']").send_keys(otp)
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    time.sleep(5)
    user = df.iloc[10, 1]
    driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(user)
    driver.find_element(By.XPATH,"//div[@class='p-element blurry-text']").click()
    yield driver  # Yielding the driver instance
    driver.quit()

@pytest.fixture
def take_screenshot(userprofile, request):
    """Fixture to capture a screenshot at specific points in the test."""
    driver = userprofile
    test_name = request.node.name
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshots_dir = r"D:\HPB_Testcase\screenshots\wellness_plan"

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
        driver = item.funcargs.get('userprofile')
        if driver:
            test_name = item.name
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            screenshots_dir = r"D:\HPB_Testcase\screenshots\wellness_plan"
            os.makedirs(screenshots_dir, exist_ok=True)
            file_name = f"{test_name}_failed_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(file_path)
            print(f"Screenshot for failed test saved at {file_path}")


def test_wellness_plan_page(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "//a[@id='Wellness Plan']").click()
    take_screenshot()
    time.sleep(2)

def test_generate_plan_page(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "//button[normalize-space()='Generate Plan']").click()
    time.sleep(2)
    take_screenshot()

def test_patient_condition_question(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "//label[normalize-space()='High-normal blood pressure']//span[@class='checkmark']").click()
    driver.find_element(By.XPATH, "//label[normalize-space()='High-normal blood pressure']//span[@class='checkmark']").click()
    take_screenshot()

def test_patient_condition_question_2(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "//div[@class='checkbox-group']//div[@class='checkbox-container']//div[1]//label[1]//span[1]").click()
    take_screenshot()

def test_patient_condition_question_3(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']//div[1]//div[1]//div[1]//label[1]//span[1]").click()
    time.sleep(2)
    take_screenshot()

def test_patient_assessment_date(userprofile, take_screenshot):
    driver = userprofile
    assessment_date = str(datetime.now().day)
    driver.find_element(By.XPATH, "//input[@placeholder='Select date']").send_keys(assessment_date)
    time.sleep(2)
    take_screenshot()

def test_Sign_download_pdf(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign Off & Share']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[normalize-space()='Confirm']").click()
    time.sleep(2)
    take_screenshot()