str_a = input()
str_b = input()

cnt_str = 0
a_length = len(str_a)

for i in range(a_length-1):
    if str_a[i] == str_b[0] and str_a[i+1] == str_b[1]:
        cnt_str += 1
    
print(cnt_str)