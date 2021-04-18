even_number = ['0','2','4','6','8','10']
odd_number = ['1','3','5','7','9']
OneToTen = []
Number = ['6','3','4','2','5','1']

OneToTen = even_number.extend(odd_number)
OneToTen = even_number
print(OneToTen)


# extend' add the whole list to list // not return value
OneToTen.extend(odd_number)
print(OneToTen)

# append' add element to the back
OneToTen.append(even_number[1])
print(OneToTen)

# insert' add element w/ locations // push right
OneToTen.insert(0,'Number')
print(OneToTen)

# remove' remove element in lists
OneToTen.remove('1')
print(OneToTen)

# pop' remove last element in the lists
OneToTen.pop()
print(OneToTen)

# index' tell the position of the element in lists
print(OneToTen.index('Number'))

# clear' clear all the elements in lists
OneToTen.clear()
print(OneToTen)

# sort' ascending order of lists
Number.sort()
print(Number)

# reverse' reverse order from front to back back to front
Number.reverse()
print(Number)

# copy' copy lists from another lists
Number = OneToTen.copy()
print(Number)