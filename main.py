from get_two_numbers import get_two_numbers

what_calculate = 0
while what_calculate <= 5:
    print("""
          Addition - 1
          Subtraction - 2
          Multiplication - 3
          Division - 4
          MOD - 5""")
    what_calculate = int(input('What u wanna calculate'))
    if(what_calculate == 1):
        a, b = get_two_numbers()
        print(f'Sum of a = {a} and b = {b} is {a + b}')
    if(what_calculate == 2):
        a, b = get_two_numbers()
        print(f'Subtraction of a = {a} and b = {b} is {a - b}')
    if(what_calculate == 3):
        a, b = get_two_numbers()
        print(f'Multiplication of a = {a} and b = {b} is {a * b}') 
    if(what_calculate == 4):
        a, b = get_two_numbers()
        try:
            print(f'Divison of a = {a} and b = {b} is {a / b}')
        except ZeroDivisionError:
            print('impossible to divide by 0')
            
    if(what_calculate == 5):
        a, b = get_two_numbers()
        print(f'MOD of a = {a} and b = {b} is {a / b}')
        
if __name__ == "__main__":
    pass