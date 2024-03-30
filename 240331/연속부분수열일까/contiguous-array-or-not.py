aNum, bNum = tuple(map(int, input().split()))
aArr = list(map(int, input().split()))
bArr = list(map(int, input().split()))

# 1. b 수열의 첫 번째 원소가 a 수열에 있는지 확인
idx = 0
if bArr[0] in aArr:
# 2. 만약 첫 번째 원소가 a 수열에 있다면 for 문을 돌려 b 수열의 다음항도 a 에 있는지 확인
    aIdx = aArr.index(bArr[0])
    for i in range(1, len(bArr)): # i: 0~ b수열 개수
        if bArr[i] != aArr[aIdx+1]:
            idx = -1
            break;
        aIdx += 1

if idx == -1:
    print('No')
else:
    print('Yes')