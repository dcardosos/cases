import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.style.use('ggplot')

# Address constants
SRC_DIR = os.path.join( os.path.abspath( '.' ), 'src' ) # interactive mode in termnial
SRC_DIR = os.path.dirname( os.path.abspath( __file__) ) # __file__ file property
BASE_DIR = os.path.dirname( SRC_DIR )
DATA_DIR = os.path.join( BASE_DIR, 'data' )
IMG_DIR = os.path.join( BASE_DIR, 'figs')

# Function to save plots
def save_plot(filename):
    plt.savefig(os.path.join( IMG_DIR, filename)) 

# Data reading
df = pd.read_excel(os.path.join( DATA_DIR, 'travel insurance.xlsx'), engine='openpyxl')

# Dimensonality and types of data
print(f'Dataframe shape (rows, columns)-> {df.shape}')
print(df.dtypes)

# Change column names
df.columns = df.columns.str.replace(' ', '_')
df.rename(columns = {'Commision_(in_value)': 'Commision'}, inplace = True)

df.to_csv(os.path.join( DATA_DIR, 'travel_insurance.csv'), sep = ',', index = False)
# Cat and num features
cat_features = df.select_dtypes('object').columns.tolist() # categoric features
num_features = set( df.columns ) - set( cat_features )     # numeric features

# Missing values
print(df.isna().sum())

## % of NaN per column
print( df.isna().sum() / df.shape[0] ) # 71,22% of missing value in Gender feature

# Correlação
sns.pairplot(df, hue = 'Claim');  # não há correlação clara entre as features
save_plot('pairplot_by_claim') 
plt.show()

## Heatmap
### Forte correlação entre Net_Sales e Comission
df_corr = df[ num_features ].corr()
mask = np.triu(np.ones_like(df_corr, dtype=bool))

sns.heatmap(df_corr, mask = mask)
save_plot('heatmap_numeric_features')
plt.show()

df[['Net_Sales', 'Commision']].corr(method= 'kendall')

# Describe stats
df.describe()    # negative duration, net_sales? age zero?  

## Describe all categoric features
df[cat_features].describe()         # 2 uniques: agency_type, channel, claim and gender 

# Duration
## Negative duration because timezone difference? How to count this?
df[ 'Duration' ].unique()  # in minutes, probably ---- -2, -1, 0, 1, 2

### Investigate --- we have five observations with negative duration
def investigate_negative_duration(col):
    '''
    Return dataframe with values that has negative duration

    param:
        col (string): Name of column to analyze

    return:
        series and print unique values
    '''
    d = df[df.loc[:, 'Duration'] < 0][col]
    print(f'Unique values for {col} feature: {d.unique()}\n')

    return(d)

## We have a pattern!
list(map(investigate_negative_duration, df.columns.tolist()))

# Age
sns.histplot(df, x = 'Age')   ## som 118 ages 
plt.show()

df[df.Age > 100].Age.count() ### 984 peoples with > 110 years old
df[df.Age > 100].Age.unique() ### all is 118y

## data frame withot outliers for better visualization
outlier = max(df['Age'])
without_outlier =  df[ df['Age'].apply( lambda x: x < outlier ) ]

sns.histplot( without_outlier, x = 'Age' )
plt.show()

## quantity
### mostly between 30 and 40 years old, 36y is the most commom (38% of observations)
df['Age'].value_counts() / df.shape[0] 

### maximum age is 88y -- without outlier
sorted(df['Age'].unique())

## age 0
### net sales 30 negative, and 30 positive, the rest is the same
### cancellation of travel?           
df[df.Age == 0][num_features]

# Net Sales
sns.histplot(df['Net_Sales'])  # histplot meio distorcido
plt.show()


df['Net_Sales'].describe()     # negative net sales ?????

sns.histplot(df[ df['Net_Sales'] > 0]['Net_Sales'])
plt.show()       # 678 observations with negative net sales

### parece ser erro
df[ df['Net_Sales'] < 0 ]['Product_Name'].value_counts() /  df[ df['Net_Sales'] < 0 ].shape[0]  

df['Product_Name'].value_counts() / df.shape[0]

df[ df['Net_Sales'] < 0 ]['Commision'].hist(bins= 10); plt.show()

df['Commision'].hist(bins= 10); plt.show()

sns.regplot(x = 'Commision', y = 'Net_Sales', data = df[ df['Net_Sales'] > 0 ]); 
save_plot('regplot_commission_netsales_positive_values')
plt.show()

# Commision
df['Commision'].describe()   ### desvio padrão alto, mediana zero?

df['Commision'].hist(); plt.show()

df['Commision'].value_counts()   ## 0]: 35217 observacoes
df[df['Commision'] == float(0)]['Claim'].value_counts()   ## a maioria é claim zero obvio


#### Distribuição de variáveis
df['Claim'].value_counts() / df.shape[0]   # 98,54% No, e 1,46 % Yes

def countplot_general( x ):
    
    sns.countplot(x = x, data = df)
    
    save_plot(f'{x}_countplot_general')
    
    plt.show() 


def countplot_claimed( x ):
    
    sns.countplot(x = x, data = df[df['Claim'] == 'Yes'])
    
    save_plot(f'{x}_countplot_claimed')
    
    plt.show()

list(map(countplot_general, df[set(cat_features) - set(['Product_Name', 'Destination'])]))

list(map(countplot_claimed, df[set(cat_features) - set(['Product_Name', 'Destination', 'Claim'])]))

### pra product name e destination
#### prod name: cancellation, 2way comprehensive, rental car, basic, bronze, 1way comprehensive
df['Product_Name'].value_counts().plot(kind = 'barh'); 
plt.tight_layout(); 
save_plot('product_name_barh')
plt.show()

#### destination
##### reading a list with right countries name
raw_data_url = 'https://gist.githubusercontent.com/kalinchernev/486393efcca01623b18d/raw/daa24c9fea66afb7d68f8d69f0c4b8eeb9406e83/countries'
list_country_names = pd.read_csv(raw_data_url, sep = '\n', header= None)[0].values.tolist()

df['Destination'].value_counts()[:30].plot(kind = 'barh'); 
save_plot('large_30_count_destination')
plt.show()


#### Describe by claim
def claimed_describe(col):
    return(df.groupby('Claim')[col].describe().drop('count', axis = 1))

claimed_describe('Age')         # nada de mto diferente
claimed_describe('Duration')    # media bem maior mas porque o std é grande tbm, mediana 16 pontos maior  
claimed_describe('Commision')   #  comissao bem maior, obvio
claimed_describe('Net_Sales')   # mais vendas, media == std, mediana alta