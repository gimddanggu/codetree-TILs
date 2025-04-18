n = int(input())
arr = list(map(int, input().split()))

for idx, a in enumerate(arr):
    if idx % 2 == 0: # 인덱스는 짝수인게 홀수번째
        sort_arr = sorted(arr[:idx+1])
        print(sort_arr[idx//2], end = ' ') 
# Please write your code here.