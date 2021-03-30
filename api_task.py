import requests

class Location():
    def __init__(self):
        self.url = "http://api.postcodes.io/postcodes/"  # base url to append postcode onto
        self.name = input("Please enter your name: ")
        self.postcode = input("Please enter your postcode:  ")
        self.url_arg = self.url + self.postcode  # complete url to request
        self.response = requests.get(self.url_arg)  # request the url
        self.response_dict = self.response.json()  # turns to dictionary format
        self.response_result = self.response_dict["result"]

    def greet_user(self):
        print(f"Welcome, {self.name}!")

    def validate_connection(self):
        if self.response.status_code == 200:
            print(f"Connected! status code: {self.response.status_code}")
        else:
            print(f"Failed to connect. status code: {self.response.status_code}")

    def get_nhs_area(self):
        for keys in self.response_result:
            if keys == "nhs_ha":
                print("Your NHS area is " + str(self.response_result["nhs_ha"]))

