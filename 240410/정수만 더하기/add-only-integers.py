strr = input()
n_sum = 0

for i in strr:
    if i.isdigit():
        i = int(i)
        n_sum += i

print(n_sum)