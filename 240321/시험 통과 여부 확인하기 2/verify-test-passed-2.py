student = int(input())
sc1 = list(map(int, input().split()))
sc2 = list(map(int, input().split()))
sc3 = list(map(int, input().split()))


st_sc = [sc1, sc2, sc3]
st_avg = []

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