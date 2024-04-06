strr = input()

while(True):
    n = int(input())
    strr = strr[:n] + strr[n+1:]
    
    if n > len(strr):
        strr = strr[:-1]

    print(strr)
    
    if len(strr) == 1:
        break