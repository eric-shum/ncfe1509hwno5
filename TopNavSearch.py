from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TopNavSearch:
    def __init__(self, driver):
        self.mm = 0
        self.ucarriage = 0
        self.mdent = 0
        self.fend = 0
        self.rend = 0
        self.driver = driver

    def runSearch(self, query):
        searchfield = self.driver.find_element(By.ID, "input-search")
        searchfield.clear()
        searchfield.send_keys(query)
        searchBtn = self.driver.find_element(By.XPATH, "//button[@data-uname='homepageHeadersearchsubmit']")
        searchBtn.click()
        html = self.driver.page_source
        datawait = WebDriverWait(self.driver, 60).until(
            ec.presence_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//td")))
        datatable = self.driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable\"]")
        # self.assertIn("PORSCHE", datatable.text)
        # self.driver.find_element(By.NAME, "serverSideDataTable_length").click()
        return datatable

    def showEntries(self, numOfEntries):
        dropdown = self.driver.find_element(By.NAME, "serverSideDataTable_length")
        dropdown.find_element(By.XPATH, "//option[. = " + numOfEntries + "]").click()
        dropdown.click()
        return dropdown

    def switch(self, damage):
        switcher = {
            'REAR END': self.rearend,
            'FRONT END': self.frontend,
            'MINOR DENT/SCRATCHES': self.minordent,
            'UNDERCARRIAGE': self.undercarriage
        }
        return switcher.get(damage, self.misc)()

    def rearend(self):
        self.rend += 1

    def frontend(self):
        self.fend += 1

    def minordent(self):
        self.mdent += 1

    def undercarriage(self):
        self.ucarriage += 1

    def misc(self):
        self.mm += 1


