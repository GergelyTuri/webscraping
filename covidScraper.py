#!/usr/bin/env python
# coding: utf-8

#################################################################
# This file collets data from https://coronavirus.health.ny.gov #
# website. GT 3/27/2020.                                        #
#################################################################


from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# downlad a page and print out some content of it
url = 'https://coronavirus.health.ny.gov/county-county-breakdown-positive-cases'
page = get(url)
# print(page.text[:500])
print('page status code: %s' % page.status_code)
      
# parsing the page with bs4
soup = BeautifulSoup(page.content, 'html.parser')
# soup

# finding the date of the update on the site
# and converting it to file name
# the line below creates a bs4 object then converts it to str
updateDate = soup.find('div',
             attrs={'class':'wysiwyg--field-webny-wysiwyg-title'}).text
print(updateDate)
(text, date) = updateDate.split(': ')
# print(date)
date0 = datetime.strptime(date, '%B %d, %Y | %I:%M%p')
# print(date0)
dateStr = datetime.strftime(date0, '%Y_%m_%d__%H_%M')
fileName = dateStr  

# using `find_all` method to find the data table 
tables = soup.find_all('table')
      
# prepping dataframe by convering `tables` to list 
# cool factor: reading bs4 ResultSet with Pandas
# https://pythonprogramminglanguage.com/web-scraping-with-pandas-and-beautifulsoup/

tablelist = pd.read_html(str(tables))
      
# dump it to csv
path = ('c:/Users/Gergo_PC/Documents/code/webscraping/covidData/')
tablelist[0].to_csv(path+text+fileName+'.csv')




