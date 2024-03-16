arr_sum = 0 
arr_ev = 0
arrange = [4, 10, 37, 53, 88, 260, 67, 88, 500, 400]
flag = 0

for a in arrange:
    if a >= 250:
        break;
    flag += 1


for a in arrange[:flag]:
    arr_sum += a
    arr_ev = arr_sum / flag



print(arr_sum, arr_ev)