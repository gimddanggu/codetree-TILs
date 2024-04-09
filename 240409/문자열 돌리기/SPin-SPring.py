strr = input()
length_str = len(strr)

for _ in range(length_str+1):
    print(strr)
    strr = strr[-1] + strr[:-1]