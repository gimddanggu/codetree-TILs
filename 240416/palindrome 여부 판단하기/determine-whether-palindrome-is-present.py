_str = input()


def paindrome_str(_str):
    st = ""
    for i in range(len(_str)-1, -1, -1):
        st += _str[i]
    return st


if paindrome_str(_str) == _str:
    print('Yes')
else:
    print('No')