k = int(input('Enter Number : '))
answer = 1

def factorial(k,answer):
    if k > 1:
        answer = answer * (k)
        return factorial(k-1,answer)
    return answer
    
print(str(k)+'!','=',factorial(k,answer))
