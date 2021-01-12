# -----HTML REQUESTS----- #

# GET - pull from an API
# requests.get(thing I want to get)

# POST - post to an external service like Google Sheets, Twitter, etc
# requests.post()

# PUT - update something in the external service
# requests.put()

# DELETE - delete something in the external service
# delete.put()


import requests
from datetime import datetime

USERNAME = "beazer"
TOKEN = "q03849htqiu4&paq3q4$9"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# Print response as text
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%Y%m%d"))

post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today? "),
}

response = requests.post(url=post_endpoint, json=post_config, headers=headers)
print(response.text)


# UPDATE A POST

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "68",
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)
