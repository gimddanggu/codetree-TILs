str1 = input()
str2 = input()

for i in range(len(str1)):
    str1 = str1[1:] + str1[0]
    if str1 == str2:
        print(i+1)
        break;
        
if str1 != str2:
    print(-1)