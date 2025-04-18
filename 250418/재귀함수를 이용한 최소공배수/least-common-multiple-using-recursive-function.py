n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

# def sol(a, b, i):
#     if i == n:
#         return a
#     if a < b:
#         a, b = b, a

#     if a % b == 0:
#         return sol(a, arr[i], i+1)
#     else :
#         return sol(a*b, arr[i], i+1)
# print(sol(arr[0], arr[1], 1))

def gcd(a, b):  
    r = a % b
    if r == 0:
        return b 

    return gcd(b, r)

def lcm(a, b):
    return (a * b) / gcd(a, b)

for i in range(len(arr)-1):
    arr[i+1] = lcm(arr[i], arr[i+1])

print(int(arr[-1]))

