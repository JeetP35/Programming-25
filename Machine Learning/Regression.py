import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Load Data
df = pd.read_csv('student_habits_performance.csv')

x = df['study_hours_per_day'].to_numpy()
y = df['exam_score'].to_numpy()

#values
m = 0.0
b = 0.0
h = 1e-5
rate = 0.001
tolerance = 1e-6

#predicting y
def ypredict(x,m,b):
  return m * x + b

#calculating mse
def mse(y_data,y_pred):
  return np.mean((y_data - y_pred)**2)

y_predict = ypredict(x,m,b)
mse_value = mse(y,y_predict)

while True:
  mse_nudge_m = mse(y, ypredict(x, m+h, b))
  mse_nudge_b = mse(y, ypredict(x, m, b+h))

  slope_m = (mse_nudge_m - mse_value) / h
  slope_b = (mse_nudge_b - mse_value) / h
  m -= rate * slope_m
  b -= rate * slope_b

  new_y_predict = ypredict(x, m, b)

  new_mse = mse(y, new_y_predict)

  if abs(mse_value - new_mse) < tolerance:
    break

  mse_value = new_mse

print("Final b value:", b)
print("Final m value:", m)
print("Final mse", new_mse)

#plotting final result
plt.scatter(x,y)
plt.plot(x, ypredict(x,m,b))
plt.xlabel("study_hours_per_day")
plt.ylabel("exam_score")
# plt.ylim(0,100)
plt.savefig("Exam Score vs Study Hours")
plt.clf()
plt.plot(x, ypredict(x,m,b))
plt.xlabel("study_hours_per_day")
plt.ylabel("exam_score")
# plt.ylim(0,100)
plt.savefig("Exam Score vs Study Hours (line of best fit)")