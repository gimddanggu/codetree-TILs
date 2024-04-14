a, b = tuple(map(int, input().split()))
cnt = 0


def num_in_tsn(n):
    n = str(n)
    return '3' in n or '6' in n or '9' in n
    
def three_multiple(n):
    return n % 3 == 0

def game_369(n):
    global cnt
    if num_in_tsn(n) or three_multiple(n):
        cnt += 1



for i in range(a, b+1):
    game_369(i) #369 조건 맞으면 카운팅


print(cnt)