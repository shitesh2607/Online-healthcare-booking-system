from selenium import webdriver
import pytest


# noinspection PyGlobalUndefined
from selenium.webdriver.common.by import By


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://127.0.0.1:8000/')
    assert driver.title == 'Doc Med'
    driver.find_element_by_xpath("//button[@class='button button1']").click()
    driver.find_element_by_xpath("//input[@name='username']").send_keys('pradeep')
    driver.find_element_by_xpath("//input[@name='password']").send_keys('iamthequeen')
    driver.find_element_by_xpath("//input[@type='submit']").click()
    assert driver.title == 'Doctor Dashboard'
    yield
    driver.close()
    driver.quit()
    print('Test Done')

def test_prescription(test_setup):
    driver.find_element(By.CSS_SELECTOR, ".wrapper_right").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > p").click()
    driver.find_element(By.CSS_SELECTOR, ".wrapper").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) > p").click()
    driver.find_element(By.CSS_SELECTOR, ".view_appointment td:nth-child(3)").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > p").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-outline-dark").click()
    driver.find_element(By.NAME, "symptom").click()
    driver.find_element(By.NAME, "symptom").send_keys("Lyme")
    driver.find_element(By.NAME, "medicine").click()
    driver.find_element(By.NAME, "medicine").send_keys("Penicillin")
    driver.find_element(By.NAME, "doctorFee").click()
    driver.find_element(By.NAME, "doctorFee").send_keys("200")
    driver.find_element(By.NAME, "medicineFee").click()
    driver.find_element(By.NAME, "medicineFee").send_keys("100")
    driver.find_element(By.NAME, "otherCharges").click()
    driver.find_element(By.NAME, "otherCharges").send_keys("50")
    driver.find_element(By.NAME, "submit").click()
    driver.find_element(By.CSS_SELECTOR, ".wrapper_right").click()
    driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(1) > #navbarDropdown").click()
    driver.find_element(By.CSS_SELECTOR, ".show > .dropdown-item:nth-child(3)").click()
    assert driver.title == 'Doc Med'
