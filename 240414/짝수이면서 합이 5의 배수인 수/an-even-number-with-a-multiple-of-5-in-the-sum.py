def evne_five(n):
    num = int(n[0]) + int(n[1])
    return int(n) % 2 == 0 and num % 5 == 0


n = input()
if evne_five(n):
    print('Yes')
else:
    print('No')