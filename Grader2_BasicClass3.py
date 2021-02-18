print('*** New Range ***')
Inp = list(map(float,input('Enter Input : ').split()))
answer = []

def newRange():
    if len(Inp) == 1:
        start = 0
        for i in range(start,int(Inp[0]),1):
            answer.append(float(i))
        print(tuple(answer))
    if len(Inp) == 2:
        i = Inp[0]
        while i < Inp[1]:
            answer.append(i)
            i = i + 1
        else:
            print(tuple(answer))
    if len(Inp) == 3:
        i = Inp[0]
        while i < Inp[1]:
            answer.append(round(i,3))
            i = i + Inp[2]
        else:
            print(tuple(answer))

newRange()