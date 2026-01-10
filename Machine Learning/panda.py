import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('student_habits_performance.csv')

exam_scores = df['exam_score']
study_hours = df['study_hours_per_day']
sleep_hours = df['sleep_hours']

#Part 1
plt.scatter(study_hours,exam_scores)
plt.savefig('examScore_and_studyHours.png')

plt.clf() #Clearing Figure

plt.scatter(sleep_hours,exam_scores)
plt.savefig('examScore_and_sleepHours.png')

#Part 2
def calculate(min_hours):
  min_hours = float(min_hours)
  if min_hours < 0:
    print("Error: study hours cannot be negative")
    return
  
  student = df[study_hours >= min_hours]

  if len(student) == 0:
    print(f"no student studied for that {min_hours} hours")
    return
  passed_students = df[(study_hours >= min_hours) & (exam_scores > 50)]
  success_percentage = (len(passed_students) / len(student)) * 100
  return success_percentage

hours = input("Enter the number of study hours : ")
result = calculate(hours)
if result is not None:
  print(f"{result}% of students who study for atleast {hours} hours a day passed the exam.")