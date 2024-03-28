num = int(input())
arr = []

result = num
cnt = 0

"""
while(True):
    if result % 5 == 0:
        cnt += 1
    print(result, end=' ')
    result += num
    if cnt == 2:
        break;

if result % num == 0:
    arr.append(result)
if result == num * 10:
    break;
"""

while(True):
    arr.append(result)
    if result % 5 == 0:
        cnt += 1
    result += num

    if cnt == 2:
        break;
    
for n in range(len(arr)):
    print(arr[n], end=' ')