import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import pandas as pd
import os
from datetime import datetime

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
    user = df.iloc[10, 1]
    driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(user)
    driver.find_element(By.XPATH,"//div[@class='p-element blurry-text']").click()
    time.sleep(3)
    yield driver  # Yielding the driver instance
    time.sleep(5)
    driver.quit()

@pytest.fixture
def take_screenshot(userprofile, request):
    """Fixture to capture a screenshot at specific points in the test."""
    driver = userprofile
    test_name = request.node.name
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshots_dir = r"D:\HPB_Testcase\screenshots/Patients_Logs"

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
            screenshots_dir = r"D:\HPB_Testcase\screenshots/Patients_Logs"
            os.makedirs(screenshots_dir, exist_ok=True)
            file_name = f"{test_name}_failed_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(file_path)
            print(f"Screenshot for failed test saved at {file_path}")


def test_patients_logs_page(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, f"//a[@id='Patient Logs']").text
    assert element == "Patient Logs"
    time.sleep(2)
    take_screenshot()
    time.sleep(1)

def test_Avg_Systolic_Clinic_Blood_Pressure(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, f"//div[normalize-space()='Avg. Systolic (Clinic)']").text
    assert element == "Avg. Systolic (Clinic)"
    time.sleep(2)
    take_screenshot()
    time.sleep(1)

def test_Avg_Diastolic_Clinic_Blood_Pressure(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, f"//div[normalize-space()='Avg. Diastolic (Clinic)']").text
    assert element == "Avg. Diastolic (Clinic)"
    time.sleep(2)
    take_screenshot()
    time.sleep(1)

def test_Avg_Systolic_Self_Record_Blood_Pressure(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, f"//div[normalize-space()='Avg. Systolic (Self-Record)']").text
    assert element == "Avg. Systolic (Self-Record)"
    time.sleep(2)
    take_screenshot()
    time.sleep(1)

def test_Avg_Diastolic_Self_Record_Blood_Pressure(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, f"//div[normalize-space()='Avg. Diastolic (Self-Record)']").text
    assert element == "Avg. Diastolic (Self-Record)"
    time.sleep(2)
    take_screenshot()
    time.sleep(1)

def test_Refresh(userprofile, take_screenshot):
    driver = userprofile
    driver.find_element(By.XPATH, "//img[@src='./assets/images/refresh.png']").click()
    time.sleep(2)
    take_screenshot()
    time.sleep(2)

def test_Fasting_Blood_Glucose(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, f"(//div[contains(text(),'Fasting Blood Glucose')])[1]").text
    assert element == "Fasting Blood Glucose"
    time.sleep(2)
    take_screenshot()
    time.sleep(1)

def test_Hba1c(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, f"//div[normalize-space()='Hba1c']").text
    assert element == "Hba1c"
    time.sleep(2)
    take_screenshot()
    time.sleep(1)

def test_Weight(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, f"(//span[@class='heart-rate-type'][normalize-space()='Weight'])[1]").text
    assert element == "Weight"
    time.sleep(2)
    take_screenshot()
    time.sleep(1)

def test_BMI(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, f"//span[@class='heart-rate-type'][normalize-space()='BMI']").text
    assert element == "BMI"
    time.sleep(2)
    take_screenshot()
    time.sleep(1)

def test_Waist_Circumference(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, f"//div[normalize-space()='Waist Circumference']").text
    assert element == "Waist Circumference"
    time.sleep(2)
    take_screenshot()
    time.sleep(1)

def test_Lipids(userprofile, take_screenshot):
    driver = userprofile
    element = driver.find_element(By.XPATH, f"//div[normalize-space()='Lipids']").text
    assert element == "Lipids"
    time.sleep(2)
    take_screenshot()
    time.sleep(1)

def test_bmi_calculation(userprofile, take_screenshot):
    driver = userprofile
    bmi_element = driver.find_element(By.XPATH, "//div[@id='profile-bmi']/p[2]").text
    weight_element = driver.find_element(By.XPATH, "//p[@id='user-weight']").text
    height_element = driver.find_element(By.XPATH, "//p[@id='user-height']").text
    if bmi_element == "--":
        assert bmi_element == weight_element and bmi_element == height_element
    else:
        bmi = float(bmi_element)
        weight = float(weight_element.split()[0])
        height = float(height_element.split()[0])
        height = height / 100
        bmi_calculation = weight / (height ** 2)
        bmi_calculation = round(bmi_calculation, 2)
        assert bmi_calculation == bmi
        time.sleep(2)
        take_screenshot()
        time.sleep(1)

