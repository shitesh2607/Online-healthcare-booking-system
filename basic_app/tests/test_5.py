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

def test_dashboard(test_setup):
    driver.find_element(By.CSS_SELECTOR, ".wrapper_left li:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) > p").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > p").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > p").click()
    driver.find_element(By.NAME, "full_name").click()
    driver.find_element(By.NAME, "full_name").send_keys("Dr. Pradeep Shalvi")
    driver.find_element(By.NAME, "phone_number").click()
    driver.find_element(By.NAME, "phone_number").send_keys("1855544414")
    driver.find_element(By.NAME, "speciality").click()
    dropdown = driver.find_element(By.NAME, "speciality")
    dropdown.find_element(By.XPATH, "//option[. = 'Dermatologist']").click()
    driver.find_element(By.NAME, "speciality").click()
    driver.find_element(By.NAME, "qualification").click()
    driver.find_element(By.NAME, "qualification").send_keys("MD")
    driver.find_element(By.NAME, "location").click()
    driver.find_element(By.NAME, "location").send_keys("Mumbai")
    driver.find_element(By.NAME, "hospital_name").click()
    driver.find_element(By.NAME, "hospital_name").click()
    driver.find_element(By.NAME, "hospital_name").send_keys("Seven Hills Hospital")
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(9)").click()
    driver.find_element(By.NAME, "phone_number").clear()
    driver.find_element(By.NAME, "phone_number").send_keys("8855544414")
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(9)").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > p").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) > p").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > p").click()
    driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(1) > #navbarDropdown").click()
    driver.find_element(By.CSS_SELECTOR, ".show > .dropdown-item:nth-child(3)").click()
    assert driver.title == 'Doc Med'
