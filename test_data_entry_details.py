from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.fixture()
def setUp():
    global name, address, pincode, mobile_number, email_id, password, confirm_password, driver
    name = input("Enter your Name: ")
    address = input("Enter your Address: ")
    pincode = input("Enter your Pincode: ")
    mobile_number = input("Enter your Mobile Number: ")
    email_id = input("Enter your Mail ID: ")
    password = input("Enter your Password: ")
    confirm_password = input("Re-Enter your Password to Confirm it: ")

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    yield

    time.sleep(7)
    driver.close()

def test_data_entry(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/userdata.php")

    driver.find_element_by_name("name").send_keys(name)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[4]").click()
    time.sleep(2)
    driver.find_element_by_name("Address").send_keys(address)
    time.sleep(2)
    driver.find_element_by_name("Pincode").send_keys(pincode)
    time.sleep(2)
    driver.find_element_by_name("Mobile").send_keys(mobile_number)
    time.sleep(2)
    driver.find_element_by_name("Email").send_keys(email_id)
    time.sleep(2)
    driver.find_element_by_name("pass").send_keys(password)
    time.sleep(2)
    driver.find_element_by_name("cnfpass").send_keys(confirm_password)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[10]/td[2]/div/input").click()
    time.sleep(2)
    driver.find_element_by_name("subbtn").click()
    time.sleep(7)