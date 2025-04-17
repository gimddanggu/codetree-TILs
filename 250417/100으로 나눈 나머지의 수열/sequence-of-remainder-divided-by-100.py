N = int(input())

# Please write your code here.
i = 1
arr = [2, 4]
def sol(N, i, a, b):
    if i == N-1:
        return b
    
    c = (a * b) % 100
    return sol(N, i+1, b, c)

print(sol(N, 1, 2, 4))