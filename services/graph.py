import requests
import os

TOKEN_URL = "https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
GRAPH_URL = "https://graph.microsoft.com/v1.0"


def get_access_token():
    tenant = os.getenv("TENANT_ID")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    url = TOKEN_URL.format(tenant=tenant)

    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "https://graph.microsoft.com/.default",
        "grant_type": "client_credentials"
    }

    response = requests.post(url, data=data)
    return response.json().get("access_token")


def list_files(folder_path):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}

    url = f"{GRAPH_URL}/me/drive/root:{folder_path}:/children"
    response = requests.get(url, headers=headers)

    return response.json().get("value", [])


def get_file_content(file_id):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}

    url = f"{GRAPH_URL}/me/drive/items/{file_id}/content"
    response = requests.get(url, headers=headers)

    return response.text
