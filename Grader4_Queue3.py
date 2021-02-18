class Queue:
    def __init__(self):
        self.item = []

    def push(self,item):
        self.item.append(item)

    def deQueue(self):
        if self.size() > 0:
            return self.item.pop(0)

    def size(self):
        return len(self.item)

    def __str__(self):
        return str(self.item)

    def isEmpty(self):
        return len(self.item) == 0

Inp = input('Enter code,hint : ').split(',')
Asc = Queue()

if Inp[1] == 'f':
    for i in Inp[0]:
        i = chr(ord(i)-1)
        Asc.push(i)
        print(Asc)
elif Inp[1] == 'n':
    for y in Inp[0]:
        y = chr(ord(y)+6)
        Asc.push(y)
        print(Asc)
elif Inp[1] == 'I':
    for z in Inp[0]:
        z = chr(ord(z)+8)
        Asc.push(z)
        print(Asc)

