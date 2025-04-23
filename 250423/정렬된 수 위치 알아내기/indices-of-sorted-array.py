n = int(input())
sequence = list(map(int, input().split()))

arr = [[v, idx] for idx, v in  enumerate(sequence)]
sort_arr = sorted(arr, key=lambda x : x[0])

for i in range(n):
    sort_arr[i].append(i)

sort_arr.sort(key=lambda x: x[1])
for i in range(n):
    print(sort_arr[i][2]+1, end=' ')
