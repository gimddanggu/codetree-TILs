strr = input()
n = int(input())
leng = len(strr)
rev_str = strr[::-1]
if n > leng:
    print(strr)

else:
    for i in range(n):
        print(rev_str[i], end = '')