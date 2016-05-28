
# coding: utf-8

# In[103]:

import urllib2
import ssl
import json
import pandas as pd
from pandas import Series, DataFrame
from pandas import read_html
from pandas.io.json import json_normalize
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
from IPython.display import display
from re import sub
from decimal import Decimal
import sys


# In[112]:

# Download data and load into a data frame
api_key='api_key=07hRwPr5tDcuNE0FPWTuzIi2WORhRkDitFti4muJ'
search_url = 'https://api.fda.gov/device/event.json?'
context = ssl._create_unverified_context()
query = '&search=date_received:[19910101+TO+20160101]&count=date_received'
request = search_url+api_key+query
data = urllib2.urlopen(request,context=context).read()
data = json.loads(search_results.decode('string-escape').strip('"'))
df = json_normalize(data["results"])


# In[113]:

# Fix date format
df['time'] = pd.to_datetime(df['time'])


# In[120]:

df[df['count'] > 10000]


# In[119]:

df.plot(x='time', y='count')


# In[ ]:



