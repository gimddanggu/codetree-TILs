a, b = tuple(input().split())
num1, num2 = '', ''
for i in a:
    if i.isdigit():
        num1 += i
    else:
        break;

#print(num1)
for i in b:
    if i.isdigit():
        num2 += i
    else:
        break;

print(int(num1) + int(num2))