# -*- coding: utf-8 -*-
"""
Created on Wed May 10 20:01:54 2017

@author: Shaurya Rawat
"""

import pandas as pd
import numpy as np
import math

data=pd.read_csv('D:\\IE MBD 2016\\Recommendation Engines\\IE-Lab1-Package-O1(1)\\IE-Lab1-Package-O1\\Data\\critics.csv')
data.fillna(value=0,inplace=True)
#1
#Pearson Correlation Coefficient
from scipy.stats.stats import pearsonr
data2=data.drop(['User'],axis=1)
coeff=pearsonr(data2.iloc[14].values,data2.iloc[11].values)
pear=np.corrcoef(data2.iloc[14].values,data2.iloc[11].values)[1,0]

#2
import matplotlib.pyplot as plt

#Pearson's product-moment coefficient characteries the slope of linear fit
#We use linear regression to plot it on the scatter plot
##EXECUTE ENTIRE CHUNK TOGETHER TO GET THE GRAPH
##      FOR Victoria and Nuria
plt.scatter(data2.iloc[14],data2.iloc[11],color='blue')
A = np.vstack([data2.iloc[14].values,np.ones(len(data2.iloc[14].values))]).T
m,c = np.linalg.lstsq(A,np.array(data2.iloc[11].values))[0]
plt.plot(data2.iloc[14].values,data2.iloc[14].values*m+c,label="r = %6.2e"%(pear))
plt.legend(loc=3)
#########
## FOR Maria and Nerea (1,12)
pear2=np.corrcoef(data2.iloc[1].values,data2.iloc[12].values)[1,0]
plt.scatter(data2.iloc[1],data2.iloc[12],color='blue')
A = np.vstack([data2.iloc[1].values,np.ones(len(data2.iloc[1].values))]).T
m,c = np.linalg.lstsq(A,np.array(data2.iloc[12].values))[0]
plt.plot(data2.iloc[1].values,data2.iloc[1].values*m+c,label="r = %6.2e"%(pear2))
plt.legend(loc=3)
#The pearson correlation coefficient is greater for Maria and Nerea therefore they are more similar
#than Victoria and Nuria.
##########
## FOR Chris and Jim (8,9)
pear3=np.corrcoef(data2.iloc[8].values,data2.iloc[9].values)[1,0]
plt.scatter(data2.iloc[8],data2.iloc[9],color='blue')
A = np.vstack([data2.iloc[8].values,np.ones(len(data2.iloc[8].values))]).T
m,c = np.linalg.lstsq(A,np.array(data2.iloc[9].values))[0]
plt.plot(data2.iloc[8].values,data2.iloc[8].values*m+c,label="r = %6.2e"%(pear3))
plt.legend(loc=3)
#The pearson correlation coefficient for Chris and Jim is greater than that of Victoria and Nuria
#but less than that of Maria and Nerea
##########


#3
#First we drop Victoria's record from the dataset
data_without_user=data.drop(['User'],axis=1)
recomm_data=data.drop(data.index[14]) #14 is Victoria's Record
recomm_data=recomm_data.drop(['User'],axis=1)
row_means=np.mean(recomm_data)
user_mean=np.mean(data_without_user.iloc[14])
recomm_data.shape[0]#19
pearson=[0]*10
for i in range(19):
    pearson.append(np.corrcoef(data_without_user.iloc[14].values,recomm_data.iloc[i].values)[1,0])
for i in range(9):
    pearson.remove(0)
pearson.remove(0)
pearson # now we have a list of all pearson correlation coefficients 
diff=recomm_data-row_means
diff=diff.multiply(pearson,axis=0)
d=sum(diff.values)
score=user_mean+ (d/(sum(np.abs(pearson))))
victoria_values=data_without_user.iloc[14].values
victoria_values=victoria_values.tolist() #converting the row Victoria to list to find indices

index= [i for i, x in enumerate(victoria_values) if x == 0.0] #index of zeros in victoria
finalscore=score[index]
finalscore.sort()
finalscore=finalscore[::-1]
finalscore[0:5]


#4
pearson
pearson.sort()
pearson=pearson[::-1]
pearson[0:5]




    
        