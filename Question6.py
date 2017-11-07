6.
import api

user_id = 100

users = [api.get_user(user_id) for user_id in range(100, 110)]

print(user_id)


A. UnboundLocalError
B. 100
C. 109
D. None
