print('*** multiplication or sum ***')
Inp1,Inp2 = map(int,input('Enter num1 num2 : ').split())

if Inp1 * Inp2 > 1000:
    print('The result is ',str(Inp1 + Inp2))
elif Inp1 * Inp2 <= 1000:
    print('The result is ',str(Inp1 * Inp2))