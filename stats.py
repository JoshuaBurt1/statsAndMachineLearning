import statistics
import math

#user data entry
lst = []  # creating an empty list; Source - https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/
n = int(input("Enter number of elements : ")) # number of elements as input
for i in range(0, n): # iterating till the range
    ele = int(input())
    lst.append(ele) # adding the element 
lst.sort()# sorts list for subsequent functions


print("")
print("############### DATASET ATTRIBUTES ###############")
#sorted array
print("Sorted array:" + str(lst))

#minimum, maximum, range
print("Minimum: " + str(lst[0]) + ", Maximum: " + str(lst[-1]) + ", Range: " + str(lst[-1]-lst[0])) #prints 0th index value of sorted array (minimum), prints final index value of sorted array (maximum), prints range=maximum - minimum

#mean
mean = ""
def meanF(lst):
    mean = (sum(lst)/len(lst))
    return mean
print("Mean of array: " + str(meanF(lst))) #mean of array; print(statistics.fmean(lst)) --> statistics library confirmation
print("Geometric mean: " + str(statistics.geometric_mean(lst))) #https://en.wikipedia.org/wiki/Geometric_mean
print("Harmonic mean: " + str(statistics.harmonic_mean(lst))) #https://en.wikipedia.org/wiki/Harmonic_mean#In_finance

#median
median = "" 
def medianF(lst):
    if len(lst)==1 or len(lst)==2: #median of array; print(str(statistics.median(lst))) --> statistics library confirmation
        median = sum(lst)/len(lst) #median1 of array (1 or 2)
    if len(lst)%2==1 and len(lst)!=1:
        median = lst[int(len(lst)/2):-int(len(lst)/2)] #median2.i of array (3,5,7,...)
    if len(lst)%2==0 and len(lst)!=2:
        median = sum(lst[(int(len(lst)/2)-1):-(int(len(lst)/2)-1)])/2 #median2.ii of array (4,6,8,...)
    return median
print("Median: " + str(medianF(lst)))

#mode of array; print("Mode: " + str(statistics.mode(lst))) --> statistics library confirmation, not true mode as will return lowest number if equally distributed values
mode1 = [] # returns multiple modes, Source: https://www.nobledesktop.com/learn/python/mode-in-python
y ={}
for a in lst:
    if not a in y:
        y[a] = 1
    else:   
        y[a]+=1
mode1 = [g for g, l in y.items() if l==max(y.values())]
print("Mode: " + str(mode1))

#variance
var1 = []
for j in lst:
    var1.append((j-meanF(lst))**2) #calls mean function: meanF
var2=sum(var1)/len(var1)
print("Variance: "+ str(var2))

#standard deviation
print("Standard deviation: " + str(math.sqrt(var2)))


print("")
print("############### QUARTILES ###############")
#QUARTILES #Source: https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_summarizingdata/bs704_summarizingdata7.html
#lower quartile
lqr = []
def lowerQ(lst):
    for l in range(0, int(len(lst)/2)):
        lqr.append(lst[l])
    return lqr
print("Lower Quartile: " + str(lowerQ(lst)) + ", Q1: " + str(medianF(lqr))) #Q1 - median of lower quartile, 25th percentile (Q1)
#upper quartile
uqr = []
def upperQ(lst):
    if len(lst)%2==1: #if length of array is odd (==1)
        for l in range(int(len(lst)/2)+1, len(lst)): #includes median value for odd numbered array (+1)
            uqr.append(lst[l])
        return uqr
    if len(lst)%2==0: #if length of array is even (==0)
        for l in range(int(len(lst)/2), len(lst)):
            uqr.append(lst[l])
        return uqr
print("Upper Quartile: " + str(upperQ(lst)) + ", Q3: " + str(medianF(uqr))) #Q3 - median of upper quartile, 75th percentile (Q3)
#interquartile range 
q1 = medianF(lqr)
q3 = medianF(uqr)
if type(q1) == list and type(q3) == list: #medianF returns a list datatype for lists 6,7,10... etc lengths; this converts to evaluable type
    q1f=q1[0]
    q3f=q3[0]
    iqr1=q3f-q1f
    print("IQR: "+ str(iqr1) + ", Semi-IQR: " + str(iqr1/2)) #semi-IQR is computed as one half the difference between the 75th percentile (Q3) and the 25th percentile (Q1).
    lowOutlier1 = (q1f-1.5*iqr1)
    lowXOutlier1 = (q1f-3*iqr1)
    highOutlier1 = (q3f+1.5*iqr1)
    highXOutlier1 = (q3f+3*iqr1)
    print("Low extreme outlier range: " + str(lowXOutlier1) + ", Low outlier range: " + str(lowOutlier1) + ", High outlier range: " + str(highOutlier1) + ", Extreme high outlier range: " + str(highXOutlier1))
if type(q1) == float and type(q3) == float:
    iqr2=q3-q1
    print("IQR: "+ str(iqr2) + ", Semi-IQR: " + str(iqr2/2))
    lowOutlier2 = (q1-1.5*iqr2)
    lowXOutlier2 = (q1-3*iqr2)
    highOutlier2 = (q3+1.5*iqr2)
    highXOutlier2 = (q3+3*iqr2)
    print("Low extreme outlier range: " + str(lowXOutlier2) + ", Low outlier range: " + str(lowOutlier2) + ", High outlier range: " + str(highOutlier2) + ", Extreme high outlier range: " + str(highXOutlier2))


print("")
print("############### DATA MODELING ###############")
#for a second dataset (x-value, ie. equal time interval); use index value of lst (y-values)
print(lst)
lst_x=[]
for x in range(0, len(lst)):
    lst_x.append(x)
print(lst_x)
print("Covariance: " + str(statistics.covariance(lst_x, lst)))
print("Pearson correlation coefficient: " + str(statistics.correlation(lst_x, lst))) # Pearson correlation coefficient ― also known as Pearson's r, the Pearson product-moment correlation coefficient (PPMCC), the bivariate correlation,[1] or colloquially simply as the correlation coefficient[2] ― is a measure of linear correlation between two sets of data.    
print("Linear regression equation (y=mx+b <--> y=slope*x+intercept): " + str(statistics.linear_regression(lst_x, lst)))
#r-squared
#Adj R-Sq
#root MSE
#dependent mean
#coeff var
#standard error
#t value
#PR > |t|
#residual sum of squares
#bivariate normal distribution
#t-test
#2 tail t-test
#Welch's t-test, or unequal variances t-test
#p-value
#chi-squared test