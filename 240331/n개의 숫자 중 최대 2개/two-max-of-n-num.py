n = int(input())
n_list = list(map(int, input().split()))
t = 1
#start = 0
#max_val = n_list[0]
for i in range(n-1):
    cnt = 0

    for j in range(n-1):
        if n_list[j] < n_list[j+1]:
            n_list[j], n_list[j+1] = n_list[j+1], n_list[j]
        elif n_list[j] == n_list[j+1]:
            cnt += 1
        
        else:
            cnt += 1
    if cnt == n-1:
        break;

print(n_list[0], n_list[1])