from selenium import webdriver
import pytest


# noinspection PyGlobalUndefined
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://127.0.0.1:8000/')
    assert driver.title == 'Doc Med'
    yield
    driver.close()
    driver.quit()
    print('Test Done')

def test_invalidusername(test_setup):
    driver.find_element_by_xpath("//button[@class='button button1']").click()
    driver.find_element_by_xpath("//input[@name='username']").send_keys('alexahere')
    driver.find_element_by_xpath("//input[@name='password']").send_keys('iamthequeen')
    driver.find_element_by_xpath("//input[@type='submit']").click()
    assert driver.title == 'Login!'

def test_invalidpassword(test_setup):
    driver.find_element_by_xpath("//button[@class='button button1']").click()
    driver.find_element_by_xpath("//input[@name='username']").send_keys('alex')
    driver.find_element_by_xpath("//input[@name='password']").send_keys('iamalexan')
    driver.find_element_by_xpath("//input[@type='submit']").click()
    assert driver.title == 'Login!'

def test_login(test_setup):
    driver.find_element_by_xpath("//button[@class='button button1']").click()
    driver.find_element_by_xpath("//input[@name='username']").send_keys('gautam')
    driver.find_element_by_xpath("//input[@name='password']").send_keys('iamthequeen')
    driver.find_element_by_xpath("//input[@type='submit']").click()
    assert driver.title == 'Patient Dashboard'
