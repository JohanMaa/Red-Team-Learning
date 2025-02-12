import requests

target = "example.com"
subdomains = ["admin", "mail", "test", "dev"]

for sub in subdomains:
    url = f"http://{sub}.{target}"
    try:
        response = requests.get(url)
        print(f"[+] Subdomain ditemukan: {url}")
    except requests.ConnectionError:
        pass

