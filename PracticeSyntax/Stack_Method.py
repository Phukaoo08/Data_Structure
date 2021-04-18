class Stack:
    def __init__(self):
        self.item = []

    def push(self,item):
        self.item.append(item)

    def pop(self):
        if len(self.item) < 1:
            return 'cannot pop, stack is empty.'
        else:
            self.item.pop()

    def isEmpty(self):
        return len(self.item) == 0
        
    def size(self):
        return len(self.item)

    def __str__(self):
        return str(self.item)

s = Stack()
s.push(1)
print(s.pop())