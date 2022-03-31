# Code for extracting news from rt..
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
# For Scrapping.----------------------------------
import requests as rq
from bs4 import BeautifulSoup as Bs
import html
from lxml import etree
#------------------------------------------------

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(40)  # seconds

url_yes = "https://actualidad.rt.com/todas_las_noticias"
driver.get(url_yes)

r = rq.get(url_yes)
print(r.status_code)  # should be 200.
soup = Bs(r.content, "html.parser")

dom = etree.HTML(str(soup))

#----------

search_xpath = "/html/body/div[1]/main/div/section/div[1]/div[3]/div[1]/div"
              # /html/body/div[1]/main/div/section/div[1]/div[3]/div[1]/div[1]/article/div[2]/div[1]/div/div/a       
a = driver.find_elements_by_xpath(search_xpath)
#print(a)
b = dom.xpath(search_xpath)  # Both are the same.
#print(b)
lista_pags = []
for i in range(int(len(a)/2) -1):
    
    b = dom.xpath(search_xpath + "[" + str(i+1) +
                  "]/article/div[2]/div[1]/div/div/a")
    #try:
        #print(b[0].attrib['href'])
    # 
    link = b[0].attrib['href']
    # it's https://actualidad.rt.com/ + b.
    lista_pags.append("https://actualidad.rt.com/"
                      + b)
    #finally:
    #    print(b)
    
