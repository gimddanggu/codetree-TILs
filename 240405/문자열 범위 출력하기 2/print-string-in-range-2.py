strr = input()
n = int(input())
leng = len(strr)
for i in range(leng - 1 , leng - n -1, -1):
    print(strr[i], end = '')