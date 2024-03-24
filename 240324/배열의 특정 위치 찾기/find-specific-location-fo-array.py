arr = list(map(int, input().split()))

even_list = arr[1::2]
third_list = arr[2::3]

print(sum(even_list), round(sum(third_list)/len(third_list), 1))