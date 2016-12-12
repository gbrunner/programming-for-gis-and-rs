#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      greg6750
#
# Created:     11/12/2016
# Copyright:   (c) greg6750 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib2
import json

## Get all immigration data
url = 'http://data.unhcr.org/api/stats/mediterranean/monthly_arrivals_by_country.json?'
data = urllib2.urlopen(url)
imm_data = json.load(data)
print(imm_data)


## Get only Greece from 2014
country = 'GRE'
year = 2016
url =  'http://data.unhcr.org/api/stats/mediterranean/monthly_arrivals_by_country.json?year=%s&country=%s' % (year, country)
data = urllib2.urlopen(url)
imm_data = json.load(data)
print(imm_data)

## Get only Greece from 2014
#country = 'GRE'
year = 2016
month = 1
url =  'http://data.unhcr.org/api/stats/mediterranean/monthly_arrivals_by_country.json?year=%s&month=%s' % (year, month)
data = urllib2.urlopen(url)
imm_data = json.load(data)
print(imm_data)


## Parsing the data into an array
rows = []
import datetime
for row in enumerate(imm_data):
    date = datetime.datetime.strptime(str(row[1]['month']) + ',' + str(row[1]['year']), "%m,%Y").date()
    temp = (row[1]['country_en'],date, row[1]['value'], row[1]['month_en']+'_'+str(row[1]['year']))
    rows.append(temp)
    print(temp)

## Create table

## Insert data into table

## Join Table to Existing feature class