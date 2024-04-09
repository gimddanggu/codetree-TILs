strr = input()
result = ''
for i in strr:
    if i >= 'A' and i <= 'Z':
        result += i.lower()

    elif i >= 'a' and i <= 'z':
        result += i.upper()
print(result)