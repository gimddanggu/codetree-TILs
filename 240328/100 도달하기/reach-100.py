num = int(input())
arr = [1, num]


for i in range(2,100):
    arr.append(arr[i-2] + arr[i-1])
    if arr[i] >= 100:
        break;

for a in arr:
    print(a, end=' ')