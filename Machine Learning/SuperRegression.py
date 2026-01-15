#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

#Load Data
df = pd.read_csv('student_habits_performance.csv')

df['parental_education_level'] = df['parental_education_level'].replace('None', 'Uneducated')

#Encoding Categorical Columns
df['gender'] = df['gender'].str.lower()
df['diet_quality'] = df['diet_quality'].str.lower()
df['parental_education_level'] = df['parental_education_level'].str.lower()
df['internet_quality'] = df['internet_quality'].str.lower()

df['part_time_job'] = df['part_time_job'].str.lower()
df['extracurricular_participation'] = df['extracurricular_participation'].str.lower()


df = pd.get_dummies(df, columns=['gender'], drop_first=True)


df['diet_quality'] = df['diet_quality'].map({'poor': 0, 'fair': 1, 'good': 2})
df['parental_education_level'] = df['parental_education_level'].map({'uneducated': 0, 'high school': 1, 'bachelor': 2, 'master': 3})
df['internet_quality'] = df['internet_quality'].map({'poor': 0, 'average': 1, 'good': 2})
df['part_time_job'] = df['part_time_job'].map({'yes':1, 'no':0})
df['extracurricular_participation'] = df['extracurricular_participation'].map({'yes':1, 'no':0})

df = df.dropna()

#Independent Variables
x = df.drop(columns=['student_id', 'exam_score'])

#Target
y = df['exam_score']

# Split data into train and test data (80% training data, 20% testing data)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=57)

# Train model using a linear regression
model = LinearRegression()
model.fit(x_train, y_train)

print("Testing Model:", model.score(x_test, y_test))
print("Training Model", model.score(x_train, y_train))

#Predictions
y_pred = model.predict(x_test)

#Graph
plt.scatter(x_test['study_hours_per_day'], y_test)
plt.scatter(x_test['study_hours_per_day'], y_pred)
plt.xlabel("study_hours_per_day")
plt.ylabel("exam_score")
plt.savefig("actual_vs_predictions.png")