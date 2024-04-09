strr = input()
strr2 = input()
leng = len(strr2)

while(True):
    if strr2 in strr:
        idx = strr.index(strr2)
        strr = strr[:idx] + strr[idx+leng:]
    else:
        break;
print(strr)