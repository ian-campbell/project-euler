def findmysum():
    mysum = 0
    for i in range(0, 1000):
        if i % 3 and i % 5 == 0:
            mysum += i
            pass
        elif i % 3 == 0:
            mysum += i
            pass
        elif i % 5 == 0:
            mysum += i
            pass
    return mysum
