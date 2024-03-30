import sys
cn = int(input())
nList = list(map(int, input().split()))
minVal = nList[0]
cnt = 1
for i in nList[1:]:
    if i < minVal:
        minVal = i 
        cnt = 1
    elif i == minVal:
        cnt += 1


print(minVal, cnt)