strr = input()
# print(strr[:-1])

#for i in range(3):
while(True):
    n = int(input())
    if n >= len(strr):
        strr = strr[:-1]

    else: 
        strr = strr[:n] + strr[n+1:]

    print(strr)

    if len(strr) == 1:
        break