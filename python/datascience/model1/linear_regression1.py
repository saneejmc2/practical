import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 

df = pd.read_csv('House_Price.csv')

print(df) 
print(df['crime_rate'])

x = pd.DataFrame(df['crime_rate'])
print(x)
y = pd.DataFrame(df['price'])
print(y)

sc = StandardScaler()
X_scaled = sc.fit_transform(x)
#print(X_scaled)
X_train,X_test,Y_train,Y_test = train_test_split(X_scaled,y,test_size=0.3,random_state=42)

lr = LinearRegression()
lr.fit(X_train,Y_train)
pred = lr.predict(X_scaled)

k = pd.DataFrame(pred)
print(k)

y_scaled=sc.fit_transform(y)

plt.plot(y,pred)
plt.show()