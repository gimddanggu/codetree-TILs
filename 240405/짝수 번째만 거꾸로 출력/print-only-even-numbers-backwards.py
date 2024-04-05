strr = input()

for i in range(len(strr)-1, -1, -1):
    if i % 2 != 0:
        print(strr[i], end = '')