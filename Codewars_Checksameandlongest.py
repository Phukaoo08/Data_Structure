Inp1,Inp2 = input("Enter input : ").split()
answer = []
sameCharlist = []
sameCharListJoin = []

def deleteSaMe():
    checkSame = ''
    for i in Inp1:
        if i not in sameCharlist:
            checkSame = checkSame + i
            sameCharlist.append(i)

    for y in Inp2:
        if y not in sameCharlist:
            checkSame = checkSame + y
            sameCharlist.append(y)
    print(checkSame)

def longestWithnoJoin():
    countfirstStr = 0
    countsecondStr = 0
    for i in Inp1:
        countfirstStr += 1

    for y in Inp2:
        countsecondStr += 2
    
    if countfirstStr > countsecondStr:
        print(Inp1)
    else:
        print(Inp2)  

def longestWithJoin():
    checkSameChar = ''
    finalAnswer = []
    lastAnswer = ''
    for i in Inp1:
        if i not in sameCharListJoin:
            checkSameChar = checkSameChar + i
            sameCharListJoin.append(i)

    for y in Inp2:
        if y not in sameCharListJoin and y not in Inp1:
            checkSameChar = checkSameChar + y
            sameCharListJoin.append(y)
    
    for x in checkSameChar:
        finalAnswer.append(x)
    
    finalAnswer.sort()
    
    for z in finalAnswer:
        lastAnswer = lastAnswer + z
    
    print(lastAnswer)
        
deleteSaMe()
longestWithnoJoin()
longestWithJoin()



