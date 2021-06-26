from selenium import webdriver
import pytest


# noinspection PyGlobalUndefined
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://127.0.0.1:8000/')
    assert driver.title == 'Doc Med'
    driver.find_element_by_xpath("//button[@class='button button1']").click()
    driver.find_element_by_xpath("//input[@name='username']").send_keys('alex')
    driver.find_element_by_xpath("//input[@name='password']").send_keys('iamthequeen')
    driver.find_element_by_xpath("//input[@type='submit']").click()
    assert driver.title == 'Patient Dashboard'
    yield
    driver.close()
    driver.quit()
    print('Test Done')

def test_dashboard(test_setup):
    driver.find_element(By.NAME, "location").click()
    driver.find_element(By.NAME, "location").send_keys("Mumbai")
    driver.find_element(By.ID, "inputGroupSelect01").click()
    dropdown = driver.find_element(By.ID, "inputGroupSelect01")
    dropdown.find_element(By.XPATH, "//option[. = 'Physician']").click()
    driver.find_element(By.ID, "inputGroupSelect01").click()
    driver.find_element(By.NAME, "finddoc").click()
    driver.find_element(By.NAME, "location").click()
    driver.find_element(By.NAME, "location").send_keys("Mumbai")
    driver.find_element(By.ID, "inputGroupSelect01").click()
    dropdown = driver.find_element(By.ID, "inputGroupSelect01")
    dropdown.find_element(By.XPATH, "//option[. = 'Pediatrician']").click()
    driver.find_element(By.ID, "inputGroupSelect01").click()
    driver.find_element(By.NAME, "finddoc").click()
    driver.find_element(By.NAME, "location").click()
    driver.find_element(By.NAME, "location").send_keys("Mumbai")
    driver.find_element(By.ID, "inputGroupSelect01").click()
    dropdown = driver.find_element(By.ID, "inputGroupSelect01")
    dropdown.find_element(By.XPATH, "//option[. = 'Dermatologist']").click()
    driver.find_element(By.ID, "inputGroupSelect01").click()
    driver.find_element(By.NAME, "finddoc").click()
    driver.find_element(By.NAME, "location").click()
    driver.find_element(By.NAME, "location").send_keys("Delhi")
    driver.find_element(By.ID, "inputGroupSelect01").click()
    dropdown = driver.find_element(By.ID, "inputGroupSelect01")
    dropdown.find_element(By.XPATH, "//option[. = 'Neurologist']").click()
    driver.find_element(By.ID, "inputGroupSelect01").click()
    driver.find_element(By.NAME, "finddoc").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > p").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) > p").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > p").click()
    driver.find_element(By.CSS_SELECTOR, ".wrapper_left li:nth-child(2)").click()
    driver.find_element(By.NAME, "First_name").click()
    driver.find_element(By.NAME, "First_name").send_keys("Alex")
    driver.find_element(By.NAME, "Last_name").click()
    driver.find_element(By.NAME, "Last_name").send_keys("Turner")
    driver.find_element(By.NAME, "phone_number").click()
    driver.find_element(By.NAME, "phone_number").send_keys("8745961270")
    driver.find_element(By.NAME, "doctor").click()
    dropdown = driver.find_element(By.NAME, "doctor")
    dropdown.find_element(By.XPATH, "//option[. = 'Dr. Pradeep Shalvi']").click()
    driver.find_element(By.NAME, "doctor").click()
    driver.find_element(By.NAME, "message").click()
    driver.find_element(By.NAME, "message").send_keys("Skin Rashes")
    driver.find_element(By.NAME, "time").click()
    driver.find_element(By.NAME, "time").send_keys("12:40")
    date = driver.find_element_by_xpath("//input[@type='date']")
    driver.execute_script("arguments[0].setAttribute('value', '2021-06-19')", date)
    driver.find_element_by_name("appointment").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > p").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) > p").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > p").click()
    driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(1) > #navbarDropdown").click()
    driver.find_element(By.CSS_SELECTOR, ".show > .dropdown-item:nth-child(3)").click()
    assert driver.title == 'Doc Med'
