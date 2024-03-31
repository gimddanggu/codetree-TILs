n = int(input())
n_list = list(map(int, input().split()))
#maxNum = max(n_list)
#cnt_list = [0] * (maxNum+1)
cnt_list = [0] * 1001
idx_list = []

# 각 원소의 개수를 구한다
# 원소의 개수가 1인 것 중 최대값 고른다.

for elem in n_list:
    cnt_list[elem] += 1

for idx, c in enumerate(cnt_list):
    if c == 1:
        idx_list.append(idx)

if not idx_list:
    result = -1
else:
    result = max(idx_list)

print(result)

# 개수 배열생성
# 1개인 개수 카운팅
# 개수 배열 비어있으면 -1 else max값 출력

# 카운팅 할 때