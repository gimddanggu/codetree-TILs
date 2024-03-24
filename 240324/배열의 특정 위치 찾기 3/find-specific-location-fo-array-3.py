arr = list(map(int, input().split()))

sum1 = 0

for i in range(len(arr)):
    if arr[i] == 0:
        #print(arr[i-3:i])
        sum1 = sum((arr[i-3:i]))
        break;


print(sum1)