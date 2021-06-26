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
    driver.find_element(By.CSS_SELECTOR, ".button2").click()
    driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(3) > .button").click()
    yield
    driver.close()
    driver.quit()
    print('Test Done')

def test_invalidusername(test_setup):
    driver.find_element(By.ID, "id_username").click()
    driver.find_element(By.ID, "id_username").send_keys("gautam")
    driver.find_element(By.ID, "id_password1").click()
    driver.find_element(By.ID, "id_password1").send_keys("iamthequeen")
    driver.find_element(By.ID, "id_password2").click()
    driver.find_element(By.ID, "id_password2").send_keys("iamthequeen")
    driver.find_element(By.ID, "id_first_name").click()
    driver.find_element(By.ID, "id_first_name").send_keys("Dr. Gautam")
    driver.find_element(By.ID, "id_last_name").click()
    driver.find_element(By.ID, "id_last_name").send_keys("Chauhan")
    driver.find_element(By.ID, "id_email").click()
    driver.find_element(By.ID, "id_email").send_keys("gautam@gmail.com")
    driver.find_element(By.ID, "id_phone_number").click()
    driver.find_element(By.ID, "id_phone_number").send_keys("8745961270")
    driver.find_element(By.ID, "id_speciality").click()
    driver.find_element(By.ID, "id_speciality").send_keys("Pediatrician")
    driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    assert driver.title == 'Doctor SignUp!'

def test_differentpassword(test_setup):
    driver.find_element(By.ID, "id_username").click()
    driver.find_element(By.ID, "id_username").send_keys("pradeep")
    driver.find_element(By.ID, "id_password1").click()
    driver.find_element(By.ID, "id_password1").send_keys("iamtheking")
    driver.find_element(By.ID, "id_password2").click()
    driver.find_element(By.ID, "id_password2").send_keys("iamthequeen")
    driver.find_element(By.ID, "id_first_name").click()
    driver.find_element(By.ID, "id_first_name").send_keys("Dr. Pradeep")
    driver.find_element(By.ID, "id_last_name").click()
    driver.find_element(By.ID, "id_last_name").send_keys("Sanghvi")
    driver.find_element(By.ID, "id_email").click()
    driver.find_element(By.ID, "id_email").send_keys("pradeep@gmail.com")
    driver.find_element(By.ID, "id_phone_number").click()
    driver.find_element(By.ID, "id_phone_number").send_keys("8900961270")
    driver.find_element(By.ID, "id_speciality").click()
    driver.find_element(By.ID, "id_speciality").send_keys("Pediatrician")
    driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    assert driver.title == 'Doctor SignUp!'

def test_invalidemail(test_setup):
    driver.find_element(By.ID, "id_username").click()
    driver.find_element(By.ID, "id_username").send_keys("pradeep")
    driver.find_element(By.ID, "id_password1").click()
    driver.find_element(By.ID, "id_password1").send_keys("iamthequeen")
    driver.find_element(By.ID, "id_password2").click()
    driver.find_element(By.ID, "id_password2").send_keys("iamthequeen")
    driver.find_element(By.ID, "id_first_name").click()
    driver.find_element(By.ID, "id_first_name").send_keys("Dr. Pradeep")
    driver.find_element(By.ID, "id_last_name").click()
    driver.find_element(By.ID, "id_last_name").send_keys("Sanghvi")
    driver.find_element(By.ID, "id_email").click()
    driver.find_element(By.ID, "id_email").send_keys("gautam@mail")
    driver.find_element(By.ID, "id_phone_number").click()
    driver.find_element(By.ID, "id_phone_number").send_keys("8900961270")
    driver.find_element(By.ID, "id_speciality").click()
    driver.find_element(By.ID, "id_speciality").send_keys("Pediatrician")
    driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    assert driver.title == 'Doctor SignUp!'

def test_invalidnumber(test_setup):
    driver.find_element(By.ID, "id_username").click()
    driver.find_element(By.ID, "id_username").send_keys("pradeep")
    driver.find_element(By.ID, "id_password1").click()
    driver.find_element(By.ID, "id_password1").send_keys("iamthequeen")
    driver.find_element(By.ID, "id_password2").click()
    driver.find_element(By.ID, "id_password2").send_keys("iamthequeen")
    driver.find_element(By.ID, "id_first_name").click()
    driver.find_element(By.ID, "id_first_name").send_keys("Dr. Pradeep")
    driver.find_element(By.ID, "id_last_name").click()
    driver.find_element(By.ID, "id_last_name").send_keys("Sanghvi")
    driver.find_element(By.ID, "id_email").click()
    driver.find_element(By.ID, "id_email").send_keys("pradeep@gmail.com")
    driver.find_element(By.ID, "id_phone_number").click()
    driver.find_element(By.ID, "id_phone_number").send_keys("4745961270")
    driver.find_element(By.ID, "id_speciality").click()
    driver.find_element(By.ID, "id_speciality").send_keys("Pediatrician")
    driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    assert driver.title == 'Doctor SignUp!'

def test_signup(test_setup):
    driver.find_element(By.ID, "id_username").click()
    driver.find_element(By.ID, "id_username").send_keys("pradeep")
    driver.find_element(By.ID, "id_password1").click()
    driver.find_element(By.ID, "id_password1").send_keys("iamthequeen")
    driver.find_element(By.ID, "id_password2").click()
    driver.find_element(By.ID, "id_password2").send_keys("iamthequeen")
    driver.find_element(By.ID, "id_first_name").click()
    driver.find_element(By.ID, "id_first_name").send_keys("Dr. Pradeep")
    driver.find_element(By.ID, "id_last_name").click()
    driver.find_element(By.ID, "id_last_name").send_keys("Sanghvi")
    driver.find_element(By.ID, "id_email").click()
    driver.find_element(By.ID, "id_email").send_keys("pradeep@gmail.com")
    driver.find_element(By.ID, "id_phone_number").click()
    driver.find_element(By.ID, "id_phone_number").send_keys("8900961270")
    driver.find_element(By.ID, "id_speciality").click()
    driver.find_element(By.ID, "id_speciality").send_keys("Pediatrician")
    driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    assert driver.title == 'Login!'
