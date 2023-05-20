#Transportation: ion propulsion - https://www.youtube.com/watch?v=IorDYGI1uqc, drag equation (density = 0.012 kg/m^3, drag coefficient = 1.21, area = 1) --> static electricity generation; https://www.youtube.com/watch?v=2HBiX9BT9ME; Drag Equation Calculator
#Non-linear relationships: polynomial regression
#source: https://www.youtube.com/watch?v=6CZiz-FLZF0

import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

#### LOAD DATA ####
data = pd.read_csv('VelocityToDrag.csv',sep =',')
data = data[['velocity (km/h)','drag (N)']]
print('-'*30);print('HEAD');print('-'*30)
print(data.head()) #Original data format

#### PROCESS DATA ####
#data['velocity'] = data['velocity'].map(lambda i: i.lstrip('AL').rstrip('km/h')) #strips "km/h" from right side of data
#************************************************
#polynomial regression data generation
#y = c+ m1x^1 + m2x^2+ m3x^3...    --> m = gradient or model.coef_; c = intercept

#### PREPARE DATA ####
print('-'*30);print('PREPARE DATA');print('-'*30)
x = np.array(data['velocity (km/h)']).reshape(-1, 1) #x-axis is divided by 10
y = np.array(data['drag (N)']).reshape(-1, 1)
polyFeat = PolynomialFeatures(degree=2) #the degree of the polynomial function to fit the data: 2 --> y = c+ m1x^1 + m2x^2
x = polyFeat.fit_transform(x)
print(x)

#### TRAINING DATA ####
print('-'*30);print('TRAINING DATA');print('-'*30)
model = linear_model.LinearRegression()
model.fit(x,y)
accuracy = model.score(x,y)
print(f'Accuracy:{round(accuracy*100,3)} %') #accuracy that polynomial matches data
y0 = model.predict(x)

#### PREDICTION ####
print('-'*30);print('PREDICTION');print('-'*30)
print(f'Prediction - The drag at {1000} km/h is ',end="")
print(round(int(model.predict(polyFeat.fit_transform([[1000]]))),1),'N') #Calculates drag of 1000km/h in N based on polynomial regression model
x1 = np.array(list(range(1000))).reshape(-1,1)
y1 = model.predict(polyFeat.fit_transform(x1))
print(f'Prediction - The drag at {500} km/h is ',end="")
print(round(int(model.predict(polyFeat.fit_transform([[500]]))),1),'N') #Calculates drag of 500km/h in N based on polynomial regression model
x2 = np.array(list(range(500))).reshape(-1,1)
y2 = model.predict(polyFeat.fit_transform(x2))
plt.plot(y1,'--r') #dashed red line; (polynomial degree 2) predicted value
plt.plot(y2,'-b') #blue solid line; (polynomial degree 2) predicted value
plt.show()