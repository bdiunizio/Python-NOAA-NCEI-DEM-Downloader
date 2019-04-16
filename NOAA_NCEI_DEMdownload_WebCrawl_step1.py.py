##################################
#Author: Brian Diunizio | GeoSpatial Analyst | CSA Ocean Sciences Inc.
#File Name: NOAA_NCEI_DEMdownload_WebCrawl_step1.py
#Function: This script is the first step of two steps to bulk download NOAA NCEI coastal relief models from https://www.ngdc.noaa.gov/thredds/demCatalog.html
##################################

import pandas as pd
import csv
import requests
import urllib.request
from bs4 import BeautifulSoup

first_url = ("https://www.ngdc.noaa.gov/thredds/catalog/tiles/tiled_3as/catalog.html") ## link to list of netCDF files after clicking 'Download DEM' from the selected footprint on the NCEI bathy web map
#partial_url =
r = requests.get(first_url)
content = r.text
soup = BeautifulSoup(content,"html.parser")

rel_url_list = []
abs_url_list = []

intermed_abs = first_url.split("catalog.html")
url_first_half = intermed_abs[0]
#print (url_first_half)

for td in soup.find_all("td", {"align" : "left"}):
    a_tag = td.find('a')
    rel_href = a_tag.get("href")
    rel_url_list.append(rel_href)
    
for i in rel_url_list:
    if i.endswith(".nc"):
        full_path = url_first_half + i
        abs_url_list.append(full_path)
##print (abs_url_list)

data_frame = pd.DataFrame({"URL" : (abs_url_list)})
data_frame.to_csv("URL_List.csv") ##once this .csv outputs to your folder, open it up with MS Excel and cut/paste all of the url links starting with A1 and delete anything beyond the final record in column A as well as anywhere else in the spreadsheet then save
