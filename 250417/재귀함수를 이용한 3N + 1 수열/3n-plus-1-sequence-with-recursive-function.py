n = int(input())

# Please write your code here.

def sol(n):
    if n <= 1:
        return 0
    if n % 2 == 0:
        n  /= 2
    else:
        n = n*3 + 1

    return sol(n)+1

print(sol(n)) 