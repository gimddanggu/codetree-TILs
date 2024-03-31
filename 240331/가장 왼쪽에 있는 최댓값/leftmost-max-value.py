n = int(input())
n_list = list(map(int, input().split()))

result = []
max_val = -1
# 최대값 찾기
'''
for m in range(n):
    if n_list[m] > max_val:
        max_val = n_list[m]
#  같은 값이 존재해도 가장 왼쪽원소 인덱스 추출
idx = n_list.index(max_val)
result.append(idx+1)
max_val = -1
for m in range(idx):
    if n_list[m] > max_val:
        max_val = n_list[m]
#  같은 값이 존재해도 가장 왼쪽원소 인덱스 추출
idx = n_list.index(max_val)
result.append(idx+1)
'''
idx = n
while(True):
    max_val = -1
    for m in range(idx):
        if n_list[m] > max_val:
            max_val = n_list[m]
    idx = n_list.index(max_val)      #  같은 값이 존재해도 가장 왼쪽원소 인덱스 추출
    result.append(idx+1)

    if idx == 0:
        break;

for i in result:
    print(i, end=' ')
#print(idx, max_val)