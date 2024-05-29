import requests

base_url = "https://www.aqilas.com/api/v1/"
credits_url = "credit"
sms = "sms"

def get_url(base:str, endpoint:str):
    return base + endpoint if base[-1] == "/" else base + "/" + endpoint


def get_credit(token: str):
    url = get_url(base_url, credits_url)
    headers = {
        "content-type": "application/json",
        "X-AUTH-TOKEN": token,
    }
    return requests.get(url, headers=headers).json()


def send_sms(
    token: str,
    sender: str = "",
    receivers: list = [],
    content: str = ""
):
    url = get_url(base_url, sms)
    headers = {
        "content-type": "application/json",
        "X-AUTH-TOKEN": token,
    }
    data = {"from": sender, "to": receivers, "text": content}
    return requests.post(url, headers=headers, json=data).json()


def get_sms_status(url: str, token: str, bulkid: str):
    url = get_url(base_url, sms+f"/{bulkid}")
    headers = {
        "content-type": "application/json",
        "X-AUTH-TOKEN": token,
    }
    return requests.get(url, headers=headers).json()
