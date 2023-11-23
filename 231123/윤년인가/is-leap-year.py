y = int(input())

if y % 4 == 0:
    
    if y % 100 == 0:
        print('false')
    elif y % 100 == 0 and y % 400:
        print('true')
    else:
        print('true')
else:
    print('false')