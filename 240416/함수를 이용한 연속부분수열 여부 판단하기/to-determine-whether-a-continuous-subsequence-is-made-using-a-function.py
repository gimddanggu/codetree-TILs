c1, c2 = tuple(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


# 수열 b에서 첫번째 숫자를 수열 a 인덱스 찾기
'''if arr2[0] in arr1:
    a = arr1.index(arr2[0])
    
    for i in range(c2):
        if arr1[a+i] != arr2[i]:
            return False

def sol(arr1, arr2):


def check(arr1, arr2):
    for j in range(c1):
        if arr2[0] in arr1:
            a = arr1.index(arr2[0])
        
            for i in range(c2):
                if arr1[a+i] != arr2[i]:
                    arr1 = arr[a+1:]
                    break;
'''

def sol(arr1, arr2):
    for i in range(c1):
        cnt = 0
        if arr1[i] == arr2[0]:
            for j in range(c2):
                if arr1[i+j] != arr2[j]:
                    break;
                cnt += 1
            if cnt == c2:
                return True

    return False



if sol(arr1, arr2):
    print('Yes')
else:
    print('No')