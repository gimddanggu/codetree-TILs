import sys
cn = int(input())
nList = list(map(int, input().split()))
minVal = sys.maxsize

for i in nList:
    if i < minVal:
        minVal = i 

result = nList.count(minVal)
print(minVal, result)