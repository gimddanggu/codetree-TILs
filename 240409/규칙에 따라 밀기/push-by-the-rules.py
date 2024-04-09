strr = input()
q = list(input())

for i in range(len(q)):
    if q[i] == 'L':
        strr = strr[1:] + strr[0]

    else:
        strr = strr[-1] + strr[:-1]
print(strr)