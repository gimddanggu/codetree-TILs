n = int(input())
x, y = 0, 0

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0] # N S W E

for _ in range(n):
    dire, num = tuple(input().split())
    #print(dire)
    
    if dire == 'N':
        x, y = x, y + dy[0] * int(num)
    elif dire == 'S':
        x, y = x, y + dy[1] * int(num)
    elif dire == 'W':
        x, y = x + dx[2] * int(num), y
    else:
        x, y = x + dx[3] * int(num), y
        
print(x, y)