user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class game:
    def __init__(self, Gid="codetree", level=10):
        self.Gid = Gid
        self.level = level

    
g1 = game()
g2 = game(user2_id, user2_level)

print(f"user {g1.Gid} lv {g1.level}")
print(f"user {g2.Gid} lv {g2.level}")

