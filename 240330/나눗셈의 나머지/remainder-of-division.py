t = tuple(map(int, input().split()))
a, b = t[0], t[1]
r_sum = 0
cnt_arr = [0]*(b+1)
remain_arr = []
result_arr = []
while(True):
    remain_arr.append(a % b)
    a = a // b

    if a == 0:
        break;

for elem in remain_arr:
    cnt_arr[elem] += 1

for i in cnt_arr:
    r_sum += i ** 2

print(r_sum)