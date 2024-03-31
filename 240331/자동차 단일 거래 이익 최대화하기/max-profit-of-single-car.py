n = int(input())
n_list = list(map(int, input().split()))
result_arr = [0]
# 오른쪽에 있는 가장 큰 수 - 왼쪽에 있는 작은 수
'''min_val = 1001
for idx, val in enumerate(n_list):
    if val < min_val and idx != len(n_list):
        min_val = i


        9 7 4 6 3 2
        3 4 3 8 9 2 3 6

          4 9 2 3 6 7

# 최대값 다음에 최소값오는경우 -> 최소값 다음에 오는 가장 큰 값과 계산
# 이익이 나는 경우 작은 숫자 다음 큰 숫자가 있을 때
# 이익 안 나는 경우 큰 숫자 다음에 작은 숫자만 있을 때 

9 2 2 5 6
3 5 2 4
 6 3 5 2 1 n = 5
 # 처음 한숫자 선택해서 리스트에 그 값보다 큰 수가 있다면 차이를 계산
 6 3 3 5 5 2 2 1
 6 5 3 2 5 1
 6 2 3 1
 6 1
'''
for i in range(n):
    for j in range(i+1, n):
        profit = n_list[i] - n_list[j]
        if (profit) < 0:
            result_arr.append(profit * -1)

print(max(result_arr))