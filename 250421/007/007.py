secret_code, meeting_point, time = input().split()
time = int(time)

class Agent:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

a = Agent(secret_code, meeting_point, time)
print(f"secret code : {a.secret_code}")
print(f"meeting point : {a.meeting_point}")
print(f"time : {a.time}")
