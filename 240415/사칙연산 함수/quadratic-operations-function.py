def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def division(a, b):
    return a // b


oper = ['+', '-', '*', '/']
arr = list(input().split())
num1, num2 = int(arr[0]), int(arr[2])
if arr[1] in oper:
    if arr[1] == '+':
        result = plus(num1, num2)

    if arr[1] == '-':
        result = minus(num1, num2)

    if arr[1] == '*':
        result = multi(num1, num2)

    if arr[1] == '/':
        result = division(num1, num2)

    print(f"{num1} {arr[1]} {num2} = {result}")

else:
    print('False')