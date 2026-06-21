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
    time.sleep(2)
    yield driver  # Yielding the driver instance
    driver.quit()

@pytest.fixture
def take_screenshot(userprofile, request):
    """Fixture to capture a screenshot at specific points in the test."""
    driver = userprofile
    test_name = request.node.name
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshots_dir = r"D:\HPB_Testcase\screenshots/Trends"

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
            screenshots_dir = r"D:\HPB_Testcase\screenshots/Trends"
            os.makedirs(screenshots_dir, exist_ok=True)
            file_name = f"{test_name}_failed_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(file_path)
            print(f"Screenshot for failed test saved at {file_path}")


def test_Trends_page(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "//a[@id='Trends']").click()
    time.sleep(3)
    take_screenshot()

def test_Clinical_Wellness_Score(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, "(//span[contains(text(),'Clinical')])[2]").text
    assert element == "Clinical"
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_Refresh_Trends(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "//img[contains(@src,'./assets/images/refresh.png')]").click()
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_Navigating_Lifestyle_Wellness_Score(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "//span[contains(text(),'Lifestyle')]").click()
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_Lifestyle_Wellness_Score(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, "(//span[normalize-space()='lifestyle'])[1]").text
    assert element == "lifestyle"
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_Comparison_button(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "//button[@class='filter-button']").click()
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_Comparison_Clinical_Parameter(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "//div[@class='dropdown-main ng-star-inserted']//div[1]").click()
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_Enable_Hba1c_Parameter(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[2]").click()
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_Enable_HDL_Cholesterol_Parameter(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[3]").click()
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_Comparison_Lifestyle_Parameter(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "//div[contains(@class,'dropdown-main ng-star-inserted')]//div[2]").click()
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_Enable_Steps_Parameter(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[2]").click()
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_Enable_MVPA_Parameters(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[3]").click()
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_Blood_Pressure(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, "//span[contains(@class,'card-title-history')][normalize-space()='Blood Pressure']").text
    assert element == "Blood Pressure"
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_Steps(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, "//span[normalize-space()='Steps']").text
    assert element == "Steps"
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_MVPA(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, "(//span[normalize-space()='Moderate Vigorous Physical Activity'])[1]").text
    assert element == "Moderate Vigorous Physical Activity"
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_HbA1c(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, "//span[@class='card-title-history'][normalize-space()='HbA1c']").text
    assert element == "HbA1c"
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_HDL_Cholestrol(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, "//span[normalize-space()='Lipids-HDL Cholestrol']").text
    assert element == "Lipids-HDL Cholestrol"
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_Disable_HbA1c_Parameter(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "(//span[@class='card-title-history'][normalize-space()='HbA1c'])[1]").click()
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_Disable_Steps_Parameter(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-profile/div[1]/div[2]/div/app-history/div[1]/div[3]/div[2]/app-blood-pressure-wheel-parameters/div[2]/div/div[1]/hpb-steps-rate/div/div/div/div[1]/span[2]").click()
    time.sleep(2)
    take_screenshot()
    time.sleep(2)


