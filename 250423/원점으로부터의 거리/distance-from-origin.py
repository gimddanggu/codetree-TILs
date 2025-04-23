n = int(input())
pos_arr = []
for i in range(n):
    pos_arr.append([i+1, sum(tuple(map(abs,map(int, input().split()))))])
pos_arr.sort(key=lambda x : x[1])

for d in pos_arr:
    print(d[0])