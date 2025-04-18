word1 = list(input())
word2 = list(input())

# Please write your code here.
word1.sort()
word2.sort()
def sol():
    if (len(word1) == len(word2)):
        for a, b in zip(word1, word2):
            if a != b:
                return "No"
        return "Yes"
    return "No"
print(sol())