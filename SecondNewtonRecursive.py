def valid_input(number):
    try:
        if number >= 0:
            return True
        else:
            print("Input must be a non-negative number.")
            return False
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return False


def newton_recursive(number, estimate=None, tolerance=1e-10, iteration=1, max_iterations=1000):
    if number == 0:
        return 0
    if estimate is None:
        estimate = number / 2

    new_estimate = (estimate + number / estimate) / 2

    if abs(new_estimate - estimate) < tolerance:
        return new_estimate

    return newton_recursive(number, new_estimate)

while True:
    number = float(input("Enter a non-negative number to square root: "))
    valid_input(number):
    result = newton_recursive(number)
    print(f"Square root of {number} is approximately {result}")
"""
=============================
Unit Testing for newton_recursive()
=============================

1. Input: 0
Expected: 0

2. Input: 1
Expected: 1

3. Input: 4
Expected: 2 (perfect square)

4. Input: 9
Expected: 3 (perfect square)

5. Input: 2
Expected: ~1.414213562 (irrational)

6. Input: 10
Expected: ~3.162277660 (irrational)

7. Input: -5
Expected: Invalid input message

8. Input: "abc"
Expected: Invalid input message
"""