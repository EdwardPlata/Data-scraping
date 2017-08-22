#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:42:52 2017

@author: anthonyplata
"""
#import libraries
import urllib2
from bs4 import BeautifulSoup

#specify url

quote_page= 'http://www.bloomberg.com/quote/SPX:IND'

# query the website and return the html to the variable
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable 'soup'

soup = BeautifulSoup(page,'html.parser')

# Now that we got the variable 'soup' and page we can now start taking out hte info

#take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class':'name'})

# strip)_ is used to remove starting and trailing
name_set = name_box.text.strip() # strip() is used to remove starting and trailing
print (name_set)

# get the index price

price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print (price)

#But first, we have to import the Python csv module and the datetime module to get the record date. Insert these lines to your code in the import section.

import cvs from datetime import datetime

with open('indext.cvs', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now])


# for loop
data = []
for pg in quote_page:
 # query the website and return the html to the variable ‘page’
 page = urllib2.urlopen(pg)
# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, ‘html.parser’)
# Take out the <div> of name and get its value
 name_box = soup.find(‘h1’, attrs={‘class’: ‘name’})
 name = name_box.text.strip() # strip() is used to remove starting and trailing
# get the index price
 price_box = soup.find(‘div’, attrs={‘class’:’price’})
 price = price_box.text
# save the data in tuple
 data.append((name, price))
 
 #open a csv file with append, so old data will not be erased
 with open('indext.csv','a') as csv_file:
     writer = csv.writer(csv_file)
     # the for loop
     for name, price in data:
         writer.writerow([name, price, datetime.now()])
 
 
 
 
 