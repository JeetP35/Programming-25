import numpy as np

def estimate_pi(n):
    x = np.random.rand(n)
    y = np.random.rand(n)
    inside_circle = (x ** 2 + y ** 2) <= 1
    r = np.sum(inside_circle)
    return 4 * r / n

n = 1000000
pi_value = estimate_pi(n)
print("Estimated π =", pi_value)
