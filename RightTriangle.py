def TriangleInput():
    num1 = float(input("Enter the length of one arm side: "))
    num2 = float(input("Enter the length of the other side: "))
    boolHypo = input("Is this second side the hypotenuse? (1 for Yes, 0 for No): ")
    return num1, num2, True if boolHypo == '1' else False


def InputValid(num1, num2):
    try:
        if num1 > 0 and num2 > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def HypoSideSolver(num1, num2):
    return (num1**2 + num2**2)


def ArmSideSolver(hypo, arm):
    return (hypo**2 - arm**2)


def NewtonSqrt(number, max_iterations=1000, tolerance=1e-10):
    estimate = number / 2
    for i in range(max_iterations):
        new_estimate = (estimate + number / estimate) / 2
        if abs(new_estimate - estimate) < tolerance:
            return new_estimate
        estimate = new_estimate
    return estimate


def SolveTriangle(num1, num2, boolHypo):
    if InputValid(num1, num2):
        if boolHypo == True:
            result = HypoSideSolver(num1, num2)
            finalResult = NewtonSqrt(result)
            print(f"\nGiven sides: {num1}, {num2}")
            print(f"The length of the hypotenuse side is approximately {finalResult}\n")
        elif boolHypo == False:
            if num2 > num1:
                result = ArmSideSolver(num2, num1)
                finalResult = NewtonSqrt(result)
                print(f"\nGiven hypotenuse {num2} and arm {num1}")
                print(f"The length of the missing arm side is approximately {finalResult}\n")
            else:
                print("Error: Hypotenuse must be the longest side. Please try again.\n")
        else:
            print("Invalid input for hypotenuse flag. Enter 1 for Yes or 0 for No.\n")
    else:
        print("Invalid side lengths. Please enter positive numbers.\n")


while True:
    num1, num2, boolHypo = TriangleInput()
    SolveTriangle(num1, num2, boolHypo)

"""
=============================
Unit Testing for Triangle Solver
=============================

1. Input: num1=3, num2=4, boolHypo=1
Expected: Hypotenuse = 5

2. Input: num1=5, num2=12, boolHypo=1
Expected: Hypotenuse = 13

3. Input: num1=3, num2=5, boolHypo=0
Expected: Other arm = 4

4. Input: num1=8, num2=10, boolHypo=0
Expected: Other arm = 6

5. Input: num1=-3, num2=4
Expected: Invalid input message

6. Input: num1=3, num2=2, boolHypo=0
Expected: Error message (hypotenuse must be longest side)

7. Input: non-numeric (e.g. "abc")
Expected: Invalid input message
"""