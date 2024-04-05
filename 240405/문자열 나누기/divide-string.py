n = int(input())
n_arr = list(input().split())

strr = "".join(n_arr)
#print(strr)
#print(len(strr))

for i in range(len(strr)):
    if i % 5 == 0 and i != 0:
        print()
    print(strr[i], end = '')