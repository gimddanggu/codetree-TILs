arr = list(map(int, input().split()))

for i in reversed(arr):
    if i == 0:
        continue;
    print(i, end=' ')