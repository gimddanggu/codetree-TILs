st1 = input()
st2 = input()


def find_st():
    for i in range(len(st1)-len(st2)+1):
        cnt = 0
        for j in range(len(st2)):
            if st1[i+j] == st2[j]:
                cnt += 1
            if cnt == len(st2):
                return i

    return -1
print(find_st())