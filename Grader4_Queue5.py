class Queue:
    def __init__(self,item = None):
        self.item = []
        if item != None:
            for i in item:
                if i == ' ':
                    continue
                self.item.append(i)

    def enqueue(self,item):
        self.item.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.item.pop(0)

    def size(self):
        return len(self.item)

    def __str__(self):
        res = ''
        for i in self.item:
            res = i+res
        return res
    
    def stri(self):
        res = ''
        for i in self.item:
            res += i
        return res

a_bomb, b_bomb = input('Enter Input (Normal, Mirror) : ').split(' ')
a_bomb = list(a_bomb)
b_bomb = list(b_bomb)

aItem = Queue()
bItem = Queue()

sizeA = len(a_bomb)
sizeB = len(b_bomb)
aflag = 0
bflag = 0
fflag = 0
aCount = 0
bCount = 0
fCount = 0
while sizeB > 2 and bflag == 0:
    for i in range(sizeB - 1 , -1, -1): # 0 1 2
        if b_bomb[i] == b_bomb[i-1] == b_bomb[i-2]:
            bItem.enqueue(b_bomb[i])
            b_bomb.pop(i-2)
            b_bomb.pop(i-2)
            b_bomb.pop(i-2)
            sizeB -= 3
            bCount += 1
            #print('Boom!')
            break
        if i == 0: # 0 == 0
            bflag = 1

while sizeA > 2 and aflag == 0:
    for i in range(sizeA - 2):
        if a_bomb[i] == a_bomb[i+1] == a_bomb[i+2]:
            if bItem.size() > 0:
                a_bomb.insert(i+2,bItem.dequeue())
                sizeA += 1
                fflag = 1
            if a_bomb[i] == a_bomb[i+1] == a_bomb[i+2]:
                a_bomb.pop(i)
                a_bomb.pop(i)
                a_bomb.pop(i)
                sizeA -= 3
                if fflag == 0:
                    aCount += 1
                else:
                    fCount += 1
            fflag = 0
            break
            
        if i == sizeA - 3:
            aflag = 1
while bItem.size() > 0:
    bItem.dequeue()
if sizeA > 0:
    for i in a_bomb:
        aItem.enqueue(i)
if sizeB > 0:
    for i in b_bomb:
        bItem.enqueue(i)

print('NORMAL :')
print(sizeA)
print(aItem if sizeA > 0 else 'Empty')
print(aCount,'Explosive(s) ! ! ! (NORMAL)')
if fCount>0 :
    print('Failed Interrupted',fCount,'Bomb(s)')
print('------------MIRROR------------')
print(': RORRIM')
print(sizeB)
print(bItem.stri() if sizeB > 0 else 'ytpmE')
print('(RORRIM) ! ! ! (s)evisolpxE',bCount)