person1 = tuple(input().split())
person2 = tuple(input().split())
person3 = tuple(input().split())
person, result_arr = [], []
cnt_arr = [0]*5
person.append(person1)
person.append(person2)
person.append(person3)

#person = [tuple(input().split()) for _ in range(2)]
for elem in person:
    if elem[0] == 'Y'and int(elem[1]) >= 37:
        result = 'A'

    elif elem[0] == 'Y'and int(elem[1]) < 37:
        result = 'C'

    elif elem[0] == 'N'and int(elem[1]) >= 37:
        result = 'B' 

    else:
        result = 'D'
    
    result_arr.append(result)


for arr in result_arr:
    if arr == 'A':
        cnt_arr[0] += 1
    elif arr == 'B':
        cnt_arr[1] += 1
    elif arr == 'C':
        cnt_arr[2] += 1
    else:
        cnt_arr[3] += 1

for i in range(4):
    print(cnt_arr[i], end=' ')

if cnt_arr[0] >= 2:
    print('E')