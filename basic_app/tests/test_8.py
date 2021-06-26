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

def test_prescription(test_setup):
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > p").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) > p").click()
    driver.find_element(By.CSS_SELECTOR, "td:nth-child(4)").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > p").click()
    driver.find_element(By.CSS_SELECTOR, ".button1").click()
    driver.implicitly_wait(1000)
