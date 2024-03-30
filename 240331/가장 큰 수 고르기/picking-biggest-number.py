import sys

arr = list(map(int, input().split()))


maxVal = arr[0]
for i in arr[1:]:
    if i > maxVal:
        maxVal = i

print(maxVal)