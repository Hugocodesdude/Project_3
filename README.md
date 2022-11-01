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
6. Conclusion
7. Improvments

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

4. Code Breakdown

For this project the steps were; 1.to query using MongosDB. 2. Turn the queries into dataframes. 3. Plot the data point on maps. 4. Visualise the data in a communicative manner. 5. Caluculate the distances from the data points to the chosen office location. 6. Calcute the relative mean. 

The workflow is spread between four juypter note books. 1. Approach. 2. database investigations with mongos. 3. Visualisations. 4. Distances. 5. Functions. 


------

5. Visualisation 

I created 3 interactive maps using Folium which can be found via the images folder. Please open all of these files to be able to view. 

They visualise the aray of criteria points; high value companies, design companies, video game companies, vegan restaurants, basketball courts, starbucks, nightclubs, child care and airports. 

The maps display three radius rings showing a 1km, 3km & 5km ring. This allows us to visualise from the hypothetical office location, what data criteria points are within the catchment boundary. 

------ 

6. Conclusions

Based upon the map visualisations and calculating the mean of criteria distances to to the office locations. 31 Great Pulteney St (51.5121948,-0.1360746) London would be the most suitable location for the gaming start up due to it's relative proximity to high value companies, game companies, design companies and starbucks coffee shops. 

Berlin and Barcelona were not far off, however London had a higher consentration of criteria marks. 


------

7. Next Steps

Further elements to add to the project would be:
- ranking system function  
- quality of life 
- corporate tax rate
- mean salaries
- access to green spaces 