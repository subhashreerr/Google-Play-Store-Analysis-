# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:55:58 2019

@author: Admin
"""

import pandas as pd 
import numpy as np 
import seaborn as sns 
gp = 'googleplaystore.csv'
df2= pd.read_csv(gp)

df2.info()
df2.iloc[10472]
df2 = df2.drop([10472])
df2 = df2.drop([9148])


del df2['App']
del df2['Size']
del df2['Genres']
del df2['Last Updated']
del df2['Current Ver']
del df2['Android Ver']

#1to replace the "," with null 
df2["Installs"]=df2["Installs"].replace({',':''},regex=True)
#df2["Installs"]=df2["Installs"].replace({'+':''},regex=True)# wrong method 
df2["Installs"]=df2["Installs"].map(lambda x: str(x)[:-1])

# removal of symbol in python 
df2.Price = [x.strip('$') for x in df2.Price]

#df2["Price"]=df2["Price"].str.replace({'$':''})
#3removal of the last element in installs 
#df2["Installs"]=df2["Installs"].map(lambda x: str(x)[:-1])
#df2.replace.Installs(to_replace ="0",value ="nan")
#df2.Installs.isnull().sum() 
#df2.replace(to_replace = np.nan, value =-99999) 
df2.Rating.unique()

df2.Rating.isnull().sum()

pd.DataFrame(data.df2, columns=['Rating'])

df2.Rating.median( skipna = True) 
df2.Rating.mean( skipna = True) 
df2.Rating.mode() 

# removal of null in Installs 

df2.Installs.sum()

df2['Installs']=df2['Installs'].astype(int)
type(df2['Installs'][0])



#df3 = df2[df2['Rating'].isna()]
#df1 = df2.dropna()

#df2.groupby(['Installs']).fillna

df2['Rating'] = df2.groupby(['Category'], sort=False)['Rating'].apply(lambda x: x.fillna(x.mean()))


corr = df2.corr()
sns.heatmap(data=corr,square=True,annot=True,cbar=True)
# updation of the data 
df2.to_csv('updated_data3.csv')







