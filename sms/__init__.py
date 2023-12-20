import requests

credits_url = "credit"
sms = "sms"


def get_credit(url: str, token: str):
    v = url + credits_url if url[-1] == "/" else url + "/" + credits_url
    headers = {
        "content-type": "application/json",
        "X-AUTH-TOKEN": token,
    }
    return requests.get(v, headers=headers).json()


def send_sms(
    url: str,
    token: str,
    sender: str = "ETIMBRE",
    receivers: list = [],
    content: str = "",
):
    v = url + sms if url[-1] == "/" else url + "/" + sms
    headers = {
        "content-type": "application/json",
        "X-AUTH-TOKEN": token,
    }
    data = {"from": sender, "to": receivers, "text": content}
    return requests.post(v, headers=headers, json=data).json()


def get_sms_status(url: str, token: str, bulkid: str):
    v = url + sms if url[-1] == "/" else url + "/" + sms
    v = v + "/" + bulkid
    headers = {
        "content-type": "application/json",
        "X-AUTH-TOKEN": token,
    }
    return requests.get(v, headers=headers).json()
