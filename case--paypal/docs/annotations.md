# Understanding Travel Insurance Market

## Links
- https://www.globenewswire.com/news-release/2021/05/13/2228941/0/en/Travel-Insurance-Market-Size-to-Reach-USD-40-Billion-by-2028-Policy-Types-Coverage-Benefits-Risk-Analysis-Service-Providers-Investment-Statistics-and-Upcoming-Opportunities-Adroit-.html

- https://www.melhoresdestinos.com.br/seguro-viagem-dicas.html

- https://www.alliedmarketresearch.com/travel-insurance-market


## Annotations
- O data set é de uma intermediária de seguro de viagem, ganha comissão em cima da venda de apólices.
- Você assina o seguro, assim como o seguro de carro e paga por isso, mas o seguro nem sempre é chamado (Claim), e lembrando: ele **ser chamado** é o que NÃO queremos ou é o que queremos estar o mais preparado possível, por isso precisamos reconhecer os riscos do assegurado. (Importante saber se o assegurado tem problemas de coração por exemplo, pois isso pode influenciar a depender do plano)
- Travel insurance covers the expenses incurred and minimizes the risks during travel.
- Size to Reach USD 40 billion by 2028
- Pegged at \$21 billion in 2019
- Tourism with 25% of total share in international services
- Rising number of millennials
- Increasing disposable incomes
- Decreasing flight rates
- Easy payments options
- Rising tourism promotion activities
- "Insurance providers are increasing their value-added services to achieve product differentiation from their competitors and to maintain better customer relationships"
- Data analytics to predict risks and formulate contigency plans
- "Geographically, Asia Pacific held the largest share in global travel insurance market. This has been attributed to the high demand for corporate travel insurance from countries such as China, Japan and Korea." 
- Difference between airlines and travel agencies?
- Histórico de acidentes da pessoa?



# Annotations about data

## About Duration
- I think that Duration is in **minutes**. 
- Has negative duration and very low duration, this is because timezone differece?
- There are specific five observations with negative Duration, and there are a pattern: four countries are in South Asia, and the fifth is China. Why?
- *Thinking*: I could discovery what is the origin of travel with an algorithm that calculate the possibly country of origin from the Duration feature (Am I dreaming too much????)
- All Basic plan
- All online
- All JZI agency
- All Airlines agency type
- All Basic plan
- No claim
- Net sales is 22 (BANGLADESH and CHINA) or 18 (MALAYSIA, BRUNEI DARUSSALAM and INDONESIA) 
- Comission is 7.7 BANGLADESH and CHINA) or 6.3 (MALAYSIA, BRUNEI DARUSSALAM and INDONESIA)
- Age is 118 (very strange) 
- Age is 118 (very strange) 
- Age is 118 (very strange) 
- Age is 118 (very strange) 
- Age is 118 (very strange) 
- Age is 118 (very strange) 
- Age is 118 (very strange) 
- Age is 118 (very strange) 
- Age is 118 (very strange) 
- Age is 118 (very strange) 

## About age
 - 5 outilers observations
 - Mostly between 30 and 40 years old, 36y is the most commom
 - 36y with 38% of observations
 - 984 with 118y
 - 0y are the same people, unique change is in Net_Sales (+30 and -30). Cancellation of travel?
 - Maximum age is 88y -- without outlier
 - 

## About Net Sales

- There are negative net sales, don't make sense. Exclude? Fill them?

## About Gender
- There are 71,22% of missing values. It's complicated. Drop all? Replace with __? It's importante to analysis?
  

## Mediana de X por Y

## Por Tipo de agência
### Idade
  - Airlines > Travel Agency, o primeiro passa dos 40 e o segundo nem chega a 40

### Commision
  - Airlines > Travel Agency, mediana de comissão chega perto 16 do primeiro, do segundo ... zero

### Duration
  - Travel Agency > Airlines, primeiro chega pertor dos 25, segundo crava nos 20

### Net Sales
  -  Airlines > Travel Agency, primeiro passa dos 25, segundo passa também mas ta menor

## Por Claim
- No == Yes, é igual no caso

### Commission
- Yes > No, muito maior, com mediana em 25, e 'No' em zero

### Duration
- Yes > No, com mediana maior que 35 e 'No' maior que 20 e menor que 25

### Net Sales
- Yes > NO, mediana passa dos 50, 'No' perto dos 25 

## Por gênero

