import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('student_habits_performance.csv')

exam_scores = df['exam_score']
study_hours = df['study_hours_per_day']
sleep_hours = df['sleep_hours']

print(exam_scores)

plt.scatter(study_hours,exam_scores)
plt.savefig('GraphA.png')

plt.clf()

plt.scatter(sleep_hours,exam_scores)
plt.savefig('GraphB.png')   