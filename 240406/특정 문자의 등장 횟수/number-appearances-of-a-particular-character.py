strr = input()

finds = ['ee', 'ed']
cntee, cnted = 0, 0

for i in range(len(strr)-1):
    if strr[i] == 'e' and strr[i+1] == 'e':
        cntee += 1
    if strr[i] == 'e' and strr[i+1] == 'b':
        cnted += 1
    
print(cntee, cnted)