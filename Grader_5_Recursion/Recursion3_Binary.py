def numRecursive(number, k):
    if number == 0:
        return print(str(bin(number)).replace('0b', '').zfill(k))
    return numRecursive(number - 1, k), print(str(bin(number)).replace('0b', '').zfill(k))


num = int(input('Enter Number : '))
if num < 0:
    print('Only Positive & Zero Number ! ! ! ')
else:
    numRecursive(2 ** num - 1, num)