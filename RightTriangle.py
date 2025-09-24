def TriangleInput():
    num1 = input("Enter the length: ")
    num2 = input("Enter the another length: ")
    return num1, num2

def valid_input(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        if num1 > 0 and num2 > 0:
            return "ok", num1, num2
        else:
            return "zero-or-negative", None, None
    except ValueError:
        return "non-numeric", None, None

def ValidTriangle(num1, num2):
    boolHypo = int(input("Is the one of the lengths the hypotenuse? 1 for yes, 0 for no: "))
    if boolHypo == 1:
        if num1 > num2:
            return "num1", num1, num2
        elif num2 > num1:
            return "num2", num2, num1
        else:
            print(f"Both {num1} and {num2} are equal, and aren't valid hypotenuses")
            return "equal", None, None
    elif boolHypo == 0:
        return "ok", num1, num2
    else:
        return "invalid", None, None

def HypoSideSolver(num1, num2):
    return ((num1**2) + (num2**2))

def ArmSideSolver(hypo, arm):
    return ((hypo**2) - (arm**2))

def NewtonSqrt(number, max_iterations=1000, tolerance=1e-1000):
    if number == 0:
        return 0
    estimate = number / 2
    for i in range(max_iterations):
        new_estimate = (estimate + number / estimate) / 2
        if abs(new_estimate - estimate) < tolerance:
            return new_estimate
        estimate = new_estimate
    return estimate

def triangleSolver():
    num1, num2 = TriangleInput()
    status, num1, num2 = valid_input(num1, num2)
    if status == "ok":
        triangleStatus, hypo, arm = ValidTriangle(num1, num2)
        if triangleStatus == "num1":
            missingSide = ArmSideSolver(hypo, arm)
            missingSideSqrt = NewtonSqrt(missingSide)
            print(f"Hypotenuse is {hypo}")
            print(f"Missing Length is {missingSideSqrt}")
        elif triangleStatus == "num2":
            missingSide = ArmSideSolver(hypo, arm)
            print(f"Hypotenuse is {hypo}")
            missingSideSqrt = NewtonSqrt(missingSide)
            print(f"Missing Length is {missingSideSqrt}")
        elif triangleStatus == "ok":
            missingSide = HypoSideSolver(num1, num2)
            missingSideSqrt = NewtonSqrt(missingSide)
            print(f"Hypotenuse is {missingSideSqrt}")
        elif triangleStatus == "equal":
            pass
        elif triangleStatus == "invalid":
            print("Invalid triangle")
    elif status == "zero-or-negative":
        print("Side lengths must be greater than zero")
    elif status == "non-numeric":
        print("Please enter numeric values")

while True:
    triangleSolver()
    
'''
Input 1 (Arm Length) : 3
Input 2 (Another Length) : 4
Input 3 (Confirmation) : 0 ("No, one of the input isn't hypotenuse")

Expected Output : Hypotenuse is 5
Output : Hypotenuse is 5


Input 1 (Arm Length) : 3
Input 2 (Another Length) : 5
Input 3 (Confirmation) : 1 ("Yes, one of the input is hypotenuse")

Expected Output : 
    Hypotenuse is 5
    Missing Length is 4
Output : 
    Hypotenuse is 5
    Missing Length is 4



Input 1 (Arm Length) : 5
Input 2 (Another Length) : 10
Input 3 (Confirmation) : 1 ("Yes, one of the input is hypotenuse")

Expected Output : 
    Hypotenuse is 10.0
    Missing Length is 8.660254037844386
Output : 
    Hypotenuse is 10.0
    Missing Length is 8.660254037844386



Input 1 (Arm Length) : -3
Input 2 (Another Length) : 4

Expected Output : Please enter non-negative numbers
Output : Please enter non-negative numbers



Input 1 (Arm Length) : 0
Input 2 (Another Length) : 7

Expected Output : Side lengths must be greater than zero
Output : Side lengths must be greater than zero



Input 1 (Arm Length) : abc
Input 2 (Another Length) : 5

Expected Output : Please enter numeric values
Output : Please enter numeric values
'''