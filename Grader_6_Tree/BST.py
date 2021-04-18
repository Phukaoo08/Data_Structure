class Node:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Queue:

    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)

    def enqueue(self,data):
        self.item.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.item.pop(0)

class Stack:

    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)

    def push(self,data):
        self.item.append(data)

    def pop(self):
        if not self.is_empty():
            return self.item.pop()

class BST:

    def __init__(self):
        self.root = None

    def insert(self,data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                if data > currentNode.data:
                    if currentNode.right is None:
                        currentNode.right = newNode
                        break
                    else:
                        currentNode = currentNode.right
                elif data < currentNode.data:
                    if currentNode.left is None:
                        currentNode.left = newNode
                        break
                    else:
                        currentNode = currentNode.left
        return self.root

    def in_order(self, node):
        if node == None:
            return
        else:
            self.in_oder(node.left)
            print(node.data, end = ' ')
            self.in_oder(node.right)

    def pre_order(self, node):
        if node == None:
            return
        else:
            print(node.data, end = ' ')
            self.pre_oder(node.left)
            self.pre_oder(node.right)

    def post_order(self, node):
        if node == None:
            return
        else:    
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end = ' ')

    def min(self):
        node = self.root
        while node.left is not None:
            node = node.left
        return node.data

    def max(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node.data
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

if __name__ == '__main__':
    T = BST()
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in inp:
        root = T.insert(i)
    T.printTree(root)