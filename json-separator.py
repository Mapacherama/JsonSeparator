import json

with open('mock-userdata.json', 'r') as f:
    data = json.load(f)

user_info = {}

for user in data:
    user_id = user['id']
    if user_id not in user_info:
        user_info[user_id] = []
    user_info[user_id].append(user)

# Print the information for each user
for user_id, user_data in user_info.items():
    print(f"User {user_id}: {user_data}")