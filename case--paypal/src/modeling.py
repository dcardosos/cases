import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from pycaret.classification import *    
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from imblearn.over_sampling import SMOTE
from sklearn.feature_selection import RFE
import os

SRC_DIR = os.path.join( os.path.abspath( '.' ), 'src' ) # interactive mode in termnial
SRC_DIR = os.path.dirname( os.path.abspath( __file__) ) # __file__ file property
BASE_DIR = os.path.dirname( SRC_DIR )
DATA_DIR = os.path.join( BASE_DIR, 'data' )
IMG_DIR = os.path.join( BASE_DIR, 'figs')

df = pd.read_csv(os.path.join( DATA_DIR, 'cleaned_travel_insurance.csv'))

target = df['Claim'].values
X = df.drop('Claim', axis = 1)

X_train, X_test, y_train, y_test = train_test_split(X, target, random_state= 146, test_size = .3, stratify = target)

dt = DecisionTreeClassifier()

dt.fit(X, target)

importance = dt.feature_importances_

for i,v in enumerate(importance):
	print('Feature: %0d, Score: %.5f' % (i,v))
# plot feature importance
plt.bar([x for x in range(len(importance))], importance)
plt.show()
X.iloc[:, [0, 1, 2, 3]]

clf = LogisticRegression()
clf.fit(X_train, y_train)
clf.score(X_train, y_train)

y_pred = clf.predict(X_test)

confusion_matrix(y_test, y_pred)

### SMOTE
smote = SMOTE() 

X_train_smoted, y_train_smoted = smote.fit_resample(X_train, y_train)
X_test_smoted, y_test_smoted = smote.fit_resample(X_test, y_test)

model = DecisionTreeClassifier()

model.fit(X_train_smoted, y_train_smoted)

importance = model.feature_importances_

for i,v in enumerate(importance):
	print('Feature: %0d, Score: %.5f' % (i,v))
# plot feature importance
plt.bar([x for x in range(len(importance))], importance)
plt.show()



clf.fit(X_train_smoted, y_train_smoted)

clf.score(X_test_smoted, y_test_smoted)

y_pred_smoted = clf.predict(X_test_smoted)

confusion_matrix(y_test_smoted, y_pred_smoted)

## feature importance



## Pycaret classification

exp_clf = setup(df, target= 'Claim', html= False, fix_imbalance = True)

best = compare_models(sort = 'AUC')

lightgbm = create_model('lightgbm')
gbc = create_model('gbc')


plot_model(lightgbm)
