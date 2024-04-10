cnt = 0
st_list = []
while(True):
    strr = input()
    if strr.isdigit():
        break;
    cnt += 1
    if cnt % 2 != 0:
        st_list.append(strr)
    

print(cnt)
for i in st_list:
    print(i)