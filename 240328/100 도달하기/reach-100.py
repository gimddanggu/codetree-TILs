num = int(input())
arr = [1, num]
cnt = 1

while(True):
    cnt += 1
    arr.append(arr[cnt-2] + arr[cnt-1])
    if arr[cnt] >= 100:
        break;

for a in arr:
    print(a, end=' ')