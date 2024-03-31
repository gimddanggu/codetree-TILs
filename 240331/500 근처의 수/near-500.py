n_list = list(map(int, input().split()))

# 500 미만의 가장 큰 수
# 500 초과의 가장 작은 수

u500 = [i for i in n_list if i > 500]
d500 = [i for i in n_list if i < 500]

print(max(d500), min(u500))