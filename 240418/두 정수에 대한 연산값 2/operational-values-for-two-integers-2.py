a, b = tuple(map(int, input().split()))


def sol(num1, num2):
    if num1 > num2:
        num1 *= 2
        num2 += 10

    else:
        num2 *= 2
        num1 += 10
    
    return num1, num2

a, b = sol(a, b) 
print(a, b)