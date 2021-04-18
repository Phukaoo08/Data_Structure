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

    def checkpos(self, node, level = 0):
        checklist = []
        if node != None:
            checklist.append(node.right.data)
            checklist.append(node.data)
            checklist.append(node.left.data)
        return checklist

if __name__ == '__main__':
    T = BST()
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in range(1, len(inp)):
        root = T.insert(inp[i])
    T.printTree(root)
    T.checkpos(root)