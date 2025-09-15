def TriangleInput():
    num1 = float(input("Enter the length of a arm side: "))
    num2 = float(input("Enter the length of the other arm side: "))
    boolHypo = input("Is the hypotenuse side given? (1 for Yes, 0 for No): ")
    return num1, num2

def InputValid():
    if (num1 >= 0) and (num2 >= 0):
        boolValue = True
    else:
        boolValue = False
    return boolValue

def HypoSideSolver():
    number = ((num1**2) + (num2**2))
    return number

def ArmSideSolver():
    number = ((num2 ** 2) - (num1 ** 2))
    return number

def NewtonSqrt(number, max_iterations=1000, tolerance=1e-100):
    estimate = (number/2)
    for i in range(max_iterations):
        new_estimate = (estimate + (number/estimate))/2
        if ((abs(new_estimate-estimate))<tolerance):
            return new_estimate
        estimate=new_estimate

while True:
    num1, num2 = TriangleInput()
    InputValid()
    if (boolValue==True):
        if (boolHypo == '1'):
            result = HypoSideSolver()
            finalResult = NewtonSqrt(result)
            print(f"The length of the hypotenuse side is approximately {finalResult}")
        elif (boolHypo == '0'):
            if (num2 > num1):
                result = ArmSideSolver()
                finalResult = NewtonSqrt(result)
                print(f"The length of the arm side is approximately {finalResult}")
            else:
                print("The hypotenuse side must be the longest side. Please try again.")
        else:
            print("Invalid Input for hypotenuse side. Please enter 1 for Yes or 0 for No.")
    else:
        print("Invalid Input for side lengths, Please try again")