### Idade
- M > F, M > 40,  35 < F > 40

### Commision
- F > M, M perto dos 10, F passa dos 10

### Duration
- F > M, F == 25, M == 17

### Net sales
- Posso jurar que são iguais

## Por canal de distribuição

### Idade
- Off > On, Off > 55, 40 > On > 35

### Commision
- Off > 0n, Off > 10, On == 0

### Duration
- Off > On, Off > 40, On pouco maior que 20

### Net Sales
 - Off > On, Off == 30, On > 25

## Por agência

### Idade
 - EPX chega quase nos 120..., é quase tudo igual entre 20 e 40, unicos que passam de 60 são CSR, CCR e CBH, a com idade mais nova é a ADM

### Commision
- ADM (~35) > LWX (~32) > CWT (~27) > JWT (~16) > KML(~15), depois tudo mais ou menos igual abaixo dos 10, a pior agência é a TTW (com zero) e TST (~2 ou 3)

### Duration
- TTW > 350, ganha disparado, por que? É a que tem comissão zero!
- CBH (~60) > CSR (~57) > CCR (~48) > SSI(~47), depois tudo mais ou menos igual, o menor é o RAB

### Net Sales
- TTW (~97) > ADM (~75) > LWC (~46) > [CWT, JWT, KML, C2B], a pior é a SSI (~4) 

## Por product name

## Por destination

### Idade
 - Virgin island(~52) > GUAM == IRAN (~48) > BERMUDA > NOTHERN MARIANA > GUINEA (~45)
 - Ignorando 118 de TIBET e KOREA, DEMOCRATIC...

### Commision
  - REUNION (~44.5) > BOSNIA (~41) > MAURITIUS (~35) > SLOVENIA (~32)

### Duration
   - ARMENIA (~232) > PERU (~186) > SIERRA LEONE (~161) > MALI (~131)
 - 
### NET SALES
-  TURKS AND CAICOS ISLANDS -   128.0
-  TAJIKISTAN, CAMEROON, SAMOA, GUATEMALA, PUERTO RICO == 112
-  TURKMENISTAN      -           99.5
- PANAMA                -       96.0
- CAYMAN ISLANDS        -       96.0
- CYPRUS               -        89.1
- FRENCH POLYNESIA       -      89.0
- KYRGYZSTAN             -      86.0
- BULGARIA              -       83.0
- ALBANIA                -      80.0
- CHILE                  -      80.0
- HUNGARY                -      80.0
- GUINEA-BISSAU          -      80.0
- DOMINICAN REPUBLIC      -     80.0
- SIERRA LEONE            -     80.0
- BOTSWANA                -     80.0
- UKRAINE                 -     80.0
- BERMUDA                 -     80.0
- VENEZUELA               -     80.0
- VIRGIN ISLANDS, U.S.    -     80.0
- SENEGAL                  -    80.0
- MOROCCO                  -    79.0
- ISRAEL                   -    76.5
- COLOMBIA                 -    75.0
- CANADA                   -    71.0 
 

## Dos que Claim == Yes

 Agency Type   | Duration   | Net_Sales   | Commision | Age
-------------  | -------    | -------     | -------   | -------- 
Airlines       | 134.984772 | 111.401421  | 28.200677 | 38.529611
Travel Agency  | 68.229167  | 64.425149   | 21.705446 | 38.818452

 Product_Name                        |  Duration  | Net_Sales  | Commision  |      Age
