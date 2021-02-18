class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False

    def size(self):
        return len(self.stack)

print(' *** Stack implement by Python list***')
Inp = input('Enter data to stack : ').split()
s = Stack()

for i in Inp:
    s.push(i)
print(s.size(),'Data in stack : ',s.stack)

while not s.isEmpty():
    s.pop()
print(s.size(),'Data in stack : ',s.stack)