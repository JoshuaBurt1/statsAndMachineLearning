#Standard Normal Distribution = f(x) = (e^(−x^2/2))/(√2π)
#Source - https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm
#Source - Math for the Computer Industry Unit 3.3 

import numpy as np
import matplotlib.pyplot as plt #Display the histogram of the samples, along with the probability density function:

muSND, sigmaSND = 0, 1 #preset values of mu (mean) and sigma (standard deviation)
s = np.random.normal(muSND, sigmaSND, 1000) #Source - https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
abs(muSND - np.mean(s))
abs(sigmaSND - np.std(s, ddof=1))
count, bins, ignored = plt.hist(s, 30, density=True) #plot
plt.plot(bins, 1/(sigmaSND * np.sqrt(2 * np.pi)) * np.exp( - (bins - muSND)**2 / (2 * sigmaSND**2) ), linewidth=2, color='r') #f(x) = e^((−(x−μ)^2)/(2σ^2))/(σ√2π) reduced to (e^(−x^2/2))/(√2π)
plt.show()