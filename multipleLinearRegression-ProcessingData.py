#shows multiple linear relationships
#data sources: UCI - machine learning repository, kaggle --> data source must be in same folder as python file
#csv = comma separated value

import pandas as pd #allows for importing excel file data
import numpy as np
import sklearn
from sklearn import preprocessing,linear_model

#### LOAD DATA ####
print('-'*30);print("IMPORTING DATA ");print('-'*30);
data = pd.read_csv('houses_to_rent.csv', sep = ',')
data = data [['city','rooms','bathroom', 'parking spaces','fire insurance', #data column header 
'furniture','rent amount']]
print(data.head()) # prints unprocessed data

#### PROCESS DATA #### 
#removing unprocessable symbols in csv data
data['rent amount'] = data['rent amount'].map(lambda i: int(i[2:].replace(',',''))) #lambda i: removes first 2 values(R$) & comma removed
data['fire insurance'] = data['fire insurance'].map(lambda i: int(i[2:].replace(',','')))
le = preprocessing.LabelEncoder() #sklearn function 
data['furniture'] = le.fit_transform((data['furniture'])) # le.fit_transform: transforms furnished & not furnished --> 1 & 0
print(data.head()) # prints processed data