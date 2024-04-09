str1 = input()
str2 = input()
num1, num2 = '', ''

for i in str1:
    if i >= '0' and i<= '9':
        num1 += i

for i in str2:
    if i >= '0' and i<= '9':
        num2 += i

print(int(num1) + int(num2))