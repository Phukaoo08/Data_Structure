Inp = input('Enter inpur : ')

def validate_pin():
    
    ATM_code = ''
    
    if len(Inp) >= 4 and len(Inp) <=6:
        for i in Inp:
            if ord(i) >= 48 and ord(i) <= 57:
                ATM_code = ATM_code + i
            else:
                print('ATM code must be a number!.')
                return 0
    else:
        print('ATM code must be a number between 4-6 digits!')
        return 0
    
    print('ATM code is ' + ATM_code)

validate_pin()
