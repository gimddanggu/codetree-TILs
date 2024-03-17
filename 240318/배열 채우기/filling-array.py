arr = list(map(int, input().split()))

#for i in range(len(arr)):
#    print(arr[len(arr)-i-1], end=' ')
cnt = 0
for i in arr:
    cnt += 1
    if i == 0:
        break;
if cnt < 10:
    cnt -= 1
for i in reversed(arr[:cnt]):
    print(i, end=' ')