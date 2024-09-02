import requests

class Ready2OrderAPI:
    def __init__(self, account_token):
        self.account_token = account_token
        self.base_url = "https://api.ready2order.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.account_token}"
        }

    def get_company_info(self):
        url = f"{self.base_url}/company"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_invoice(self, data):
        url = f"{self.base_url}/document/invoice"
        response = requests.post(url, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()

    # Add other methods for different API endpoints as needed