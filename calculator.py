#asks for number input with given string
#if not valid number entered, repeats
def number_input(string):
    while True:
        try:
            a = float(input(string))
            break
        except ValueError:
            print('Invalid input')
    return a

first_number = number_input('Enter a first number: ')
second_number = number_input('Enter a second number: ')

while True:
    print('Enter:')
    print('+ for sum')
    print('- for subtraction')
    print('* for multiplication')
    print('/ for division')
    print('^ for power')
    print('// for floor division')
    print('% for mod')
    print('\nn for re-enter numbers')
    print('x for exit')

    #selection handler
    operation = input('Enter: ')
    if operation == '+': result = first_number + second_number
    elif operation == '-': result = first_number - second_number
    elif operation == '*': result = first_number * second_number
    elif operation == '^': result = first_number ** second_number
    elif operation == '/':
        try:
            result = first_number / second_number
        except ZeroDivisionError:
            result = 'Zero division error'
    elif operation == '//':
        try:
            result = first_number // second_number
        except ZeroDivisionError:
            result = 'Zero division error'
    elif operation == '%':
        try:
            result = first_number % second_number
        except ZeroDivisionError:
            result = 'Zero division error'

    elif operation == 'n':
        first_number = number_input('Enter a first number: ')
        second_number = number_input('Enter a second number: ')
        continue
    elif operation == 'x':
        break
    else:
        print('Invalid input')
        wait = input('Press Enter to continue')
        continue

    #output result
    print(first_number, operation, second_number, '=', result)
    wait = input('Press Enter to continue')
    

    

