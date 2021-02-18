print('*** Rabbit & Turtle ***')
a,b,c,d = map(int,input('Enter Input : ').split())
out = 0
if(c > b):
    out = (d*a)/(c-b)
print('{:.2f}'.format(out))