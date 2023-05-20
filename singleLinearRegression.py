#Scientific measurement: compares one value (celsius) to another value (farenheit) & shows relationship (linear)
#shows linear relationship between C (x-axis) and F (y-axis)

import sklearn  
import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn import model_selection
from sklearn import linear_model

#************************************************
#single linear regression data generation

#y = mx +c    --> m = gradient or model.coef_; c = intercept
#F = 1.8*C +32

x = list(range(0,100)) # C
y = [1.8*F +32 for F in x] # F
#y = [1.8*F +32 + random.randint(-3,3) for F in x] # F
print(f'X: {x}')
print(f'Y: {y}')

plt.plot(x,y,'-*r')
plt.show()

#************************************************
#single linear regression training model

x = np.array(x).reshape(-1,1) #formatting that machine learning function requires
y = np.array(y).reshape(-1,1) #formatting that machine learning function requires

xTrain, xTest, yTrain, yTest = model_selection.train_test_split(x,y,test_size=0.2) #data needs to be trained before testing; test_size=0.2 returns 80% values
#print(xTrain.shape)
model = linear_model.LinearRegression()
model.fit(xTrain,yTrain)
accuracy = model.score(xTest,yTest)
print(f'Cofficients: {model.coef_}') #confirms that model.coef_ is 1.8 from F = 1.8*C +32
print(f'Intercept: {model.intercept_}') #confirms that model.intercept is 32 from F = 1.8*C +32
print(f'Accuracy: {round(accuracy*100,2)}')