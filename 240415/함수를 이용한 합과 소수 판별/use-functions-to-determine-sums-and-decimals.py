# a 이상 b 이하 중 소수이면서 자릿수의 합이 짝수인 수의 개수
# 소수 판별 함수 
# 자리 수 합 짝수 판별 함수

def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

def even(n):
    num1, num2 = n // 10, n % 10
    if (num1 + num2) % 2 == 0:
        return True
    
    return False


cnt = 0
a, b = tuple(map(int, input().split()))
for i in range(a, b+1):
    if prime(i) and even(i):
        cnt += 1
print(cnt)