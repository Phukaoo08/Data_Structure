print('*** multiplication or sum ***')
a,b = map(int,input('Enter num1 num2 : ').split())
out = 0
if((a*b) > 1000):
    print('The result is ' + str(a+b))
elif((a*b) <= 1000):
    print('The result is ' + str(a*b))
    