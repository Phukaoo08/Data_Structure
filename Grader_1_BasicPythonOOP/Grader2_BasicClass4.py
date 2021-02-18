Inp = list(map(int,input('Enter Your List : ').split()))
preAnswer = []
finalAnswer = []

if len(Inp) <= 2:
    print('Array Input Length Must More Than 2')
else:
    for i in range(len(Inp)):
        for a in range(len(Inp)):
            for b in range(len(Inp)):
                if i < a < b:
                    if Inp[i] + Inp[a] + Inp[b] == 5:
                        preAnswer.append(Inp[i])
                        preAnswer.append(Inp[a])
                        preAnswer.append(Inp[b])
                        preAnswer.sort()
                        if preAnswer not in finalAnswer:
                            finalAnswer.append(preAnswer)
                            preAnswer = []
                            continue
                        preAnswer = []
    print(finalAnswer)
