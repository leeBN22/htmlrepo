# when user enters a number, its sum of the numbers till the number entered is displayed

def sum(n):
    result = 0
    for i in range(1, n+1):
        result += i
    print(f'Sum of {n} is {result}')

number = int(input('Input number: '))
sum(number)