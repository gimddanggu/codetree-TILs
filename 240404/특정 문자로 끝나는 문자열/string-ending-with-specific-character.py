arr = [input() for _ in range(10)]
c = input()
cnt = 0

for a in arr:
    if c == a[-1]:
        print(a)
        cnt += 1

if cnt == 0:
    print("None")