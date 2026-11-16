import requests


def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    try:
        # gestisco gli errori
        if response.status_code == 200:
            data_users = response.json()

            # print(type(data_users[0]))
            # print(data_users[0])

            return response.status_code, data_users
        else:
            return response.status_code, []

    except Exception as e:
        print(e)
        return response.status_code, []

    # print("FINITO")
