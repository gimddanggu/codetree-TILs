N = int(input())

# Please write your code here.
i = 1
arr = [2, 4]
def sol(N, i, arr):
    if i == N:
        return
    
    arr.append((arr[i-1] * arr[i-2]) % 100)
    return sol(N, i+1, arr)

sol(N, 2, arr)
print(arr[N-1])