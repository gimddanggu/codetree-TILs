"""arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr[i] //= 2
    else:
        arr[i] += 3

for ar in arr:
    if ar == 0:
        break;
    print(ar, end=' ')
"""

# 배열에 주어진 수를 입력받아 저장합니다.
arr = list(map(int, input().split()))
new_arr = []

# 입력받은 정수로부터 출력할 값을 새로운 배열에 저장하고, 0이 나오면 for문을 탈출
for i in range(100):
	if arr[i] == 0:
		break
	if arr[i] % 2 == 0:
		new_arr.append(arr[i] // 2)
	else:
		new_arr.append(arr[i] + 3)

# 0이 나오기 전까지의 배열의 인덱스에 저장된 값을 출력
for elem in new_arr:
	print(elem, end=" ")