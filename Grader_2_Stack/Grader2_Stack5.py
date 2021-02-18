class Stack:
    def __init__(self):
        self.item = []

    def push(self,item):
        self.item.append(item)

    def pop(self):
        if len(self.item) < 1:
            return 0
        return self.item.pop()

    def isEmpty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)

    def peek(self):
        return self.item[-1]
    
    def __str__(self):
        return str(self.item)

    def delete(self,item):
        if len(self.item) > 0:
            self.item.remove(item)
        else:
            return 0

if __name__ == "__main__":
    print('******** Parking Lot ********')
    m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
    m,n = int(m), int(n)
    car = Stack()

    for i in s:
        if i == ',' or i == '0':
            pass
        else:
            car.push(int(i))

    if o == 'arrive':
        if n in car.item:
            print('car',n,'already in soi')
        elif car.size() < m:
            car.push(int(n))
            print('car',n,'arrive! : Add Car',n)
        else:
            print('car',n,'cannot arrive : Soi Full')
    elif o == 'depart':
        if car.isEmpty():
            print('car',n,'cannot depart : Soi Empty')
        else:
            if n in car.item:
                car.delete(n)
                print('car',n,'depart ! : Car',n,'was remove')
            elif n not in car.item:
                print('car',n,'cannot depart : Dont Have Car',n)
    
    print(car.item)