-----------------------------        | -----------| ---------- | ---------- | ----------  
1 way Comprehensive Plan             |  40.777778 |  40.000000 |   0.000000 | 54.111111
2 way Comprehensive Plan             |  55.077465 |  54.000000 |   0.000000 | 38.070423
Annual Gold Plan                     | 372.619048 | 350.176190 |  87.544762 | 40.714286
Annual Silver Plan                   | 371.636943 | 235.072930 |  58.767261 | 39.031847
Annual Travel Protect Gold           | 371.600000 | 253.505000 | 164.778000 | 38.900000
Annual Travel Protect Platinum       | 383.333333 | 323.400000 | 210.210000 | 39.000000
Annual Travel Protect Silver         | 368.500000 | 213.600000 | 138.840000 | 37.000000
Basic Plan                           |  35.217391 |  27.869565 |  10.423913 | 44.565217
Bronze Plan                          |  30.714286 |  41.968810 |  10.493857 | 35.752381
Cancellation Plan                    |  54.250000 |  29.431818 |   0.000000 | 35.022727
Comprehensive Plan                   |  43.200000 |  29.000000 |   9.570000 | 58.000000
Gold Plan                            |  40.166667 |  84.058333 |  21.016111 | 44.388889
Individual Comprehensive Plan        | 364.333333 |  97.000000 |   0.000000 | 35.333333
Premier Plan                         |  10.333333 |  51.000000 |  19.380000 | 43.666667
Rental Vehicle Excess Insurance      |  40.744186 |  72.293023 |  43.375814 | 37.581395
Silver Plan                          |  32.836879 |  67.166667 |  16.794326 | 36.390071
Single Trip Travel Protect Gold      |  26.500000 |  44.950000 |  29.220000 | 40.300000
Single Trip Travel Protect Platinum  |  17.200000 |  46.100000 |  29.966000 | 43.200000
Single Trip Travel Protect Silver    |  47.500000 |  31.250000 |  20.315000 | 56.750000
Spouse or Parents Comprehensive Plan | 366.000000 |  86.000000 |   0.000000 | 38.0000  00
Ticket Protector                     |  43  .428571 |   8.870000 |   2.485714 | 48.00000  0
Travel Cruise Protect                |  24.000000 |  30.000000 |  10.500000 | 36.00000  0
Value Plan                           |  47.263158 |  67.631579 |  24.905789 | 64.684211


Distribution_Channel  |  Duration   | Net_Sales | Commision |    Age
-------------------   | ----------- | --------- | --------- | ----------      
Offline               |  106.411765 | 47.176471 |  4.698235 | 62.823529
Online                |  110.870330 | 95.256143 | 26.241495 | 38.182418
## Additional importante features

- Origin of travel: this would explain negatives duration.


## Molde PyCaret
Symbol   |                            Model|Accuracy|  AUC   | Recall | Prec.  |  F1    | Kappa  |   MCC  |TT (Sec) 
-------- | ------------------------------- | ------ | ------ | ------ | -----  | ------ | ------ | ------ | ------
lr       |             Logistic Regression | 0.8127 | 0.8276 | 0.6920 | 0.0515 | 0.0959 | 0.0711 | 0.1527 | 4.927   
lda      |    Linear Discriminant Analysis | 0.8326 | 0.8273 | 0.6620 | 0.0552 | 0.1019 | 0.0775 | 0.1566 | 0.504   
gbc      |    Gradient Boosting Classifier | 0.8856 | 0.8221 | 0.5550 | 0.0685 | 0.1219 | 0.0989 | 0.1651 | 6.190   
ada      |            Ada Boost Classifier | 0.8545 | 0.8205 | 0.6022 | 0.0580 | 0.1058 | 0.0818 | 0.1537 | 1.663   
lightgbm | Light Gradient Boosting Machine | 0.9606 | 0.7999 | 0.1886 | 0.0899 | 0.1216 | 0.1042 | 0.1117 | 0.553   
nb       |                     Naive Bayes | 0.5229 | 0.7995 | 0.8868 | 0.0261 | 0.0506 | 0.0234 | 0.0962 | 0.083   
rf       |        Random Forest Classifier | 0.9693 | 0.7170 | 0.0722 | 0.0562 | 0.0629 | 0.0477 | 0.0482 | 3.183   
et       |          Extra Trees Classifier | 0.9662 | 0.6786 | 0.0832 | 0.0553 | 0.0663 | 0.0499 | 0.0510 | 3.676   
knn      |          K Neighbors Classifier | 0.8756 | 0.6167 | 0.3016 | 0.0367 | 0.0654 | 0.0409 | 0.0685 | 0.825   
dt       |        Decision Tree Classifier | 0.9629 | 0.5366 | 0.0958 | 0.0535 | 0.0685 | 0.0511 | 0.0535 | 0.287   
qda      | Quadratic Discriminant Analysis | 0.0267 | 0.5024 | 0.9921 | 0.0144 | 0.0284 | 0.0001 | 0.0065 | 0.350   
svm      |             SVM - Linear Kernel | 0.6244 | 0.0000 | 0.7893 | 0.0348 | 0.0660 | 0.0397 | 0.1106 | 0.658   
ridge    |                Ridge Classifier | 0.8326 | 0.0000 | 0.6620 | 0.0552 | 0.1019 | 0.0775 | 0.1566 | 0.086  