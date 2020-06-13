# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 15:41:49 2020

@author: Lenovo
"""

import requests
from bs4 import BeautifulSoup
    
url = "https://www.n11.com/muzik/plaklar" 

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

liste = soup.findAll("li", {"class":"column"})
count=1

for li in liste:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href").strip()
    fiyat = li.find("div", {"class":"proDetail"}).findAll("a")[0].text.strip()

    
    print(f"name: {name} link: {link} fiyat: {fiyat}")
    count+=1