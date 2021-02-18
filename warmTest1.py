print('*** Rabit & Turtle ***')
a,b,c,d = map(int,input('Enter Input : ').split())

answer = d*a / (c-b)

print('{:.2f}'.format(answer))