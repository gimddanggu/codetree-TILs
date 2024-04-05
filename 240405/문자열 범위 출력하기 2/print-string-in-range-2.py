strr = input()
n = int(input())
leng = len(strr)
rev_str = strr[::-1]

if n > leng:
    print(rev_str)

else:
    for i in range(n):
        print(rev_str[i], end = '')