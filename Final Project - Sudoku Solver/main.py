import numpy as np
import matplotlib.pyplot as plt


def validInt(value):
    try:
        num = int(value)
        if num >= 2:
            return "ok", num
        else:
            return "too-small", None
    except ValueError:
        return "non-numeric", None
    

def validStr(value):
    valid_difficulties = ["easy", "medium", "hard", "extreme"]
    if value in valid_difficulties:
        return value
    else:
        return "medium"  # default difficulty


def isValid(puzzle, n, row, col, value):
    # check row
    if value in puzzle[row]:
        return False

    # check column
    if value in puzzle[:, col]:
        return False
    # check subgrid
    startRow = (row // n) * n
    startCol = (col // n) * n

    # check if the value already exists in the subgrid
    # subgrid starts at (startRow, startCol) and is n x n in size
    if value in puzzle[startRow:startRow+n, startCol:startCol+n]:
        return False  # value cannot be placed here
    # value is valid in row, column, and subgrid
    return True


def solveSudoku(puzzle, n):
    size = n * n

    # loop through the grid to find an empty cell
    for row in range(size):
        for col in range(size):
            if puzzle[row, col] == 0:

                # try numbers in random order so puzzles differ
                numbers = np.arange(1, size + 1)
                np.random.shuffle(numbers)

                for value in numbers:
                    # check if the value is valid in this position
                    if isValid(puzzle, n, row, col, value):
                        puzzle[row, col] = value

                        # recursively attempt to solve the rest of the grid
                        if solveSudoku(puzzle, n):
                            return True
                        # undo placement if it leads to a dead end
                        puzzle[row, col] = 0

                # no valid number fits here, trigger backtracking
                return False
    # no empty cells left, puzzle is solved
    return True


def generateFullGrid(n):
    size = n * n  # total grid size
    puzzle = np.zeros((size, size), dtype=int)  # start with an empty grid
    # fill the grid using the Sudoku solver
    solveSudoku(puzzle, n)
    return puzzle  # return a complete valid Sudoku grid


def generatePuzzle(n, difficulty):
    puzzle = generateFullGrid(n)
    size = n * n

    # remove about half of the values to create a puzzle
    if difficulty == "easy":
        removals = (size * size) // 3
    elif difficulty == "medium":
        removals = (size * size) // 2
    elif difficulty == "hard":
        removals = (size * size) * 2 // 3
    elif difficulty == "extreme":
        removals = (size * size) * 3 // 4

    attempts = removals * 5

    # randomly remove values while keeping the puzzle solvable
    while removals > 0 and attempts > 0:
        # pick a random cell in the grid
        row = np.random.randint(0, size)
        col = np.random.randint(0, size)

        # only remove a number if the cell is not already empty
        if puzzle[row, col] != 0:
            backup = puzzle[row, col]
            puzzle[row, col] = 0

            # make a copy and try solving it
            # this checks whether the puzzle is still solvable after removal
            test = puzzle.copy()
            if solveSudoku(test, n):
                removals -= 1
            else:
                # restore the value if removal makes the puzzle unsolvable
                puzzle[row, col] = backup
        attempts -= 1
    return puzzle


def drawSudoku(puzzle, n, filename):
    size = n * n

    # create a blank background for the grid
    plt.imshow(np.zeros((size, size)), cmap="gray_r")

    # every n lines, we reach the edge of a subgrid
    # for example, in a 9x9 board (n = 3), lines at 0, 3, 6, 9 separate the 3x3 boxes
    for i in range(size + 1):
        if i % n == 0:
            lineWidth = 2      # thicker line for subgrid boundary
        else:
            lineWidth = 0.5    # regular cell line

        # offset by 0.5 so lines appear between cells
        plt.axhline(i - 0.5, linewidth=lineWidth, color="black")
        plt.axvline(i - 0.5, linewidth=lineWidth, color="black")

    # draw the numbers in each non-empty cell
    for row in range(size):
        for col in range(size):
            if puzzle[row, col] != 0:
                # place number in the center of the cell
                plt.text(col, row, str(puzzle[row, col]),
                         ha="center", va="center", fontsize=14)

    # remove axis labels for a clean Sudoku look
    plt.xticks([])
    plt.yticks([])

    # save the image and close the figure
    plt.savefig(filename)
    plt.close()


def main():
    # get subgrid size from user (3 → 9x9, 2 → 4x4)
    num_input = input("Enter subgrid size (3 for 9x9): ")
    status, n = validInt(num_input)
    diff_input = input("Enter difficulty (easy, medium, hard, extreme): ").lower()
    difficulty = validStr(diff_input)


    # handle invalid input
    if status == "non-numeric":
        print("Enter a valid integer")
        return
    elif status == "too-small":
        print("Subgrid size must be 2 or greater")
        return

    # generate a Sudoku puzzle
    puzzle = generatePuzzle(n, difficulty)

    # create a copy and solve it
    solution = puzzle.copy()
    solveSudoku(solution, n)

    # display results in the console
    print("Generated Puzzle:")
    print(puzzle)
    print('-----------------------------------------')
    print("Solved Puzzle:")
    print(solution)

    # save images of the puzzle and solution
    drawSudoku(puzzle, n, "sudoku_puzzle.png")
    drawSudoku(solution, n, "sudoku_solution.png")


main()
