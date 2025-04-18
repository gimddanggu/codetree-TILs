n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]
n_str = [ss for ss in str if ss[:len(t)] == t]

print(sorted(n_str)[k-1])
# Please write your code here.