unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class sol:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

a = sol(unlock_code, wire_color, seconds)
print(f"code : {a.code}\ncolor : {a.color}\nsecond : {a.sec}")
# Please write your code here.