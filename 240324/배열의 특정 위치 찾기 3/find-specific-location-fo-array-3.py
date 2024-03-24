arr = list(map(int, input().split()))

sum1 = 0

for i in range(len(arr)):
    if arr[i] == 0:
        sum1 = sum(arr[i-1::-1])
        break;


print(sum1)