a, b = tuple(map(int, input().split()))


def least_common_multiple(num1, num2):
    lcm = 0
    for i in range(num1 * num2, max(num1, num2)-1, -1):
        #print(i)
        if i % num1 == 0 and i % num2 == 0:
            lcm = i

    print(lcm)


least_common_multiple(a, b)