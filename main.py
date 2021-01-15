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
from flask import Flask, render_template, request

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

# Website link
app = Flask(__name__)



@app.route('/', methods=["GET", "POST"])
def home():
    global pixela_endpoint
    global USERNAME
    global GRAPH_ID
    post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    today = datetime.now()

    if request.method == "POST":
        start_time = request.form['start']
        end_time = request.form['end']
        fmt = '%H:%M'
        time_delta = datetime.strptime(end_time, fmt) - datetime.strptime(start_time, fmt)
        total_seconds = time_delta.total_seconds()
        duration = total_seconds / 60
        int_duration = int(duration)
        print(int_duration)

        # Post to Pixela
        post_config = {
            "date": today.strftime("%Y%m%d"),
            "quantity": f"{int_duration}",
        }
        response = requests.post(url=post_endpoint, json=post_config, headers=headers)
        print(response.text)
        return render_template("index.html", duration=duration)
    return render_template("index.html")


# UPDATE A POST
today = datetime.now()

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "68",
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

if __name__ == "__main__":
    app.run(debug=True)
