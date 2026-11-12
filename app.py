import json_placeholder

r = json_placeholder.get_users()

print("Status Code:", r[0])

for u in r[1]:
    print(u["name"])
