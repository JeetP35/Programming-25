def valid_input(value):
    try:
        number = float(value)
        if number >= 0:
            return "ok", number
        else:
            return "negative", None
    except ValueError:
        return "non-numeric", None

def newton_sqrt(number, tolerance=1e-1000, max_iterations=1000):
    if number == 0:
        return 0.0
    estimate = number / 2
    for _ in range(max_iterations):
        new_estimate = (estimate + number / estimate) / 2
        if abs(new_estimate - estimate) < tolerance * abs(new_estimate):
            return new_estimate
        estimate = new_estimate
    return estimate

def root_type(number, result, tolerance=1e-10):
    nearest = round(result)
    return abs(nearest**2 - number) < tolerance

while True:
    number = input("Enter a number to square root: ")
    status, num_val = valid_input(number)

    if status == "ok":
        result = newton_sqrt(num_val)
        print(f"Square root of {num_val} is {result}")
        if num_val != 0:
            if root_type(num_val, result):
                print(f"{result} is a perfect square root")
            else:
                print(f"{result} is an irrational root")
    elif status == "negative":
        print("Invalid input: number must be non-negative.")
    elif status == "non-numeric":
        print("Invalid input: please enter a numeric value.")
        
"""
=================
Unit Testing
=================

Test 1:
input : 4
expected output : Square root of 4.0 is 2.0
                  2.0 is a perfect square root
output : Square root of 4.0 is 2.0
         2.0 is a perfect square root

Test 2:
input : 2
expected output : Square root of 2.0 is 1.4142135623...
                  1.4142135623... is an irrational root
output : Square root of 2.0 is 1.4142135623...
         1.4142135623... is an irrational root

Test 3:
input : 0
expected output : Square root of 0.0 is 0.0
output : Square root of 0.0 is 0.0

Test 4:
input : -9
expected output : Invalid input: number must be non-negative.
output : Invalid input: number must be non-negative.

Test 5:
input : abc
expected output : Invalid input: please enter a numeric value.
output : Invalid input: please enter a numeric value.
"""