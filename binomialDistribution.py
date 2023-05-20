#Binomial distribution
#Source - https://www.geeksforgeeks.org/python-binomial-distribution/
#Source - Math for the Computer Industry Unit 3.3 --> P(X=r) = nCr*p^(r)*q^(n-r)

import math 
import scipy
from scipy.stats import binom

nInput = int(input("How many trials (n) of probability object? ")) # setting the values of n and p
pInput = eval(input("What is the probability (p) of the success of the probability object ie. dice = 1/6, coin = 1/2? ")) #eval converts string fraction/decimal to int fraction/decimal

r_values = list(range(nInput + 1)) # defining the list of r values
mean, var = binom.stats(nInput, pInput) # obtaining the mean and variance 
dist = [binom.pmf(r, nInput, pInput) for r in r_values ] # list of pmf values

print("r\tp(r) = p^(r)*q^(n-r)") # printing the table
for i in range(nInput + 1):
    print(str(r_values[i]) + "\t" + str(dist[i]))

print("mean = "+str(mean) +", variance = "+str(var)) # printing mean and variance
#x = int(input("Input the occurrences of success: ")) #Example: The probability of getting x=0 heads out of n=10 trials
#print("The probability of success occurring " +str(x)+ " times out of "+ str(nInput) +" trials is:")
#x=(math.factorial(nInput))/((math.factorial(x))*(math.factorial(nInput-x))) #x=nC(r) = n!/((r)!*(n−r)!)
#probS=x*(dist[0]) #this only works for probability 0.5
#print("is " +str(x) + "*" + str(dist[0]) +" or " + str(probS) + " or " + str(probS*100)+"%") #Example: The probability of getting x=0 heads at a p=0.5 or 50% chance out of n=10 trials is 0.0009765625

