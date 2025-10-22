import numpy as np
# import math

def estimatePi(points):
    x = np.random.random(points)
    y = np.random.random(points)
    inside = (x**2 + y**2) <= 1
    pi_est = 4 * np.sum(inside) / points
    print(f"Estimated value of Pi with {points} points: {pi_est}")
    return

estimatePi(100000000)