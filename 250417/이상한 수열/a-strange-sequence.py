N = int(input())

# Please write your code here.
def sol(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return (sol(n//3) + sol(n-1))

print(sol(N))