import socket

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    s.close()
    return result == 0

target_ip = input("Masukkan IP target: ")
ports = [21, 22, 23, 25, 53, 80, 443, 3306, 3389]  # Beberapa port umum

print(f"Scanning {target_ip}...")
for port in ports:
    if scan_port(target_ip, port):
        print(f"[+] Port {port} terbuka")
    else:
        print(f"[-] Port {port} tertutup")

