StArr = ["apple", "banana", "grape", "blueberry", "orange"]

c = input()
cnt = 0

for i in StArr:
    if c == i[2] or c == i[3]:
        cnt += 1
        print(f"{i}")
print(cnt)