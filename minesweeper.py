print('*** minesweeper ***')
a = input('Enter input : ').split(',')

for i in range(5):
    a[i] = a[i].split()
    print(a[i])

for i in range(5):
    for y in range(5):
        if a[i][y] == '-':
            a[i][y] = 0
            if(i-1 >= 0 and a[i-1][y] == '#'): #check top
                a[i][y] += 1
            if(i-1 >= 0 and y-4 <= 0 and a[i-1][y-4] == '#'): #check top right
                a[i][y] += 10
