# a, b가 주어짐
# a 이상 b 이하의 소수들의 합 구하기
# 함수 사용

# 소수: 1과 자기 자신으로만 나누어 떨어져야 한다.

def sol_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

    
a, b = tuple(map(int, input().split()))
n_sum = 0
for i in range(a, b+1):    
    if sol_prime_num(i):
        n_sum += i

print(n_sum)