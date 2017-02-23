import urllib2
import json

## Get all immigration data
url = 'http://data.unhcr.org/api/stats/mediterranean/monthly_arrivals_by_country.json?'
data = urllib2.urlopen(url)
imm_data = json.load(data)
print(imm_data)

for row in enumerate(imm_data):
    print(row[1]['country_en'])
    print(row[1]['value'])

