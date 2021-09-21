import requests
import datetime as dt

USERNAME = "aaqil"
TOKEN = "fhehwehsdbjejws"
GRAPH_ID = "graph1"


# creating user
pixela_endpoint = "https://pixe.la/v1/users"
create_user_parameters = {
    "token": TOKEN,  # can be anything but has to be more than 8 characters
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=create_user_parameters)
# print(response.text)


# creating graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = dt.datetime.now()

#  adding pixel to graph
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometres did you cycle today? ")
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# # updating value of pixel in graph
# pixel_update_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
# pixel_update_config = {
#     "quantity": "15.5"
# }

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)

# # deleting a pixel from the graph
# response = requests.delete(url=pixel_update_endpoint, headers=headers)
# print(response.text)
