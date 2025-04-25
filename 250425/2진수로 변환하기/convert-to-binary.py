n = int(input())
res_lst = []

def binary(n, res_lst):
    mok = n // 2
    na = n % 2

    res_lst.append(na)

    if mok  == 1:

        res_lst.append(1)
        return 0

    
    return binary(mok, res_lst)

binary(n, res_lst)
print(*res_lst[::-1], sep='')
# Please write your code here.