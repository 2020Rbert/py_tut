import re
# trennt Elemnte, anhand der Speratren
def split_user_input(input):
    return re.split(r'(\+|\-|\*|\/)', input)

def calc_the_list(liste, func):
    index = 0
    ergebnis = int(liste[index])

    while index < len(liste) - 2:
        operator = liste[index + 1]
        next_int = int(liste[index + 2])
        ergebnis = func(ergebnis, next_int, operator)
        index += 2

    return ergebnis

def calaculate(first_int, second_int, operator):
    if operator == '+':                     
        return first_int + second_int
    elif operator == '-':
        return first_int - second_int
    elif operator == '*':
        return first_int * second_int
    elif operator == '/':
        return first_int / second_int
    elif operator == '%':
        return first_int % second_int
    else:
        raise ValueError(f"Unbekannter Operator: {operator}")


#Input 
user_input = input("Taschenrechner: ['+', '-', '*', '÷', '%', 'd' = double ] möglich\n")
#String Spliting
splitted_string = split_user_input(user_input)
print(splitted_string)
calc_the_list(user_input, calaculate)