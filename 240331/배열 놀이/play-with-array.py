n, qNum = tuple(map(int, input().split()))
n_list = list(map(int, input().split()))

for _ in range(qNum):
    q = list(map(int, input().split()))

    if q[0] == 1:
        print(n_list[q[1]-1])

    elif q[0] == 2:
        if q[1] in n_list:
            print(n_list.index(q[1])+1)
        else:
            print(0)

    else:
        for i in range(q[1], q[2]+1):
            print(n_list[i-1], end = ' ')