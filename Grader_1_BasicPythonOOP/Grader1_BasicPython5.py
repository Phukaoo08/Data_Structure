print('*** Fun with countdown ***')
a = map(int,input('Enter List : ').split())
lists = []
Preanswer = []
Answer = []
Count = 0
current = 0
CountDown = False

for i in a:
    lists.append(i)

for x in range(len(lists)):
    if(lists[x] == 1):
        Preanswer.append(lists[x])
        Answer.append(Preanswer.copy())
        Preanswer.clear()
        Count = Count + 1
    elif(x != len(lists)-1):    
        if(lists[x] - lists[x+1] == 1):
            if(lists[x] != 1):
                Preanswer.append(lists[x])
            else:
                Preanswer.append(lists[x])
                Count = Count + 1


print([Count,Answer])

# for x in lists:
#     CountDown = True
#     if(x == 1):
#         CountDown = True
#         Count = Count + 1
#     elif(lists[current] == lists[0]): # first index case
#         CountDown = False
#         current += 1
#     elif(lists[current] == lists[current-1]):
#         CountDown = False
#         current += 1
#     elif(lists[current] - lists[current] == 1):
#         CountDown = True
#         current += 1
#     elif(lists[current] - lists[current] != 1):
#         CountDown = False
#         current += 1
#     if(CountDown is True):
#         Preanswer.append(lists[current])

