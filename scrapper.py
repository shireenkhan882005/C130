from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv


START_URL="https://exoplanets.nasa.gov/exoplanet-catalog/"


browser=webdriver.Chrome("chromedriver.exe")

browser.get(START_URL)


def scrape():
    headers=["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date", "hyperlink", 
            "planet_type", "planet_radius", "orbital_radius", "orbital_period", "eccentricity"]
    planet_data=[]


    soup= BeautifulSoup(browser.page_source,"html.parser")
    for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
        li_tags=ul_tag.find_all("li")
        temp_list=[]
        for index,li_tag in enumerate(li_tags):
            if index ==0:
                temp_list.append(li_tag.find_all("a")[0].contents[0])

            else:
                try:
                    temp_list.append(li_tag.contents[0])

                except: 
                    temp_list.append("")   


        hyperling_li_tag=li_tags[0]   

        temp_list.append("https://exoplanets.nasa.gov" + hyperling_li_tag.find_all("a",href=True)[0]["href"]         