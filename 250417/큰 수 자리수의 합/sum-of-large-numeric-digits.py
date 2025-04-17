a, b, c = map(int, input().split())
num = a*b*c
numStr = str(num)

def sol(numStr, i, sumN):
    if i == len(numStr):
        return sumN
    
    sumN += int(numStr[i])
    return sol(numStr, i+1, sumN)

print(sol(numStr, 0, 0))