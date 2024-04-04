n = int(input())
arr = [input() for _ in range(n)]
c = input()
string_len, cnt = 0, 0

for i in arr:
    if c == i[0]:
        string_len += len(i)
        cnt += 1
print(f"{cnt} {string_len / cnt:.2f}")