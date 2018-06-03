# -*- coding: utf-8 -*-
"""
SELENIUM for web browser automation

Download webdriver for Chrome 
  https://chromedriver.storage.googleapis.com/index.html?path=2.25/

Install Selenium
  conda install -c conda-forge selenium
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# specify which browser to use (Chrome)
browser = webdriver.Chrome(r'chromedriver\chromedriver.exe')
browser.implicitly_wait(2)

# open a browser
browser.get(r'https://www.opm.gov/data/Index.aspx?tag=FedScope')

# select an item in the sort by box
browser.find_element_by_xpath(
    r'//*[@id="ctl01_ctl00_MainContentPlaceHolder_MainContentPlaceHolder_SortCol"]/option[2]'
    ).click()
### Press 'go' button
browser.find_element_by_xpath(
    r'//*[@id="ctl01_ctl00_MainContentPlaceHolder_MainContentPlaceHolder_Filter"]'
    ).click()

# type and submit a query in the search box
inputbox = browser.find_element_by_xpath(
    r'//*[@id="ctl01_ctl00_MainContentPlaceHolder_MainContentPlaceHolder_SearchTerm"]')
inputbox.send_keys('OPM')
inputbox.send_keys(Keys.ENTER)

# select the assessment drop down
browser.find_element_by_xpath(
    r'//*[@id="SecondaryNavigation"]/li[1]/a[2]'
    ).click()

# get_first_zip_link
html = browser.find_element_by_xpath(
    r'//*[@id="ctl01_ctl00_MainContentDiv"]/table/tbody/tr[2]/td[3]/span/a')
link = html.get_attribute('href')

# close the browser
browser.close()
