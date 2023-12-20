from sms import get_credit, get_sms_status, send_sms

base_url = "https://www.aqilas.com/api/v1/"
token = "XXXXX"


# To find out how much credit you have left.
print(get_credit(base_url, token))

# To send a message
print(
    send_sms(
        base_url,
        token,
        receivers=["+33XXX", "+226XXX", "+226XXX", "+229XXX"],
        content="send test sms",
    )
)

# To check the status of a message
print(get_sms_status(base_url, token, "SMS BULK ID"))
