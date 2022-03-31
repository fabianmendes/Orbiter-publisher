from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
# For Scrapping.----------------------------------
import requests
from bs4 import BeautifulSoup
import html
#from lxml import etree
#------------------------------------------------
import os

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(40)  # seconds
paggina = "https://orbitacomunicacion.com/"
driver.get(paggina + "entra/")

#Detecting items:
browser = driver
username = os.environ['USERNM']
password = os.environ['PASSWD']

WebDriverWait(driver, 20).until(
    expected_conditions.
        presence_of_element_located(
        (By.ID, 'user_login')))
        # //*[@id="user_login"]
yeah = driver.find_element_by_xpath(
    '//*[@id="user_login"]'
    )
yeah.send_keys(username)
hell = driver.find_element_by_xpath(
       '//*[@id="user_pass"]'
        )
hell.click()
hell.send_keys(password)
hell.send_keys(Keys.ENTER)

WebDriverWait(driver, 20).until(
    expected_conditions.
        presence_of_element_located((By.XPATH,
                                     '//*[@id="editor"]/div[1]/div[1]/div[2]/div[2]')))


# DONE. We are in! Now let's write.
# ------------------
