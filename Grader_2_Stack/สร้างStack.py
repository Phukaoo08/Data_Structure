class Stack:
    
    def __init__(self):
        self.item = []

    def push(self,item):
        self.item.append(item)

    def pop(self):
        if len(self.item) < 1:
            return None
        else:
            return self.item.pop()

    def isEmpty(self):
        if len(self.item) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.item)

print(' *** Stack implement by Python list ***')
Inp = input('Enter data to stack : ').split()
s = Stack()

for ele in Inp:
    s.push(ele)
print(s.size(),'Data in stack :',s.item)

while not s.isEmpty():
    s.pop()
print(s.size(),'Data in stack :',s.item)