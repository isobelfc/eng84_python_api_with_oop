import requests

from api_task import Location

# create object
current_location = Location()

current_location.greet_user()
current_location.validate_connection()
current_location.get_nhs_area()
