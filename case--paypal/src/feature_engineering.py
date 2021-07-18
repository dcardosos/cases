import pandas as pd
import numpy as np
import os
import math

SRC_DIR = os.path.join( os.path.abspath( '.' ), 'src' ) # interactive mode in termnial
SRC_DIR = os.path.dirname( os.path.abspath( __file__) ) # __file__ file property
BASE_DIR = os.path.dirname( SRC_DIR )
DATA_DIR = os.path.join( BASE_DIR, 'data' )

df = pd.read_csv(os.path.join( DATA_DIR, 'travel_insurance.csv'))

# Drop gender --- lot of NaN, não é muito importante para os dados
# Para o modelo, existe muita destination, vou remover

df.drop(['Gender', 'Destination'], axis = 1, inplace = True)

# get dummies
df = pd.get_dummies(data = df, columns= ['Agency', 'Agency_Type', 'Distribution_Channel', 'Product_Name'])

# map claim
df['Claim'] = df.Claim.map({'No': 0, 'Yes': 1})

# net sales negative
df.Net_Sales[df.Net_Sales < 0] = df.Net_Sales[df.Net_Sales > 0].median() 

# age > 118: pela média
df.Age[df.Age > 100]  = df.Age[df.Age < 100].mean()

# negative duration: não tem como, só ta errado mesmo
m = df['Duration'].mean()
s = df['Duration'].std()

df.Duration.loc[df.Duration <= 0] = abs(np.random.normal(m,s))

df.to_csv(os.path.join( DATA_DIR, 'cleaned_travel_insurance.csv'), index = False)