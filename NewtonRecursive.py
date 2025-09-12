def newton_sqrt(number, iterations=12):
    estimate = number / 2
    for i in range(iterations):
        estimate = (estimate + number / estimate) / 2
    return estimate

while True:
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Please enter a non-negative number.")
            continue
        elif number == 0:
            print("Square root of 0 is 0")
            continue
        result = newton_sqrt(number)
        print(f"Square root of {number} is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")