import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

df = pd.read_csv("medical_insurance.csv")

df = df.dropna()

df['sex'] = df['sex'].str.lower()
df['smoker'] = df['smoker'].str.lower()
df['region'] = df['region'].str.lower()

df = pd.get_dummies(df, columns=['region'], drop_first=True)
# 0 0 0 = northeast
# 1 0 0 = northwest
# 0 1 0 = southeast
# 0 0 1 = southwest

df[['sex', 'smoker']] = OrdinalEncoder().fit_transform(df[['sex', 'smoker']])
df['bmi_smoker'] = df['bmi'] * df['smoker']
df['bmi_age'] = df['bmi'] * df['age']
df['age_smoker'] = df['age'] * df['smoker']

#Independent
x = df[['age', 'sex', 'bmi', 'children', 'smoker', 'bmi_smoker', 'bmi_age', 'age_smoker', 'region_northwest', 'region_southeast', 'region_southwest']]

#Dependent
y = df['charges']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=57)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)



print("Training Model:", model.score(x_train, y_train))
print("Testing Model:", model.score(x_test, y_test))

plt.scatter(x_test['bmi'], y_test)
plt.scatter(x_test['bmi'], y_pred)
plt.xlabel("bmi")
plt.ylabel("charges")
plt.savefig("bmi_vs_charges.png")
plt.clf()
plt.scatter(x_test['bmi_age'], y_test)
plt.scatter(x_test['bmi_age'], y_pred)
plt.xlabel("bmi_age")
plt.ylabel("charges")
plt.savefig("bmi_age_vs_charges.png")
plt.clf()
plt.scatter(x_test['bmi_smoker'], y_test)
plt.scatter(x_test['bmi_smoker'], y_pred)
plt.xlabel("bmi_smoker")
plt.ylabel("charges")
plt.savefig("bmi_smoker_vs_charges.png")
plt.clf()
plt.scatter(x_test['age_smoker'], y_test)
plt.scatter(x_test['age_smoker'], y_pred)
plt.xlabel("age_smoker")
plt.ylabel("charges")
plt.savefig("age_smoker_vs_charges.png")
plt.clf()
plt.scatter(x_test['age'], y_test)
plt.scatter(x_test['age'], y_pred)
plt.xlabel("age")
plt.ylabel("charges")
plt.savefig("age_vs_charges.png")