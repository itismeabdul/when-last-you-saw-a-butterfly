import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
futuredays = 25
df = pd.read_csv('/storage/emulated/0/Download/monthly_csv.csv')
date = df['Date']
target = df['target']=df['Price'].shift(-futuredays)
x = np.array(df['Price'][:-futuredays])
y = np.array(df['target'][:-futuredays])
train_data, test_data, train_target, test_target = tts(x,y, test_size = 0.1)
tree = DecisionTreeRegressor().fit(train_data.reshape(-1,1),train_target.reshape(-1,1))
print(tree)
lr = LinearRegression().fit(train_data.reshape(-1,1),train_target.reshape(-1,1))
print(lr)

Xfuture = np.array(df['target'][:-futuredays].tail(futuredays)).reshape(-1,1)
print(len(Xfuture))
prediction  = lr.predict(Xfuture)
print(len(prediction))
valid = df[x.shape[0]:]
valid['predictions'] = prediction
print(len(valid['Price']))

plt.figure(figsize=(10,180))
plt.plot(df['Price'][:-futuredays])
plt.plot(valid[['predictions']])
plt.legend(['orginal price','predict'])
plt.show()
