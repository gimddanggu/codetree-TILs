def re(n):
    if n < 10:
        return n**2

    return re(n // 10) + (n % 10)**2


n = int(input())
print(re(n))