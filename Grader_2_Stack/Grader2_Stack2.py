class Stack:
    def __init__(self):
        self.item = []

    def add(self,item):
        self.item.append(item)

    def size(self):
        return len(self.item)

    def pop(self):
        if len(self.item) == 0:
            return -1
        else:
            return self.item.pop()
        
    def delete(self,item):
        if len(self.item) == 0:
            print('-1')
            return -1
        print('Delete =',item)
        self.item.remove(item)

    def LD(self,item):
        if len(self.item) == 0:
            print('-1')
            return -1
        self.item.remove(item)

    def MD(self,item):
        if len(self.item) == 0:
            print('-1')
            return -1
        self.item.remove(item)    

    def isEmpty(self):
        return len(self.item) == 0

Inp = input('Enter Input : ').split(',')
s = Stack()
temp = Stack()

for i in Inp:
    i = i.split()
    if i[0] == 'P':
        b = s.pop()
        if b == -1:
            print('-1')
        else:
            print('Pop =',b)
    elif i[0] == 'A':
        s.add(int(i[1]))
        print('Add =',int(i[1]))
    elif i[0] == 'D':
        if not s.isEmpty():
            while int(i[1]) in s.item:
                s.delete(int(i[1]))
        else:
            print('-1')
    elif i[0] == 'LD':
        if not s.isEmpty():
            for y in s.item:
                if int(y) < int(i[1]):
                    temp.add(int(y))
            while not temp.isEmpty():
                a = temp.pop()
                print('Delete =',a,'Because',a,'is less than',i[1])
                s.LD(a)
        else:
            print('-1')
    elif i[0] == 'MD':
        if not s.isEmpty():
            for y in s.item:
                if int(y) > int(i[1]):
                    temp.add(int(y))
            while not temp.isEmpty():
                a = temp.pop()
                print('Delete =',a,'Because',a,'is more than',i[1])
                s.MD(a)
        else:
            print('-1')

print('Value in Stack =',s.item)
