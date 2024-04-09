alp = input()
asci = ord(alp)

if asci + 1 == ord('z'):
    print('a')
else:
    print(chr(ord(alp)+1))