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

Inp = input('Enter people and time : ').split()
Chashier1 = Queue()
Chashier2 = Queue()
Customers = Queue()

minute = int(Inp[1])

for i in Inp[0]:
        Customers.push(i)

for y in range(1,minute+1,1): 
    if (y % 2) == 0:
        Chashier2.deQueue()       
    temp = Customers.deQueue()
    if Chashier1.size() == 5:
        if temp is not None:
            Chashier2.push(temp)
        print(y,Customers,Chashier1,Chashier2)
    if Chashier1.size() < 5:
        if temp is not None:
            Chashier1.push(temp)
        print(y,Customers,Chashier1,Chashier2)
    if (y % 3) == 0:
        Chashier1.deQueue()

    
