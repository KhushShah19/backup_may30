   
# working on - https://docs.python.org/3/library/random.html

import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

page = urllib.request.urlopen("https://docs.python.org/3/library/random.html")
soup = bs(page)

#print(soup)

names = soup.body.findAll("dt")

#print(names)

function_names = re.findall('id="random.\w+', str(names))
function_names = [item[4:] for item in function_names]

#print(function_names)

description = soup.body.findAll('dd')

function_usage = []

for item in description:

    item = item.text
    item = item.replace('\n', ' ')
    function_usage.append(item)

#print(function_names)
#print(function_usage)
#print(len(function_names))
#print(len(function_usage))

data = pd.DataFrame({"Function name": function_names, "Function usage": function_usage})

#print(data)

data.to_csv('classmate')

print('Done ')



