import requests
from app.config import COUNTRY_API_HOST

class CountryAPIClient:

    def __init__(self, fields: list = None):
            self.fields = fields

    def fetch_country_data(self):
        if self.fields:
            fields_param = ",".join(self.fields)
            response = requests.get(f"{COUNTRY_API_HOST}?fields={fields_param}")
        else:
            response = requests.get(f"{COUNTRY_API_HOST}")
        response.raise_for_status()
        return response.json()
