def get_two_numbers() -> float:
    a = float(input(f'enter the number a \n'))
    b = float(input(f'enter the number b \n'))
    return a, b

what_calculate = 0
while what_calculate <= 4:
    what_calculate = int(input('What u wanna calculate'))
    if(what_calculate == 1):
        a, b = get_two_numbers()
        print(a + b)
    if(what_calculate == 2):
        a, b = get_two_numbers()
        print(a - b)
    if(what_calculate == 3):
        a, b = get_two_numbers()
        print(a * b) 
    if(what_calculate == 4):
        a, b = get_two_numbers()
        try:
            print(a / b)
        except ZeroDivisionError:
            print('impossible to divide by 0')