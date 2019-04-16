##################################
#Author: Brian Diunizio | GeoSpatial Analyst | CSA Ocean Sciences Inc.
#File Name: NOAA_NCEI_DEMdownload_WebCrawl_step2.py
#Function: This script is the second and final step of two steps to bulk download NOAA NCEI coastal relief models from https://www.ngdc.noaa.gov/thredds/demCatalog.html
##################################

import pandas as pd
import csv
import requests
import urllib.request
from urllib.request import urlopen
from urllib import request
from bs4 import BeautifulSoup

URL_segment = ("https://www.ngdc.noaa.gov")

contents = []

DEMs = []

download_file = []

with open('URL_List.csv','r') as csvf: # Open file in read mode
    urls = csv.reader(csvf)
    for url in urls:
        contents.append(url) # Add each url to list contents

for url in contents:  # Parse through each url in the list.
    page = urlopen(url[0]).read()
    soup = BeautifulSoup(page, "html.parser")

    for i in soup.find_all("a"):
        rel_href = i.get("href")
        if "fileServer" in rel_href:
            abs_url = URL_segment + rel_href
            DEMs.append(abs_url)

##print (DEMs)

def downloadDEM(DEM_url):
    for url in DEM_url:
        #download_file.append(i.split('tiled_1as/')[1])
        name = (url.split('tiled_3as/')[1])  ##change this as needed. this is part of the final download url in the 'HTTPServer' designation
        path = ("C:\\Path\\to\\local\\Folder") ##keep the double dashes in your file path
        fname = path + "\\"  + name

        req = requests.get(url)
        file = open(fname, 'wb')
        for chunk in req.iter_content(100000):
            file.write(chunk)
        file.close()

downloadDEM(DEMs)
