import requests
from configuration import USERS_URL, KITS_URL

# Token fijo pruebas
AUTH_TOKEN = "48edca05-3479-4d3b-accc-7c4af4729dd2"

def post_new_client_kit(kit_body, auth_token=AUTH_TOKEN):
    headers = {"Authorization": f"Bearer {auth_token}", "Content-Type": "application/json"}
    response = requests.post(KITS_URL, json=kit_body, headers=headers)
    return response