n = int(input())

def num_square(n):
    num = 1
    for j in range(n):
        for i in range(n):
            print(num, end =' ')
            num += 1
            if num == 10:
                num = 1 
        print()


num_square(n)