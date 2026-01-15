import numpy as np
import matplotlib.pyplot as plt

def randomWalk(n, maxSteps):
    position = n // 2       # start in the middle
    positions = [position]  # store path

    for step in range(maxSteps):
        move = np.random.choice([-1, 1])
        newPosition = position + move

        # absorbing boundaries
        if newPosition < 0:
            newPosition = 0
        if newPosition > n - 1:
            newPosition = n - 1
        positions.append(newPosition)
        position = newPosition

        # stop when boundary is reached
        if newPosition == 0 or newPosition == n - 1:
            break


    rows = len(positions)

    # time x space grid, 1 marks walker position
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

    # generate all walks at once
    moves = np.random.choice([-1, 1], size=(trials, maxSteps))
    positions = start + np.cumsum(moves, axis=1)

    # detect boundary hits
    hit = (positions <= 0) | (positions >= n - 1)
    hitFound = hit.any(axis=1)

    # first time each walk hits a boundary
    firstHit = np.argmax(hit, axis=1)

    # steps until hit (or maxSteps if no hit)
    steps = np.where(hitFound, firstHit + 1, maxSteps)
    return steps

nValues = np.arange(1, 51) #domain sizes
trials = 200 #walks per domain size
maxSteps = 600 #step limit
averages = [] #store avg steps

for v in nValues:
    # run many random walks for this domain size
    result = randomTrials(v, trials, maxSteps)

    # average number of steps before hitting a boundary
    averages.append(np.mean(result))

# plot results
plt.scatter(nValues, averages)
plt.title("Random Walk Simulation: Average Number of Steps vs. Displacement")
plt.xlabel("Displacement (n value)")
plt.ylabel("Average Number of Steps")
plt.savefig("RandomWalkCurve.png")
plt.show()
