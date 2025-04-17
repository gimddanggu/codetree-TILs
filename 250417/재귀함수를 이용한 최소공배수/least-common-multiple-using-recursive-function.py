n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def sol(a, b, i):
    if i == n:
        return a
    if a < b:
        a, b = b, a

    if a % b == 0:
        return sol(a, arr[i], i+1)
    else :
        return sol(a*b, arr[i], i+1)
print(sol(arr[0], arr[1], 1))

