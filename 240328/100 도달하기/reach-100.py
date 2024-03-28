num = int(input())
arr = []
arr.append(1)
arr.append(num)

for i in range(2,100):
    arr.append(arr[i-2] + arr[i-1])
    if arr[i] >= 100:
        break;

for a in arr:
    print(a, end=' ')