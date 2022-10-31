# GeoSpatial Data Project

#Title: Start-Up off

A comparative review into 3 candidate cities for a new start-up in the gaming industry. 

------- 

## Table of Contents
1. Project Focus
2. Hypothesis 
3. Tools & Method
4. Code breakdown 
5. Visualisation 
6. Improvments

## 1. Project Focus
To investigate three selected European candidate cities (London, Berlin & Barcelona) on which is best suited based off of achieving the largest volume of criteria.

--------

2. Hypothesis 

Going into this project my feeling was that Barcelona would be the best location for the start up. Given it's lower cost of living and attractive start up climate. However let'a see what the data reveals. 

--------

3. Tools & Method

For this project I used a combination of data base queries using MongosDB and API calls with FourSquare. 

I used the following tools to run the code: 

```python
from pymongo import MongoClient
import pandas as pd
import time 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import pandas as pd
import os
import requests
import json
from dotenv import load_dotenv
```

------

6. Next Steps

Further elements to add to the project would be:
- ranking system function  
- quality of life 
- corporate tax rate
- mean salaries
- access to green spaces 