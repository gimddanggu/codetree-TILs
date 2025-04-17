N = int(input())

# Please write your code here.
i = 1
arr = [2, 4]
def sol(N, i, a, b):
    if N == 1:
        return a

    if i == N:
        return b
    
    c = (a * b) % 100
    return sol(N, i+1, b, c)

print(sol(N, 2, 2, 4))