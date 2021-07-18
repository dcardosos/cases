import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.parsers import read_csv
import seaborn as sns
import os
import statsmodels.api as sm

plt.style.use('ggplot')

# Address constants
SRC_DIR = os.path.join( os.path.abspath( '.' ), 'src' ) # interactive mode in termnial
SRC_DIR = os.path.dirname( os.path.abspath( __file__) ) # __file__ file property
BASE_DIR = os.path.dirname( SRC_DIR )
DATA_DIR = os.path.join( BASE_DIR, 'data' )
IMG_DIR = os.path.join( BASE_DIR, 'figs')
IMG_BUSINESS_DIR = os.path.join ( IMG_DIR, 'business/')

df = pd.read_csv(os.path.join( DATA_DIR, 'travel_insurance.csv'))

class NumFeatureAnalysis:

    def __init__(self, dataframe):

        self.df = dataframe
        self.columns = dataframe.columns
        self.cat_features = dataframe.select_dtypes('object').columns.tolist()
        self.num_features = list(set( dataframe.columns ) - set( self.cat_features ))

    def mean_values(self, colname):
        
        return(df.groupby(colname)[self.num_features].mean())

    def median_values(self, colname):
        
        return(df.groupby(colname)[self.num_features].median())

    def plot_by_feature(self, colname):

        pass

dfa = NumFeatureAnalysis(df)

# Analisar por Agency, Agency_Type, Claim, Channel e Gender

# Bar plot horizontal
def barh_plot(by_what, col):
    by_what[col].plot(kind = 'barh')
    plt.xlabel(col)
    plt.show()

# Para printar o bar plot dado um dataframe agrupado por algo e uma coluna
def print_plot(plot_function, by_what, col):

    plot_function(by_what, col)

# Retirando Destination porque são muito grandes
cat_features = set(dfa.cat_features) - set(['Destination'])

# Dicionario com key sendo o by_col da vez, e o value sendo o data frame com os elementos
# do by_col da vez no index e as colunas sendo as cat_features definida anterioremente
by_catfeature_dict = {f'by_{i}' : dfa.median_values(i) for i in cat_features}

# Para cada dataframe criado, plotar o barh
for k, v in by_catfeature_dict.items():
    for num in dfa.num_features:
        print_plot(barh_plot, v, num)


# Analisar separadamente Destination
by_destination = dfa.median_values('Destination')

## Age
by_destination['Age'].describe()
by_destination['Age'].sort_values(ascending=False)[2:30]  # ignorar 118 anos

### idade de 118
df[df['Age'] == 118]['Claim'].value_counts() ### temos idade 118 e 10 claim yes, é importante

## Commision
by_destination['Commision'].sort_values(ascending= False)[:30]

## Duration
by_destination['Duration'].sort_values(ascending= False)[:30]

## Net Sales
by_destination['Net_Sales'].sort_values(ascending= False)[:30]

# Analisar com claim
## barh plot modificado
def barh_plot_claim(col):

    grouped_claim = df.groupby('Claim').get_group('Yes')[col].value_counts()
    grouped_claim.plot(kind = 'barh')
    plt.xlabel(col)
    plt.show()

list(map(barh_plot_claim, dfa.cat_features))
 

## Claim yes
claimed = df.groupby('Claim').get_group('Yes')

lista_claimed = [claimed.groupby('Agency_Type').median(),
                 claimed.groupby('Product_Name').median(),
                 claimed.groupby('Distribution_Channel').median(),
                 claimed.groupby('Agency').median()]

for l in lista_claimed:
    for num in dfa.num_features:
            print_plot(barh_plot, l, num)

sns.barplot()

dfa.df['Product_Name'].value_counts().to_csv(
    os.path.join(DATA_DIR, 'product_name_value_counts.csv'), index = False)


dfa.df['Product_Name'].value_counts().index.tolist()

dfa.df.groupby('Product_Name')[['Net_Sales', 'Commision']].sum().sort_values(
    by = 'Net_Sales', ascending= False)

dfa.df.groupby('Agency')[['Net_Sales', 'Commision']].sum().sort_values(
    by = 'Net_Sales', ascending= False)



dfa.df.groupby('Agency_Type')[['Net_Sales', 'Commision']].sum().sort_values(
    by = 'Net_Sales', ascending= False)


dfa.df['Claim'].value_counts() / dfa.df['Claim'].value_counts().sum()