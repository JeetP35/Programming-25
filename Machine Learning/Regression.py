import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('student_habits_performance.csv')

x = np.array([1, 2, 2.5, 3, 4, 4.5, 5, 6, 7, 8, 9])
y_data = np.array([33, 41, 45, 51, 62, 68, 74, 80, 85, 90, 97])
b = 30
m = 7
h = 1e-5

def ypredict(x,m,b):
  return m * x + b

def mse(y_data,y_pred):
  return np.mean((y_data - y_pred)**2)

mse_init = mse(y_data, ypredict(x,m,b))

mse_nudge_m = mse(y_data, ypredict(x,m+h,b))
mse_nudge_b = mse(y_data, ypredict(x,m,b+h))

m_slope = (mse_nudge_m - mse_init)/h
b_slope = (mse_nudge_b - mse_init)/h

print('initial mse is:', mse_init)
print('mse after m is nudged by h is:', mse_nudge_m)
print('mse after b is nudged by h is:', mse_nudge_b)
print('slope along the m axis is:', m_slope)
print('slope along the b axis is:',b_slope)