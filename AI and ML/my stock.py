import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
import matplotlib.pyplot as plt


df = pd.read_csv('/storage/emulated/0/Download/daily_csv.csv', nrows=3000)
futuredays = 300
target = df['target']=df['Price'].shift(-5)
x = np.array(df['Price'][:-futuredays])
y = np.array(df['target'][:-futuredays])
train_data, test_data, train_target, test_target = tts(x,y, test_size = 0.1)
lr = LinearRegression()
train = lr.fit(train_data.reshape(-1,1),train_target.reshape(-1,1))

Xfuture = np.array(df['Price'].tail(futuredays)).reshape(-1,1)
print(Xfuture)
prediction = lr.predict(Xfuture)

valid = df.tail(futuredays)
print(len(prediction))
print(len(valid['Price']))
valid['predictions'] = prediction

plt.figure(figsize=(10,180))
plt.plot(df['Price'][:-futuredays])
plt.plot(valid[['Price','predictions']])
plt.legend(['orginal price','predict'])
plt.show()

print(df.tail(25))
print(valid)
print()
print()
#print(valid)






