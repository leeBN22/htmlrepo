# To get the maximum of three numbers

def max(a,b,c):
    if a>b and a > c:
        print(f'The maximum of three numbers is {a}')
    elif b > a and b > c:
        print(f'The maximum of three numbers is {b}')
    else:
        print(f'The maximum of three numbers is {c}')

n1 = int(input('Input number1: '))
n2 = int(input('Input number2: '))
n3 = int(input('Input number3: '))
max(n1,n2,n3)