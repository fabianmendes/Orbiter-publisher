# Code for extracting news from rt..

# For Scrapping.----------------------------------
import requests as rq
from bs4 import BeautifulSoup as Bs
import html
from lxml import etree
#------------------------------------------------

url_yes = "https://actualidad.rt.com/todas_las_noticias"

r = rq.get(url_yes)
print(r.status_code)  # should be 200.
soup = Bs(r.content, "html.parser")

dom = etree.HTML(str(soup))
noticias_xpath = "/html/body/div[1]/main/div/section/div[1]/div[3]/div[1]"

noticias_lista = dom.xpath(noticias_xpath + "/div")

print(len(noticias_lista))
#print(str(noticias_lista))

