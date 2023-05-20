#Financial: determines whether house is cheap or overpriced based on comparing multiple houses with multiple attributes
#multiple linear regression --> multiple gradients & coefficients (# data attributes = # of gradients)
#data sources: UCI - machine learning repository, kaggle --> data source must be in same folder as python file
#csv = comma separated value
#source = https://www.youtube.com/watch?v=BETGdxOA1ss

import pandas as pd #pd is short form of pandas
import numpy as np #np is short form of numpy
import matplotlib.pyplot as plt
import sklearn
from sklearn import preprocessing,linear_model

#### LOAD DATA ####
print('-'*30);print("IMPORTING DATA ");print('-'*30);
data = pd.read_csv('houses_to_rent.csv', sep = ',')
data = data [['city','rooms','bathroom', 'parking spaces','fire insurance',
'furniture','rent amount']] 
print(data.head()) # prints unprocessed data

#### PROCESS DATA ####
#removing unprocessable symbols in csv data
data['rent amount'] = data['rent amount'].map(lambda i: int(i[2:].replace(',',''))) #lambda i: removes first 2 values(R$) & comma removed
data['fire insurance'] = data['fire insurance'].map(lambda i: int(i[2:].replace(',','')))
le = preprocessing.LabelEncoder() #sklearn function 
data['furniture'] = le.fit_transform((data['furniture'])) # le.fit_transform: transforms furnished & not furnished --> 1 & 0
print(data.head()) # prints processed data

print('-'*30);print("CHECKING NULL DATA ");print('-'*30);
print(data.isnull().sum()) #checks for data sets with null data
#data = data.dropna() #replaces null data with 0 (if any null data)
print('-'*30);print(" HEAD ");print('-'*30);
print(data.head())

#************************************************
#multiple linear regression data generation
#y = c+ m1x1 + m2x2+ m3x3...    --> m = gradient or model.coef_; c = intercept; in this case 6 attributes therefore 6 mx values

#### SPILT DATA ####
#need to split data into x and y values
print('-'*30);print(" SPLIT DATA ");print('-'*30);
x = np.array(data.drop(['rent amount'],1))
y = np.array(data['rent amount'])
print('X',x.shape) #prints values and associated attributes
print('Y',y.shape) #prints values

xTrain, xTest, yTrain, yTest = sklearn.model_selection.train_test_split(x,y,
test_size=0.2) #splits data set into testing set and training set; test_size can affect model accuracy
#, random_state=10)
print('XTrain',xTrain.shape) #prints training set
print('XTest',xTest.shape) #prints testing set

#### TRAINING ####
print('-'*30);print(" TRAINING ");print('-'*30);
model = linear_model.LinearRegression()
model.fit(xTrain,yTrain)
accuracy = model.score(xTest,yTest)
print('Coefficients: ',model.coef_)
print('Intercept: ', model.intercept_)
print('Accuracy:',round(accuracy*100,3),'%')

#### EVALUATION ####
print('-'*30);print(" MANUAL TESTING ");print('-'*30);
testVals = model.predict(xTest)
print(testVals.shape) #prints testing set
error = []
for i,testVal in enumerate(testVals): #prints actual rent amount, predicted rent amount, error (negative is good deal, positive is overpriced)
    error.append(yTest[i]-testVal)
    print(f'Acutal:{yTest[i]} Prediction:{int(testVal)} Error: {int(error[i])}') #comment out to view previous print statements
#plt.plot(x,y,'-*r')
#plt.show()