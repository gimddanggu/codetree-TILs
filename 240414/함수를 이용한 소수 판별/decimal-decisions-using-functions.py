# a, b가 주어짐
# a 이상 b 이하의 소수들의 합 구하기
# 함수 사용

# 소수: 1과 자기 자신으로만 나누어 떨어져야 한다.

# 입력값이 하나만 오는 경우 false 처리
# 입력값이 두개 오는 경우 정상 처리
# 1. 소수 판별 함수, 2. 입력 받은 값 몇 개인지 확인하여 구분해주는 함수


def sol(arr):
    sum_n = 0
    if len(arr) == 2:
        for i in range(arr[0], arr[1]+1):
            sum_n += sol_prime_num(i)
        return sum_n
    return 0

def sol_prime_num(n):
    if n == 1:
        return 0

    for i in range(2, n):
        if n % i == 0:
            return 0
    return n

    
arr_n = list(map(int, input().split()))  
print(sol(arr_n))