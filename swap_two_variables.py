# user inputs two numbers. One number is assigned to a variable,
# the other is assigned to another variable. The task is to invert the variables,
# so that the first variable contains the second number, the first number is
# in the second variable.


def swap_ab(a,b):
    a, b = b, a
    print(f'After a = {a} and b = {b}')

'''  method 1:
   temp = a
    a = b
    b = temp
    print(f'After a = {a} and b = {b}')
    method 2:
     a = a+b 
    b = a-b
    a = a-b
'''
a = int(input('Input value a: '))
b = int(input('Input value b: '))

print(f'Before a = {a} and b = {b}')
swap_ab(a,b)