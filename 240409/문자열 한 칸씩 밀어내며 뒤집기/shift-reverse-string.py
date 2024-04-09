strr, q = tuple(input().split())
q = int(q)

for i in range(q):
    n = int(input())
    if n == 1:
        strr = strr[1:] + strr[0]
    elif n == 2:
        strr = strr[-1] + strr[:-1]
    else:
        strr = "".join(reversed(strr))

    print(strr)