#Calculating pi using Gregory-Leibniz series

def pi():
    n = 0
    piList = []
    piSum = 0
    while piSum != 3.141592653:
        pi = ((-1)**n) / ((2*n) + 1)
        piList.append(pi)
        n += 1
        piSum = 4 * sum(piList)
    print(piSum)

pi()