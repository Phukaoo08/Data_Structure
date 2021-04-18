class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        else:
            cur,st = self.head,str(self.head.item) + ''
            while cur.next != None:
                st += str(cur.next.item ) + ''
                cur = cur.next 
            return st

    def isEmpty(self):
        return self.head == None
    
    def append(self,item):
        self._size = self._size + 1
        if self.isEmpty():
            self.head = Node(item)
            return
        else:
            node = self.head
            while(node.next != None):
                node = node.next
            node.next = Node(item)

    def addHead(self,item):
        self._size = self._size + 1
        if self.isEmpty():
            self.head = Node(item)
            return 0
        else:
            node = self.head
            self.head = Node(item)
            self.head.next = node

    def search(self, item):
        node = self.head
        if self.isEmpty():
            return 'No node No data!'
        else:
            while node.next != None:
                if node.item == item:
                    return 'Found'
                else:
                    node = node.next
            if node.item == item:
                return 'Found'
            else:
                return 'Not found!'

    def index(self, item):
        index = 0
        node = self.head
        if self.isEmpty():
            return -1

        if self.size() == 1:
            if node.item == item:
                return index
        
        while node.next != None:
            if node.item == item:
                return index
            else:
                node = node.next
                index = index + 1
        if node.item == item:
            return index
        else:
            return -1

    def size(self):
        return self._size

    def pop(self,pos):
        index = 0
        if pos >= self.size() or pos < 0:
            return 'Out of range'

        if pos == 0 and self.size() == 1:
            self.head = None
        elif pos == 0:
            self.head = None
            self.head = self.head.next
        else:
            node = self.head
            while index != pos -1:
                index = index + 1
            else:
                node.next = node.next.next

        self._size = self._size - 1
        return 'Complete'  

if __name__ == "__main__":
    L = LinkedList()
    inp = input('Enter Input : ').split(',')
    for i in inp:
        if i[:2] == "AP":
            L.append(i[3:])
        elif i[:2] == "AH":
            L.addHead(i[3:])
        elif i[:2] == "SE":
            print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
        elif i[:2] == "SI":
            print("Linked List size = {0} : {1}".format(L.size(), L))
        elif i[:2] == "ID":
            print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
        elif i[:2] == "PO":
            before = "{}".format(L)
            k = L.pop(int(i[3:]))
            print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    print("Linked List :", L)     