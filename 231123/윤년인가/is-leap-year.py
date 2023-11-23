y = int(input())

if y % 4 == 0:
    
    if y % 100 == 0 and y % 400:
        print('true')
    elif y % 100 == 0:
        print('false')
    else:
        print('true')
else:
    print('false')