import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Demos.FileSecurityTest import permissions_dir_inherit

df = pd.read_csv('../dataset/USA_Housing.csv')
df = df.drop("Address", axis=1)
print(df.head())

print(df.info())

print(df.describe())

sns.heatmap(df.corr())

print(df.columns)

X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms','Avg. Area Number of Bedrooms', 'Area Population']]
y = df['Price']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=101)

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train,y_train)

predictions = lm.predict(X_test)
print("Kết quả predict 20%:")
print(predictions)

pre1=lm.predict([X_test.iloc[1]])
print("kết quả pre1 =",pre1)

pre2=lm.predict([[66774.995817,5.717143,7.795215,4.320000,36788.980327]])
print("kết quả pre2 =",pre2)

print(lm.intercept_)
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
print(coeff_df)

from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

import pickle
modelname = "../trainmodel/housingmodel.zip"
pickle.dump(lm, open(modelname, 'wb'))