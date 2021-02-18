print('*** Minesweeper ***')
a = input('Enter input(5x5) : ').split(',')
print('\n')

for i in range(5):
    a[i] = a[i].split()
    print(a[i])

print('\n')

for i in range(5):
    for z in range(5):
        if(a[i][z] == '-'):
            a[i][z] = 0
            if(i-1 >= 0 and a[i-1][z] == '#'): #check top
                a[i][z] += 1
            if(i-1 >= 0 and z+1 <= 4 and a[i-1][z+1] == '#'): #check top right
                a[i][z] += 1
            if(z+1 <= 4 and a[i][z+1] == '#'): #check right
                a[i][z] += 1
            if(z+1 <= 4 and i+1 <= 4 and a[i+1][z+1] == '#'): #check bottom right
                a[i][z] += 1
            if(i+1 <= 4 and a[i+1][z] == '#'): #check bottom
                a[i][z] += 1
            if(i+1 <= 4 and z-1 >= 0 and a[i+1][z-1] == '#'): #check bottom left
                a[i][z] += 1
            if(z-1 >= 0 and a[i][z-1] == '#'): #check left
                a[i][z] += 1  
            if(i-1 >= 0 and z-1 >= 0 and a[i-1][z-1] == '#'): #check top left
                a[i][z] += 1  
        a[i][z] = str(a[i][z])            


print(*a,sep=('\n'))

            