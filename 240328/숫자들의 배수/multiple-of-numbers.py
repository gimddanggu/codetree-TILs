num = int(input())
result = num
cnt = 0
while(True):
    if result % 5 == 0:
        cnt += 1
    print(result, end=' ')
    result += num
    if cnt == 2:
        break;