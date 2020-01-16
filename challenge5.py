import unittest, re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common2.TopNavSearch import TopNavSearch
from collections import Counter


class challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        self.driver.maximize_window()
        s = TopNavSearch(self.driver)
        querylist = ["porsche", "honda", "ford", "nissan"]
        numOfEntry = 100
        for q in querylist:

            self.assertIn(q.upper(), s.runSearch(q).text)
            self.assertIn(str(numOfEntry), s.showEntries(str(numOfEntry)).text)

            modelslist = []
            damageslist = []

            i = 1
            while i <= numOfEntry:
                element = self.driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable\"]/tbody/tr[" + str(i) + "]/td[6]/span")
                modelslist.append(element.text)
                element2 = self.driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable\"]/tbody/tr[" + str(i) + "]/td[12]/span")
                damageslist.append(element2.text)
                i += 1

            modelslist.sort()
            print(modelslist)

            c = Counter(modelslist)

            for model, modelcount in c.items():
                isOrAre = " is "
                if int(modelcount) > 1:
                    isOrAre = " are "
                print("There" + isOrAre + str(modelcount) + " " + model + " on the page")

            print(damageslist)

            for d in range(len(damageslist)):
                s.switch(damageslist[d])

            print("There are " + str(s.rend) + " REAR END damages on the page for " + q)
            print("There are " + str(s.fend) + " FRONT END damages on the page for " + q)
            print("There are " + str(s.mdent) + " MINOR DENT/SCRATCHES damages on the page for " + q)
            print("There are " + str(s.ucarriage) + " UNDERCARRIAGE damages on the page for " + q)
            print("There are " + str(s.mm) + " MISC damages on the page for " + q)

            s.rend = s.fend = s.mdent = s.ucarriage = s.mm = 0

if __name__ == '__main__':
    unittest.main()