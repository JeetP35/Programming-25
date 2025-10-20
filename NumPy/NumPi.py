import numpy as np
import math

def estimatePi(points):
    x = np.random.random(points)
    y = np.random.random(points)
    inside = (x**2 + y**2) <= 1
    pi = 4 * np.sum(inside) / points
    return pi

def nextEstimate(points, accuracy):
    pi_est = estimatePi(points)
    difference = abs(pi_est - math.pi)
    if difference <= accuracy:
        return points, pi_est
    else:
        return nextEstimate(points * 2, accuracy)

def main():
    accuracy = 1e-8
    points = 1000
    points, pi_est = nextEstimate(points, accuracy)
    print(f"\nFinal π ≈ {pi_est} with {points} points (accuracy ±{accuracy})")

main()