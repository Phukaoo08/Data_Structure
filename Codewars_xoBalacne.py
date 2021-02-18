Inp = input('Enter Input : ')

def xo():
    checkXO = ''
    count_x = 0
    count_o = 0

    for i in Inp:
        checkXO = checkXO + i
        if i == 'x' or i == 'X':
            count_x = count_x + 1
        elif i == 'o' or i == 'O':
            count_o = count_o + 1
    if count_o == count_x:
        State = 'True'
    elif count_o != count_x:
        State = 'False'
    
    print(checkXO)
    print(State)

xo()