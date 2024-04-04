n = int(input())

arr = [input() for _ in range(n)]
string_cnt = 0
cnt = 0

for i in arr:
    string_cnt += len(i)
    if i[0] == 'a':
        cnt += 1

print(f"{string_cnt} {cnt}")