str1, str2 = input().split()

result = str1 if len(str1) > len(str2) else same if str1 == str2 else str2
print(result, len(result))