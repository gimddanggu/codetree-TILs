n = int(input())
sum_n = 0
for i in range(n):
    sum_n += int(input())

sum_n = str(sum_n)
print(sum_n[1:] + sum_n[0])