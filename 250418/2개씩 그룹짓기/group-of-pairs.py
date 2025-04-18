n = int(input())
nums = list(map(int, input().split()))
res = []
# Please write your code here
nums.sort()
rev_nums = sorted(nums, reverse=True)

for n in zip(nums, rev_nums):
    res.append(sum(n))

print(max(res))