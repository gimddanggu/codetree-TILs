a, b = input().split()
arr = list(map(int, input().split()))

cnt = 0

for num in arr:
    if num == int(b):
        cnt += 1
print(cnt)

#print(arr.count(int(b)))