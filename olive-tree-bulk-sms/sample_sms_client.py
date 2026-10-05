import requests

url = "https://example-sms-provider.com/api/messages"

payload = {
    "recipient": "254700000000",
    "message": "Sample customer notification",
    "sender_id": "COMPANY"
}

response = requests.post(url, json=payload, timeout=30)

print("Status Code:", response.status_code)
print("Response:", response.text)
