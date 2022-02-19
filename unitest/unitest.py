import unittest
from selenium import webdriver
import page
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):


        assert "baidu" in self.driver.title,"python.org title doesn't match."
        self.driver.find_element(By.XPATH, '//*[@id="id-search-field"]').send_keys("pycon")
        self.driver.find_element(By.ID, 'submit').click()
        assert "No results found." not in self.driver.page_source,"No results found."






    def tearDown(self):
        self.driver.close() 
   

if __name__ == "__main__":
    unittest.main()