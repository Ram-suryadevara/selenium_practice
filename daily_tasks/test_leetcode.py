import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup(request):
    global driver
    print("initiating chrome driver")
    driver = webdriver.Chrome()
    driver.get("https://leetcode.com/")
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_title(self):
        print("Verify title...")
        print(driver.title)
        assert "LeetCode - The World's Leading Online Programming Learning Platform" in driver.title

    def test_content_text(self):
        print("Verify content on the page...")
        centerText = driver.find_element(By.XPATH, "//h1[normalize-space()='A New Way to Learn']").text
        assert "A New Way to Learn" == centerText
