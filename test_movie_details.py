from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.fixture()
def setUp():
    global movie_name, year_of_release, director_name, distributor, producer, driver
    movie_name = input("Enter a Movie Name: ")
    year_of_release = input("Enter the Year of Release: ")
    director_name = input("Enter the Director Name: ")
    distributor = input("Enter a Distributor Name: ")
    producer = input("Enter the Producer Name: ")

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    yield
    time.sleep(7)
    driver.close()

def test_movie_form(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    driver.find_element_by_name("mname").send_keys(movie_name)
    time.sleep(2)
    driver.find_element_by_name("myear").send_keys(year_of_release)
    time.sleep(2)
    driver.find_element_by_name("mdirector").send_keys(director_name)
    time.sleep(2)
    driver.find_element_by_name("mdist").send_keys(distributor)
    time.sleep(2)
    driver.find_element_by_name("mproducer").send_keys(producer)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[3]").click()
    time.sleep(2)
    driver.find_element_by_name("subbtn").click()
    time.sleep(7)
