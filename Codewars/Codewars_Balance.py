Inp = map(int, input('Enter list of number : ').split())

def CheckingBalance():
    numList = []
    sumleft = 0
    sumright = 0

    for i in Inp:
        numList.append(i)

    if len(numList) < 2:
        print('there must have more than 2 integers in list!')
    else:
        for i in numList:
            if i >= 1:
                for i in range(i,0,-1):
                    sumleft = sumleft + i
                for i in range(i,-1,1):
                    sumright = sumright + i
            if sumleft == sumright:
                print(str(i))
                break
            else:print('This list has no balance')

CheckingBalance()
            
