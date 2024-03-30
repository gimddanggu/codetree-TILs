t = tuple(map(int, input().split()))
a, b = t[0], t[1]
#a, b = 1000, 2
r_sum = 0
cnt_arr = [0]*(b+1)
remain_arr = []
result_arr = []
while(a>=1):
    remain_arr.append(a % b)
    a = a // b


for elem in remain_arr:
    cnt_arr[elem] += 1

for i in cnt_arr:
    r_sum += i ** 2

#print(remain_arr)
#print(cnt_arr)
print(r_sum)