from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()


def test_assert_title_of_homepage():
    driver.get("https://pynative.com/")
    assert driver.title == "PYnative: Learn Python with Tutorials, Exercises, and Quizzes"


def test_assert_title_of_homepage_python():
    driver.get("https://pynative.com/python/")
    assert driver.title == "Python Tutorials – PYnative"


def test_assert_presence_of_login_button():
    driver.get("https://pynative.com/python/")
    # driver.find_element(By.XPATH, "//span[@class='close']").click()
    assert driver.find_element(By.LINK_TEXT, "Python File Handling")
