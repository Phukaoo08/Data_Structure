class Stack:
    def __init__(self, list = None):
        if list is None:
            self.item = []
        else:
            self.item = list

    def push(self,item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def empty(self):
        return self.item.clear()
        
    def isEmpty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)

def reverseList(classic):
    create = Stack()
    while not classic.isEmpty():
        create.push(classic.pop()) ### create new stack w/ reversing old stack
    return create

Inp = input('Enter Input : ').split(',')

stack_tree = Stack()
stack_main = Stack()
stack_see = Stack()
lastTree = []

for i in Inp:
    i = i.split()
    if i[0] == 'A':
        stack_tree.push(int(i[1]))
    elif i[0] == 'B':
        stack_main = reverseList(stack_tree)

        while not stack_main.isEmpty():
            lastTree = stack_main.pop()
            stack_tree.push(lastTree)

            if stack_see.isEmpty():
                stack_see.push(lastTree)
                continue
            
            elif lastTree < stack_see.peek():
                stack_see.push(lastTree)

            elif lastTree >= stack_see.peek():
                while not stack_see.isEmpty() and lastTree >= stack_see.peek():
                    stack_see.pop()
                else:
                    stack_see.push(lastTree)
        
        print(stack_see.size())
        stack_see.empty()