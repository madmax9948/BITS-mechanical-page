from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyexcel
import time
import numpy as np
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome('/Users/Shreyas/Desktop/chromedriver',options = options)

sheet = pyexcel.get_sheet(file_name="journal.xlsx")


for i in range(185,200):
    driver.get('https://www.crossref.org/')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="tabs-search"]/li[2]/a').click()
    time.sleep(1)
    search_box = driver.find_element_by_xpath('//*[@id="metadatasearchbox"]')
    time.sleep(1)
    search_box.send_keys(sheet[i,0])
    search_box.send_keys(Keys.ENTER)
    time.sleep(1)
    doi = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[1]/td/div/div/a')
    print(doi.text)