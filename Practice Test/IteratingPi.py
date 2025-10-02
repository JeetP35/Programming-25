#Calculating pi using Gregory-Leibniz series

def pi():
    n = 0
    piList = []
    tolerance = 1e-10
    while True:
        pi = ((-1)**n) / ((2*n) + 1)
        piList.append(pi)
        n += 1
        piSum = 4 * sum(piList)
        if abs(piSum - 3.141592653589793) < tolerance:
            print(f"Calculated value of pi: {piSum}")
pi()