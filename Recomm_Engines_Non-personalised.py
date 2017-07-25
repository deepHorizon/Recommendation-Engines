# -*- coding: utf-8 -*-
"""
Created on Fri May  5 05:17:27 2017

@author: Shaurya Rawat
"""
import pandas as pd
import numpy as np
data=pd.read_csv('D:\IE MBD 2016\Recommendation Engines\IE-Lab1-Package-O1(1)\IE-Lab1-Package-O1\Data\critics.csv',keep_default_na=True)
data.fillna(value=0,inplace=True)

#1
data.columns
mean_data=np.mean(data[data!=0])
mean_data=mean_data.sort_values(ascending=False)
mean_data.head(5)

#2
newdata=data[data!=0]
rating_data=newdata.drop('User',axis=1)
rating=(sum(i>=4 for i in rating_data[rating_data.columns].values)/rating_data[rating_data.columns].count())*100
rating.sort()
rating=rating[::-1]
rating[0:5]

#3
quantity=rating_data[rating_data.columns].count()
quantity.sort()
quantity=quantity[::-1]
quantity[0:5]

#4
#data.ix[:,data.columns!='User']
#we are selecting Star Wars IV by default
Users=data[data.columns[0]].values
starwars4=data[data.columns[1]].values

data_starwars=data.ix[(data['User']=='John')|(data['User']=='Maria')|(data['User']=='Martina')|(data['User']=='Ana')|(data['User']=='Marc')|(data['User']=='Jim')|(data['User']=='Chris')|(data['User']=='Bernard')|(data['User']=='Nuria')|(data['User']=='Nerea')|(data['User']=='Carles')|(data['User']=='Victoria')|(data['User']=='Nadia')|(data['User']=='Oriol')|(data['User']=='Valery')]
totalwatched=data_starwars.shape[0] #15
data_starwars=data_starwars.drop(data_starwars.columns[0],axis=1) #drop User
data_starwars=data_starwars.drop(data_starwars.columns[0],axis=1) #drop Star Wars 4
other_watched=data_starwars[data_starwars.columns].count()
percent_watched=other_watched/totalwatched
percent_watched.sort()
percent_watched=percent_watched[::-1]
percent_watched[0:5]

#5
#Values for Babe
babe_values=data[data.columns[20]].values
for i in babe_values:
    if i>=4:
        print(np.where(babe_values==i))
#from this we get values for iloc 8,10,15,17
data.iloc[8],data.iloc[10],data.iloc[15],data.iloc[17]
#np.shape(data_babe) #(4,21)
#mean_data_babe=np.mean(data_babe)
# we get 4 users: jim,bernard, ivan, nadia
data_babe=data.ix[(data['User']=='Jim')|(data['User']=='Bernard')|(data['User']=='Ivan')|(data['User']=='Nadia')]
data_babe=data_babe.drop(['Babe'],axis=1) #remove Babe from dataset
np.shape(data_babe) #(4,20)
mean_data_babe=np.mean(data_babe)
mean_data_babe.sort()
mean_data_babe=mean_data_babe[::-1]
mean_data_babe[0:5]





