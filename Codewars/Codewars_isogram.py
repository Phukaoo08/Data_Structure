Inp = input('Enter input : ')

def is_isogram():
    checkASCIIList = []
    duplicateList = []
    checkChar = ''
    for i in Inp:
        if i not in duplicateList and i not in duplicateList and ord(i) not in checkASCIIList:
            duplicateList.append(i)
            checkChar = checkChar + i
            checkASCIIList.append(ord(i))
            if ord(i) >= 65 and ord(i) <= 90:
                i = ord(i) + 32
                checkASCIIList.append(i)
            elif ord(i) >= 97 and ord(i) <= 122:
                i = ord(i) - 32
                checkASCIIList.append(i)
        else:
            print('there is a same char in this list')
            return 0
    print(checkChar)
    print('This string is a Isogram')

is_isogram()