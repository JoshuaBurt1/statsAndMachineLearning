#Probability Density Function = f(x) = e^((−(x−μ)^2)/(2σ^2))/(σ√2π); related to standard normal distribution
#Source - https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm
#Source - https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
#Source - Math for the Computer Industry Unit 3.3 

import numpy as np
import matplotlib.pyplot as plt #Display the histogram of the samples, along with the probability density function:
import scipy.stats as st

#A. Custom Probability Density Function -->user sets values of mu (mean) and sigma (standard deviation)
mu = eval(input("What is the mean (mu): ")) #Example: what is the average grade from 0-100
sigma = eval(input("What is the standard deviation (sigma): ")) #Example: What is the distribution of values from the mean of the data set
s = np.random.normal(mu, sigma, 10000) #creates (10000) randomized values within normal distribution range of mu and sigma
abs(mu - np.mean(s))
abs(sigma - np.std(s, ddof=1))
count, bins, ignored = plt.hist(s, 30, density=True) 
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r') #f(x) = e^((−(x−μ)^2)/(2σ^2))/(σ√2π)
plt.show() #matplotlib.pyplot; prints a sample plot using random data - unrelated to subsequent calculations
x = int(input("To find the probability of an event occurring in comparison to normally distributed data, enter a value: ")) #Example: grades --> mean score of 58 and a standard deviation of 7, what is probability x = score of 70
z=(x-mu)/sigma 
print("The z-score of a value (x) occurring is " + str(z)) 
pLeft=st.norm.cdf(z) #scipy.stats
print("The probability of an event occurring less than (x) is: "+str(pLeft))
pRight=1-st.norm.cdf(z)
print("The probability of an event occurring greater than (x) is: "+str(pRight))
