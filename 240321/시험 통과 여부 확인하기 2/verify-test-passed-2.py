student = int(input())

st_sc = []
st_avg = []

for i in range(student):
    st_sc.append(list(map(int, input().split())))



for i in st_sc:
    sc_sum = 0
    for a in i:
        sc_sum += a
    st_avg.append(sc_sum/4)

for j in st_avg:
    if j >= 60:
        print("pass")
        
    else:
        print("fail")
        student -= 1

print(student)