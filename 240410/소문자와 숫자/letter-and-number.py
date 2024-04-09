strr = input()
strr = strr.lower()

for i in strr:
    if i.isalpha() or i.isdigit():
        print(i, end='')