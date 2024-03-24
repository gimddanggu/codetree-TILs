arr = list(map(int,input().split()))

#pp, p = arr[0], arr[1]
'''
for i in range(10):
    pp, p = p, pp + p
    print(pp, end = ' ')
'''
for i in range(3,11):
    arr.append((arr[i-3]+arr[i-2]) % 10)

for i in range(10):
    print(arr[i], end=' ')