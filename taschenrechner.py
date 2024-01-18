import re
from icecream import ic


def split_calculation_input(input):
    return re.split(r'(\+|\-|\*|\/)', input)

def calaculate(first_int, second_int, operator):
    if operator == '+':                     
        return first_int + second_int
    elif operator == '-':
        return first_int - second_int
    elif operator == '*':
        return first_int * second_int
    elif operator == '/':
        return first_int / second_int
    
def remove_nachkomma_null(zahl):
    str_zahl = str(zahl)
    if str_zahl[-1] == '0' and str_zahl[-2] =='.':
        return round(zahl)
    else:
        return zahl

def choose_the_numbers(splited_list_user):
    global first_int 
    global operator 
    global second_int 
    global counter
    global user_input

    if counter - 1 == 0:
        
        
        ic(f'der verdammte innere count: {counter}')
        first_int = int(splited_elements[0])
        operator = splited_elements[1]
        second_int = int(splited_elements[2])
    else:
        first_int = result
        operator = splited_list_user[0]
        second_int = int(splited_list_user[1])

        user_input = input(remove_nachkomma_null(result))


counter = 0
first_int = None
operator = None
second_int = None
user_input = input('Your input: ')
while True:

    splited_elements = split_calculation_input(user_input)
    choose_the_numbers(splited_elements)
    counter += 1

    result = calaculate(first_int, second_int, operator)
    print(f"Ergebnis: {remove_nachkomma_null(result)}")
    #first_int = result
    #user_input = input(result) 
    ic(counter)