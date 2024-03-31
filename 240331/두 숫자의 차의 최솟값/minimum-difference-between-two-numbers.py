n = int(input())
n_list = list(map(int, input().split()))

sub_min = 1
for a in range(n):
    for b in range(a+1, n):
        result = n_list[a] - n_list[b] if n_list[a] > n_list[b] else n_list[b] - n_list[a]

        if sub_min > result:
            sub_min = result


print(sub_min)