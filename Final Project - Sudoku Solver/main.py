import numpy as np
import matplotlib.pyplot as plt

def validInt(value, minValue):
    try:
        num = int(value)
        if num >= minValue:
            return "ok", num
        else:
            return "too-small", None
    except ValueError:
        return "non-numeric", None

def createMasks(puzzle, n):
    size = n * n
    masks = []

    for value in range(1, size + 1):
        mask = np.ones((size, size), dtype=int)

        positions = np.argwhere(puzzle == value)
        for r, c in positions:
            mask[r, :] = 0
            mask[:, c] = 0

            sr = (r // n) * n
            sc = (c // n) * n
            mask[sr:sr+n, sc:sc+n] = 0

        mask[puzzle != 0] = 0
        masks.append(mask)

    return np.array(masks)

def solveKnown(puzzle, n):
    masks = createMasks(puzzle, n)
    overlap = np.sum(masks, axis=0)

    rows, cols = np.where(overlap == 1)
    for i in range(len(rows)):
        r = rows[i]
        c = cols[i]
        value = np.where(masks[:, r, c] == 1)[0][0] + 1
        puzzle[r, c] = value

    return puzzle

def solveSudoku(puzzle, n):
    while True:
        before = puzzle.copy()
        puzzle = solveKnown(puzzle, n)
        if np.array_equal(before, puzzle):
            break

    if np.all(puzzle != 0):
        return True

    size = n * n
    for r in range(size):
        for c in range(size):
            if puzzle[r, c] == 0:
                for value in range(1, size + 1):
                    test = puzzle.copy()
                    test[r, c] = value
                    if createMasks(test, n)[value - 1, r, c] == 1:
                        puzzle[r, c] = value
                        if solveSudoku(puzzle, n):
                            return True
                        puzzle[r, c] = 0
                return False
    return False

def generateFullGrid(n):
    size = n * n
    puzzle = np.zeros((size, size), dtype=int)
    solveSudoku(puzzle, n)
    return puzzle

def generatePuzzle(n):
    puzzle = generateFullGrid(n)
    size = n * n
    removals = n * n * 3

    while removals > 0:
        r = np.random.randint(0, size)
        c = np.random.randint(0, size)
        if puzzle[r, c] != 0:
            backup = puzzle[r, c]
            puzzle[r, c] = 0
            test = puzzle.copy()
            if not solveSudoku(test, n):
                puzzle[r, c] = backup
            else:
                removals -= 1

    return puzzle

def drawSudoku(puzzle, n, filename):
    size = n * n
    fig, ax = plt.subplots()
    ax.imshow(np.zeros((size, size)), cmap="gray_r")

    for i in range(size + 1):
        lw = 2 if i % n == 0 else 0.5
        ax.axhline(i - 0.5, linewidth=lw, color="black")
        ax.axvline(i - 0.5, linewidth=lw, color="black")

    for r in range(size):
        for c in range(size):
            if puzzle[r, c] != 0:
                ax.text(c, r, str(puzzle[r, c]),
                        ha="center", va="center", fontsize=14)

    ax.set_xticks([])
    ax.set_yticks([])
    plt.savefig(filename)
    plt.close()

def main():
    n_input = input("Enter subgrid size (3 for 9x9): ")
    status, n = validInt(n_input, 2)

    if status == "non-numeric":
        print("Enter a valid integer")
        return
    elif status == "too-small":
        print("Subgrid size must be 2 or greater")
        return

    puzzle = generatePuzzle(n)
    solution = puzzle.copy()
    solveSudoku(solution, n)

    print("Generated Puzzle:")
    print(puzzle)

    print("Solved Puzzle:")
    print(solution)

    drawSudoku(puzzle, n, "sudoku_puzzle.png")
    drawSudoku(solution, n, "sudoku_solution.png")

while True:
    main()
