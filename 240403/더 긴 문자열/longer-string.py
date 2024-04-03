str1, str2 = input().split()

#result = str1 if len(str1) > len(str2) else 'same' if len(str1) == len(str2) else str2
#print(result, len(result))

if len(str1) == len(str2):
    print('same')

elif len(str1) > len(str2):
    print(str1, len(str1))

else:
    print(str2, len(str2))