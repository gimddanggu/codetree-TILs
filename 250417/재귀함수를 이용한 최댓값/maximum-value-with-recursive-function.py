n = int(input())
arr = list(map(int, input().split()))

max_num = arr[0]
def sol(max_num, idx):
    if idx == n:
        return max_num
    
    if arr[idx] > max_num:
        max_num = arr[idx]
        # print(max_num)
    
    return sol(max_num, idx+1)

print(sol(max_num, 1))
