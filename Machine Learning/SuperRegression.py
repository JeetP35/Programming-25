#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

#Load Data
df = pd.read_csv('student_habits_performance.csv')

#Encoding Categorical Columns
categorical_columns = ['gender', 'diet_quality', 'parental_education_level', 'internet_quality']
df[categorical_columns] = OrdinalEncoder().fit_transform(df[categorical_columns])

df['part_time_job'] = df['part_time_job'].str.lower()
df['extracurricular_participation'] = df['extracurricular_participation'].str.lower()

df['part_time_job'] = df['part_time_job'].map({'yes':1, "no":0})
df['extracurricular_participation'] = df['extracurricular_participation'].map({'yes':1, "no":0})

#Independent Variables
x = df[['age','gender','study_hours_per_day','social_media_hours','netflix_hours',
        'part_time_job','attendance_percentage','sleep_hours','diet_quality',
        'exercise_frequency','parental_education_level','internet_quality',
        'mental_health_rating','extracurricular_participation']]

#Target
y = df['exam_score']

df = df.dropna()

# Split data into train and test data (80% training data, 20% testing data)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=57)

# Train model using a linear regression
model = LinearRegression()
model.fit(x_train, y_train)

print("Testing Model:", model.score(x_test, y_test))
print("Training Model:", model.score(x_train, y_train))

#Predictions
y_pred = model.predict(x_train)

#Graph
plt.scatter(x_train['study_hours_per_day'], y_train)
plt.scatter(x_train['study_hours_per_day'], y_pred)
plt.xlabel("study_hours_per_day")
plt.ylabel("exam_score")
plt.savefig("training_vs_testing_predictions.png")
