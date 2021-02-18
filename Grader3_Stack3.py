class Stack:
    def __init__(self):
        self.item = []

    def push(self,item):
        self.item.append(item)

    def pop(self):
        if len(self.item) > 0:
            return self.item.pop()
        else:
            print('list is empty')

    def isEmpty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)

def postfix():
    print(' ***Postfix expression calcuation***')
    Inp = input('Enter Postfix expression : ').split()
    s = Stack()

    for i in Inp:
        if i in ('+','-','*','/'):
            op1, op2 = s.pop(), s.pop()
            if i == '+':
                s.push(op2+op1)
            elif i == '-':
                s.push(op2-op1)
            elif i == '*':
                s.push(op2*op1)
            elif i == '/':
                s.push(op2/op1)
        else:
            s.push(int(i))

    if not s.isEmpty():
        print('Answer : ','{:.2f}'.format(s.pop()))
    else:
        print('list is [] , cannot pop.')

postfix()
