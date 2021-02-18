class Queue:
    def __init__(self):
        self.item = []

    def push(self,item):
        self.item.append(item)

    def deQueue(self):
        if self.size() > 0:
            return self.item.pop(0)
        else:
            print('Empty')

    def size(self):
        return len(self.item)

    def __str__(self):
        if self.size() > 0:
            return ', '.join(str(item) for item in self.item)
        else:
            return 'Empty'

    def isEmpty(self):
        return len(self.item) == 0
    

Inp = input('Enter Input : ').split(',')
Q = Queue()
DQ = Queue()

for i in Inp:
    i = i.split()
    if i[0] == 'E':
        Q.push(int(i[1]))
        print(Q)    
    elif i[0] == 'D':
        if Q.isEmpty():
            print('Empty')
        else:
            temp = Q.deQueue()
            print(temp,'<-',Q)
            DQ.push(temp)

print(DQ,':',Q)