# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 15:03:58 2020

@author: Lenovo
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

liste = soup.find("tbody", {"class":"lister-list"}).findAll("tr", limit=250)
count = 1


for tr in liste:
    title = tr.find("td", {"class":"titleColumn"}).find("a").text
    year = tr.find("td", {"class":"titleColumn"}).find("span").text.strip("()")
    rating = tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text
    
    
    print(f"{count}- film: {title.ljust(250)} yıl: {year} değerlendirme: {rating}")
    count+=1
print(liste)

