def sol(n):
    if n % 100 == 0 and n % 400 != 0:
        return 'false'
    if n % 4 != 0:
        return 'false'

    return 'true'


n = int(input())
print(sol(n))