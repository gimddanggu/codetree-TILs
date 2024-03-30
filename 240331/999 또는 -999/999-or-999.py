arr = list(map(int, input().split()))
minVal = maxVal = arr[0]

idx = -1
if 999 in arr:
    idx = arr.index(999)
elif -999 in arr:
    idx = arr.index(-999)

for i in range(1, idx):
    if arr[i] < minVal:
        minVal = arr[i]
    if arr[i] > maxVal:
        maxVal = arr[i]

print(maxVal, minVal)