st = input()
c = input()
cnt = 0

for i in range(len(st)):
    if st[i] == c:
        cnt += 1

print(cnt)