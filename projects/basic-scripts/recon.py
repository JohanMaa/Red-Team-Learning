import requests

url = "http://example.com"
response = requests.get(url)

print(f"Status Code: {response.status_code}")
print("Headers:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

