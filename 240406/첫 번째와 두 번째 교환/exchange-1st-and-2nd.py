strr = input()
str_1st = strr[0]
str_2nd = strr[1]

strr_list = list(strr)
str_length = len(strr_list)

for i in range(len(strr)):
    if strr_list[i] == str_1st:
        strr_list[i] = str_2nd
    
    elif strr_list[i] == str_2nd:
        strr_list[i] = str_1st

print(''.join(strr_list))