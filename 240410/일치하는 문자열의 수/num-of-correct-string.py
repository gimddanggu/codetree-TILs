n, str1 = tuple(input().split())
cnt = 0

for _ in range(int(n)):
    st = input()
    if st == str1:
        cnt += 1

print(cnt)