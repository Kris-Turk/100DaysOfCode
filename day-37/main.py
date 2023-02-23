import requests

pixela_endpoint = "https://pixe.la/v1/users/"

user_parameters = {
    "token": "Wsdnfowapoi32423sd777lfmnve",
    "username": "swip",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# user = requests.post(url=pixela_endpoint, json=user_parameters)
# print(user)

# Replace these with your own Pixela user ID and token
user_id = "your-user-id"
token = "your-token"

# Set the details of your new graph
graph_name = "Coding Habit Tracker"
graph_id = "coding-habit"
unit = "days"
type = "int"
color = "shibafu"

# Make a POST request to create the graph
url = f"https://pixe.la/v1/users/{user_id}/graphs"
headers = {"Authorization": f"Bearer {token}"}
data = {
    "name": graph_name,
    "id": graph_id,
    "unit": unit,
    "type": type,
    "color": color
}
response = requests.post(url, headers=headers, json=data)

# Check the status code of the response to make sure the request was successful
if response.status_code == 201:
    print("Successfully created graph")
else:
    print("Failed to create graph")

# Set the value for the current day
date = "2022-01-01"  # Replace this with the current date
quantity = "1"  # Replace this with the number of days you coded

# Make a PUT request to record the
