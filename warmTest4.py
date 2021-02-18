print('*** Minesweeper ***')
b = input('Enter input(5x5) : ').split(',')
print('\n')

for i in range(5):
    b[i] = b[i].split()
    print(b[i])

print('\n')

for i in range(5):
    for z in range(5):
        if(b[i][z] == '-'):
            b[i][z] = 0
            if(i-1 >= 0 and b[i-1][z] == '#'): 
                b[i][z] += 1
            if(i-1 >= 0 and z+1 <= 4 and b[i-1][z+1] == '#'): 
                b[i][z] += 1
            if(z+1 <= 4 and b[i][z+1] == '#'): 
                b[i][z] += 1
            if(i+1 <= 4 and z+1 <= 4 and b[i+1][z+1] == '#'): 
                b[i][z] += 1
            if(i+1 <= 4 and b[i+1][z] == '#'): 
                b[i][z] += 1
            if(i+1 <= 4 and z-1 >= 0 and b[i+1][z-1] == '#'): 
                b[i][z] += 1
            if(z-1 >= 0 and b[i][z-1] == '#'): 
                b[i][z] += 1
            if(z-1 >= 0 and i-1 >=0 and b[i-1][z-1] == '#'):
                b[i][z] += 1
        b[i][z] = str(b[i][z])

print(*b,sep=('\n'))

