def hel(n):
    if n == 0:
        return

    hel(n-1)
    print("HelloWorld")


n = int(input())

hel(n)