
# coding: utf-8

# In[123]:

import urllib2
import ssl
import json
import pandas as pd
from pandas import Series, DataFrame
from pandas import read_html
from pandas.io.json import json_normalize
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from zipfile import ZipFile
import os


# In[124]:

# Parameters
start_year = 2000
end_year = 2015
data_dir = './data/'


# In[125]:

# Download event data files from OpenFDA
'''
api_key='api_key=07hRwPr5tDcuNE0FPWTuzIi2WORhRkDitFti4muJ'
search_url = 'https://api.fda.gov/download.json?'
query = '&search=device.generic_name:davinci&count=event_type.exact'
request = search_url+api_key#+query
context = ssl._create_unverified_context()
search_results = urllib2.urlopen(request,context=context).read()
data = json.loads(search_results.decode('string-escape').strip('"'))
df = json_normalize(data["results"])
for d in df['device.event.partitions'][0]:
    zip_path = d['file']
    quarter = zip_path.split('/')[-2]
    filename = zip_path.split('/')[-1].split('.zip')[0]
    short_filename = filename.split('-')[2]
    if (quarter.find('q') > -1):
        year = int(quarter.split('q')[0])
        if (year >= start_year and year <= end_year):
            print zip_path            
            # Download the Zip file
            with open(data_dir+filename+'.zip', 'wb') as zfile:
                zfile.write(urllib2.urlopen(zip_path).read())
            # Extract the Zip file
            zip_data = ZipFile(data_dir+filename+'.zip', 'r').extractall(data_dir)
            # Rename to quarter name
            os.rename(data_dir+filename,data_dir+quarter+'_'+short_filename+'.json')
            # Clean up the folder by deleting the Zip file
            os.remove(data_dir+filename+'.zip');
            print quarter+' downloaded.'
'''

