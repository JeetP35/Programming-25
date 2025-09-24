def fib1(termCount):
    seq = [0, 1]
    while len(seq) < termCount:
        seq.append(seq[-1] + seq[-2])
    return seq[:termCount]

def fib2(startIndex, termCount):
    seq = [0, 1]
    while len(seq) < startIndex + termCount:
        seq.append(seq[-1] + seq[-2])
    return seq[startIndex:startIndex + termCount]

def validInput(value, minValue):
    try:
        num = int(value)
        if num >= minValue:
            return "ok", num
        else:
            return "too-small", None
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

def assignment():
    termCount = input("Enter how many Fibonacci terms: ")
    status, termCount = validInput(termCount, 2)
    if status == "ok":
        print(fib1(termCount))
    elif status == "too-small":
        print("Enter a number ≥ 2")
    else:
        print("Enter a valid integer")

    start = input("Enter Fibonacci start index: ")
    status, start = validInput(start, 0)
    if status == "ok":
        count = input("Enter how many terms: ")
        status, count = validInput(count, 2)
        if status == "ok":
            print(fib2(start, count))
        elif status == "too-small":
            print("Enter a number ≥ 2")
        else:
            print("Enter a valid integer")
    elif status == "too-small":
        print("Start index must be ≥ 0")
    else:
        print("Enter a valid integer")

    number = input("Enter a number to factorize: ")
    status, number = validInput(number, 2)
    if status == "ok":
        print(primeFactors(number))
    elif status == "too-small":
        print("Enter a number ≥ 2")
    else:
        print("Enter a valid integer")

assignment()