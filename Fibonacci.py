def Fib1(termCount):
    FibSeq1 = [0, 1]
    while (len(FibSeq1) < termCount):
        FibSeq1.append(FibSeq1[-1] + FibSeq1[-2])
    return FibSeq1[:termCount]

def Fib2(startIndex, termCount):
    FibSeq2 = [0, 1]
    while ((len(FibSeq2)) < (startIndex + termCount)):
        FibSeq2.append(FibSeq2[-1] + FibSeq2[-2])
    return FibSeq2[startIndex:startIndex + termCount]

def validInput(value):
    try:
        number = float(value)
        if number > 0:
            return "ok", number
        else:
            return "zero-or-negative", None
    except ValueError:
        return "non-numeric", None

def primeFactors(number):
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    return factors

def Assignment():
    termCount = input("Enter the number of terms you want in the Fibonacci sequence: ")
    status, termCount = validInput(termCount)
    if status == "ok":
        termCount = int(termCount)
        if termCount >= 2:
            print(Fib1(termCount))
            break
        else:
            print("Please enter a number greater than or equal to 2")
    elif status == "zero-or-negative":
        print("Please enter a number greater than 0")
    elif status == "non-numeric":
        print("Please enter a valid number")


    fibStart = input("Enter the starting index of the Fibonacci sequence: ")
    status, fibStart = validInput(fibStart)
    if status == "ok":
        fibStart = int(fibStart)
        if fibStart >= 0:
            print(Fib2(fibStart, termCount))
            break
        else:
            print("Please enter a number greater than or equal to 0")
    elif status == "zero-or-negative":
        print("Please enter a number greater than or equal to 0")
    elif status == "non-numeric":
        print("Please enter a valid number")
    fib2TermCount = input("Enter the number of terms you want in the Fibonacci sequence: ")
    status, fib2TermCount = validInput(fib2TermCount)
    if status == "ok":
        fib2TermCount = int(fib2TermCount)
        if fib2TermCount >= 2:
            print(Fib2(fibStart, fib2TermCount))
            break
        else:
            print("Please enter a number greater than or equal to 2")
    elif status == "zero-or-negative":
        print("Please enter a number greater than or equal to 2")
    elif status == "non-numeric":
        print("Please enter a valid number")


    primeInput = input("Enter a number to find its prime factors: ")
    status, primeInput = validInput(primeInput)
    if status == "ok":
        primeInput = int(primeInput)
        if primeInput >= 2:
            print(primeFactors(primeInput))
            break
        else:
            print("Please enter a number greater than or equal to 2")
    elif status == "zero-or-negative":
        print("Please enter a number greater than or equal to 2")
    elif status == "non-numeric":
        print("Please enter a valid number")

while True:
    Assignment()