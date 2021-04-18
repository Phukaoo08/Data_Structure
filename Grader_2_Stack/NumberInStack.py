class Stack:
    def __init__(self):
        self.item = []

    def add(self,item):
        self.item.append(item)

    def pop(self):
        if len(self.item) ==0:
            return -1
        else:
            return self.item.pop()

    def size(self):
        return len(self.item)

    def delete(self,item):
        if len(self.item) == 0:
            print('-1')
            return -1
        else:
            print('Delete =',item)
            self.item.remove(item)

    def lessthanDelete(self,item):
        if len(self.item) == 0:
            print('-1')
            return -1
        else:
            self.item.remove(item)

    def morethanDelete(self,item):
        if len(self.item) == 0:
            print('-1')
            return -1
        else:
            self.item.remove(item)

    def isEmpty(self):
        return len(self.item) == 0

Inp = input('Enter input : ').split(',')
S = Stack()
temp = Stack()

for i in Inp:
    i = i.split()
    if i[0] == 'P':
        Popele = S.pop()
        if Popele == -1:
            print('-1')
        else:
            print('Pop =',Popele)
    elif i[0] == 'A':
        S.add(int(i[1]))
        print('Add =', int(i[1]))
    elif i[0] == 'D':
        if not S.isEmpty():
            while i[1] in S.item:
                S.delete(int(i[1]))
        else:
            print(-1)
    elif i[0] == 'LD':
        if not S.isEmpty():
            for y in S.item:
                if int(y) < int(i[1]):
                    temp.add(int(y))
                while not temp.isEmpty():
                    TempPop = temp.pop()
                    print('Delete =',TempPop,'Because',TempPop,'is less than',int(i[1]))
                    S.lessthanDelete(TempPop)
        else:
            print('-1')
    elif i[0] == 'MD':
        if not S.isEmpty():
            for y in S.item:
                if int(y) > int(i[1]):
                    temp.add(int(y))
                while not temp.isEmpty():
                    TempPop = temp.pop()
                    print('Delete =',TempPop,'Because',TempPop,'is more than',int(i[1]))
                    S.morethanDelete(TempPop)
        else:
            print('-1')

print('Value =',S.item)