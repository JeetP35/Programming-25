import numpy as np
import matplotlib.pyplot as plt

def generateRule184(m, n):
    rule184Array = np.zeros((m, n), dtype=int)
    rule184Array[0] = np.random.randint(0, 2, n)

    for generate in range(1, m):
        left = np.roll(rule184Array[generate - 1], 1)
        center = rule184Array[generate - 1]
        right = np.roll(rule184Array[generate - 1], -1)
        move_in = (left == 1) & (center == 0)
        move_out = (center == 1) & (right == 0)
        next_gen = ((center & ~move_out) | move_in) * 1
        rule184Array[generate] = next_gen

    return rule184Array

def main():
    m = 100
    n = 100
    rule184Array = generateRule184(m, n)
    plt.imshow(rule184Array, cmap='gray', interpolation='nearest')
    plt.title('Rule 184')
    plt.savefig("My_Rule_184.png")
    plt.show()

main()