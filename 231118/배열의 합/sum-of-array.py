a = [list(map(int, input().split())) for i in range(4)]
sumList = []

for i in range(len(a)):
    sumList.append(sum(a[i]))
    print(sumList[i])