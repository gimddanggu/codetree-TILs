a, b = tuple(map(int, input().split()))
cnt = 0
sum_n = a + b
sum_n = str(sum_n)

for i in sum_n:
    if i == '1':
        cnt += 1
print(cnt)