import numpy as np
import matplotlib.pyplot as plt

def generateRandomWave(n, xMin, xMax, iter = 1000):
    x = np.linspace(xMin, xMax, iter)
    a = np.random.rand(n)
    b = np.random.rand(n)
    y = np.zeros((n, iter))

    for i in range(n):
        y[i] = a[i] * np.sin(b[i] * x)
        plt.plot(x, y[i])

    plt.savefig('waves.png')
    plt.clf()

    y_sum = np.sum(y, axis = 0)
    plt.plot(x, y_sum)
    plt.savefig('resultantWave.png')

generateRandomWave(5, 0, 100)