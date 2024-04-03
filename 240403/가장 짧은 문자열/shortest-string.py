arrStr = []

for _ in range(3):
    arrStr.append(len(input()))

result = max(arrStr) - min(arrStr)
print(result)