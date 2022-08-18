from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import socket
import getpass
import os
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import csv

data = pd.read_csv('nr_per_filtrin_whatsapp.csv')
data_dict = data.to_dict('list')
numrat = data_dict['numrat']
moblie_no_list = zip(numrat,)

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("http://web.whatsapp.com")
time.sleep(240)

csvfile = open('numrat qe kane whatsapp.csv', 'a', newline='')

for mobile in moblie_no_list:
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(mobile))
    time.sleep(20)
    try:
        elem = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div').click()
        print('Ky numer ka whatsapp: ',mobile)
        writer = csv.writer(csvfile)
        writer.writerows(map(lambda x: [x], mobile))
    except NoSuchElementException:
        pass