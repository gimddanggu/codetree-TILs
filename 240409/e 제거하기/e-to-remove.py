strr = input()

for i in range(len(strr)-1):
    
    if strr[i] == 'e':
        re_strr = strr[:i] + strr[i+1:]
        break;

print(re_strr)