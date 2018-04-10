import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class PythonOrgSearch2 (unittest.TestCase):

    def setUp(self):
        # create instance of Firefox WebDriver
        # self.driver = webdriver.Firefox(executable_path="/home/crawler/Documents/geckodriver")
        self.driver = webdriver.Chrome("/home/crawler/Documents/chromedriver")

    def test_search_in_python_org(self):
        # navigate to page with URL
        self.driver.get("http://www.python.org")
        # check string "Python" in title
        self.assertIn("Python", self.driver.title)
        # find element
        elem = self.driver.find_element_by_name("q")
        # enter keyboard, clear all before
        elem.clear()
        elem.send_keys("pycon1")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source
        # self.assertNotIn("No results found.", self.driver.page_source)

    def tearDown(self):
        self.driver.close()