# 질의 1 a번째 문자와 b 번째 문자를 교환한 뒤 출력
# 질의 2 문자 a를 전부 문자 b로 변경한 뒤 출력

strr, n = tuple(input().split())
strr_a = ''
for i in range(int(n)):
    q, n1, n2 = tuple(input().split())

    if q == '1':
        n1 = int(n1)-1
        n2 = int(n2)-1
        a = strr[n1]
        b = strr[n2]
        for i in range(len(strr)):    
            strr_a = strr[:n1] + b + strr[n1+1: n2] + a + strr[n2+1:]
        print(strr_a) 
    else:
        '''
        for i in range(len(strr)):
            if n1 == strr[i]:
                strr_a = strr[:i] + n2 + strr[i+1:]
                print(strr_a)
        print(strr_a, 2)
        '''
        strr_a = strr.replace(n1, n2)
        print(strr_a)