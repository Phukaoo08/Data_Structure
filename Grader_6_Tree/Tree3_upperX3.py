class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
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
                    #----------------------------------
                elif data < currentNode.data:
                    if currentNode.left is None:
                        currentNode.left = newNode
                        break
                    else:
                        currentNode = currentNode.left
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def printx3(self, node, data,level = 0):
        if node != None:
            if int(node.data) > int(data):
                node.data = node.data * 3
            self.printx3(node.right, data, level + 1)
            print('     ' * level, node)
            self.printx3(node.left, data, level + 1)

if __name__ == '__main__':
    T = BST()
    inp, k = input('Enter Input : ').split('/')
    inp = [int(i) for i in inp.split()]
    for i in inp:
        root = T.insert(i)
    T.printTree(root)
    print('--------------------------------------------------')
    T.printx3(root,k)