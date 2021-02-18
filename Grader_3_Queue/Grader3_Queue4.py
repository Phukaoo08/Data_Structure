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

Inp = input('Enter Input : ').split(',')
In = Queue()
Activity = Queue()
Location = Queue()
MyQueueInt = Queue()
YrQueueInt = Queue()
MyQueue = Queue()
YrQueue = Queue()
Scores = 0

for i in Inp:
    i = i.split()
    MyQueueInt.push(i[0])
    YrQueueInt.push(i[1])
    for y in i:
        y = y.split(':')
        if y[0] == '0':
            Activity.push('Eat')
        elif y[0] == '1':
            Activity.push('Game')
        elif y[0] == '2':
            Activity.push('Learn')
        elif y[0] == '3':
            Activity.push('Movie')
        if y[1] == '0':
            Location.push('Res.')
        elif y[1] == '1':
            Location.push('ClassR.')
        elif y[1] == '2':
            Location.push('SuperM.')
        elif y[1] == '3':
            Location.push('Home')

z = 0

while z < Activity.size():
    if Activity.item[z] == Activity.item[z+1] and Location.item[z] != Location.item[z+1]:
        Scores = Scores + 1
    elif Activity.item[z] != Activity.item[z+1] and Location.item[z] == Location.item[z+1]:
        Scores = Scores + 2
    elif Activity.item[z] == Activity.item[z+1] and Location.item[z] == Location.item[z+1]:
        Scores = Scores + 4
    elif Activity.item[z] != Activity.item[z+1] and Location.item[z] != Location.item[z+1]:
        Scores = Scores - 5
    z = z + 2

for i in range(Activity.size()):
    if (i % 2) == 0:
        MyString = Activity.deQueue() + ':' + Location.deQueue()
        MyQueue.push(MyString)
    else:
        YrString = Activity.deQueue() + ':' + Location.deQueue()
        YrQueue.push(YrString)

Statement = ''

if Scores >= 7:
    Statement = Statement + 'Yes! You\'re my love! : Score is '
elif Scores < 7 and Scores > 0:
    Statement = Statement + 'Umm.. It\'s complicated relationship! : Score is '
else:
    Statement = Statement + 'No! We\'re just friends. : Score is '
    
print('My   Queue =',', '.join(MyQueueInt.item))
print('Your Queue =',', '.join(YrQueueInt.item))
print('My   Activity:Location =',', '.join(MyQueue.item))
print('Your Activity:Location =',', '.join(YrQueue.item))
print(Statement + str(Scores) + '.')
