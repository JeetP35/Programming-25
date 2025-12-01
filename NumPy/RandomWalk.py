import numpy as np
import matplotlib.pyplot as plt

def randomWalk(n, maxSteps):
    position = n // 2
    positions = [position]
    for step in range(maxSteps):
        move = np.random.choice([-1, 1])
        newPosition = position + move
        if newPosition < 0:
            newPosition = 0
        if newPosition > n - 1:
            newPosition = n - 1
        positions.append(newPosition)
        position = newPosition
        if newPosition == 0 or newPosition == n - 1:
            break
    rows = len(positions)
    walkArray = np.zeros((rows, n), dtype=int)
    walkArray[np.arange(rows), positions] = 1
    return walkArray

m = 200
n = 101
walk = randomWalk(n, m)
plt.imshow(walk, cmap='gray_r', interpolation='nearest')
plt.title('Random Walk')
plt.savefig("RandomWalk1D.png")
plt.show()

def randomTrials(n, trials, maxSteps):
    start = n // 2
    moves = np.random.choice([-1, 1], size=(trials, maxSteps))
    positions = start + np.cumsum(moves, axis=1)
    hit = (positions <= 0) | (positions >= n - 1)
    hitFound = hit.any(axis=1)
    firstHit = np.argmax(hit, axis=1)
    steps = np.where(hitFound, firstHit + 1, maxSteps)
    return steps

nValues = np.arange(1, 51)
trials = 200
maxSteps = 600
averages = []

for v in nValues:
    result = randomTrials(v, trials, maxSteps)
    averages.append(np.mean(result))

plt.scatter(nValues, averages)
plt.title("Random Walk Simulation: Average Number of Steps vs. Displacement")
plt.xlabel("Displacement (n value)")
plt.ylabel("Average Number of Steps")
plt.savefig("RandomWalkCurve.png")
plt.show()
