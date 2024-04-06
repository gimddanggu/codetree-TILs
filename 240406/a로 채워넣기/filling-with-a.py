# slicing 이용하여 새로운 문자열 생성
# list() 함수로 감싼 후 변경 -> .join 이용하여 다시 문자열로 변경

strr = input()
str_a = strr[0] + 'a' + strr[2:-2] + 'a' + strr[-1]
print(str_a)