A = input()


def sol(a):
    if len(set(a)) >= 2:
        return "Yes"
    return "No"


print(sol(A))

