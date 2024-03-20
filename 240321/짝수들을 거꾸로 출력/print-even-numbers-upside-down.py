num = int(input())
arr = list(map(int, input().split()))

even_arr = []

for i in arr:
    if i % 2 == 0:
        even_arr.append(i)

for i in even_arr[::-1]:
    print(i, end=' ')