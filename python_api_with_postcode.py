# API for postcode.io

import requests

url = "http://api.postcodes.io/postcodes/"
postcode = "e147le"

url_arg = url + postcode
print(url_arg)

response = requests.get(url_arg)

# good to check status code before doing anything else
print(response.status_code)

# # check some misc. associated information
# print(response.content)
# print(response.headers)
# print(response.encoding.isdigit())
# print(response.headers.keys())
# print(response.is_redirect)

response_dict = response.json()  # json() helps us convert to dictionary
# print(type(response_dict))

print(response_dict)

response_result = response_dict["result"]

for keys in response_result.keys():
    if keys == "postcode":
        print("Your postcode location is " + str(response_result["postcode"]))

    if keys == "longitude":
        print(f"Your longitude is {response_result['longitude']}")
    elif keys == "latitude":
        print(f"Your latitude is {response_result['latitude']}")
