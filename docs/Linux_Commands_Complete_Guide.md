# 📌 **Kumpulan Perintah Linux Terlengkap & Panduan Penggunaannya**

Dokumen ini berisi daftar perintah Linux yang tersusun secara sistematis berdasarkan kategori, dengan penjelasan detail, contoh penggunaan, dan saran tambahan untuk memaksimalkan penggunaannya.

---

## 📂 **Kategori Perintah Linux**
1. [Perintah Dasar & Navigasi](#1-perintah-dasar--navigasi)
2. [Manajemen File & Direktori](#2-manajemen-file--direktori)
3. [Izin & Hak Akses](#3-izin--hak-akses)
4. [Jaringan & Koneksi](#4-jaringan--koneksi)
5. [Manajemen Proses](#5-manajemen-proses)
6. [Scripting & Automation](#6-scripting--automation)
7. [Administrasi Sistem](#7-administrasi-sistem)
8. [Manajemen Paket](#8-manajemen-paket)
9. [Keamanan & Forensik](#9-keamanan--forensik)
10. [Logging & Monitoring](#10-logging--monitoring)

---

## 1️⃣ **Perintah Dasar & Navigasi**
| Perintah | Fungsi | Contoh Penggunaan | Penjelasan |
|----------|--------|------------------|------------|
| `ls` | Menampilkan daftar file/direktori | `ls -l` | Menampilkan daftar file dengan format panjang |
| `cd` | Berpindah direktori | `cd /home/user` | Berpindah ke direktori `/home/user` |
| `pwd` | Menampilkan direktori aktif | `pwd` | Menunjukkan path absolut dari direktori aktif |

---

## 2️⃣ **Manajemen File & Direktori**
| Perintah | Fungsi | Contoh Penggunaan | Penjelasan |
|----------|--------|------------------|------------|
| `cp` | Menyalin file/direktori | `cp file1.txt file2.txt` | Menyalin `file1.txt` ke `file2.txt` |
| `mv` | Memindahkan/Mengganti nama file | `mv old.txt new.txt` | Mengubah nama `old.txt` menjadi `new.txt` |
| `rm` | Menghapus file/direktori | `rm -r myfolder` | Menghapus `myfolder` secara rekursif |

---

## 3️⃣ **Izin & Hak Akses**
| Perintah | Fungsi | Contoh Penggunaan | Penjelasan |
|----------|--------|------------------|------------|
| `chmod` | Mengubah izin file | `chmod 755 script.sh` | Memberikan izin eksekusi pada `script.sh` |
| `chown` | Mengubah kepemilikan file | `chown user:group file.txt` | Mengubah kepemilikan `file.txt` |
| `umask` | Menetapkan izin default | `umask 022` | File baru akan memiliki izin `755` |

---

## 4️⃣ **Jaringan & Koneksi**
| Perintah | Fungsi | Contoh Penggunaan | Penjelasan |
|----------|--------|------------------|------------|
| `ping` | Mengecek koneksi | `ping google.com` | Mengirim paket ICMP ke `google.com` |
| `netstat` | Menampilkan status jaringan | `netstat -tulnp` | Melihat daftar port yang terbuka |
| `curl` | Mengunduh data | `curl -O http://example.com/file.zip` | Mengunduh file dari URL |

---

## 5️⃣ **Manajemen Proses**
| Perintah | Fungsi | Contoh Penggunaan | Penjelasan |
|----------|--------|------------------|------------|
| `ps` | Menampilkan proses aktif | `ps aux` | Menampilkan semua proses yang berjalan |
| `kill` | Menghentikan proses | `kill 1234` | Menghentikan proses dengan PID 1234 |
| `htop` | Monitoring proses | `htop` | GUI interaktif untuk melihat proses |

---

## 6️⃣ **Scripting & Automation**
| Perintah | Fungsi | Contoh Penggunaan | Penjelasan |
|----------|--------|------------------|------------|
| `bash` | Menjalankan script | `bash script.sh` | Menjalankan `script.sh` |
| `cron` | Menjadwalkan tugas otomatis | `crontab -e` | Mengedit jadwal `cron` |
| `awk` | Pemrosesan teks | `awk '{print $1}' file.txt` | Menampilkan kolom pertama dari file |

---

## 7️⃣ **Administrasi Sistem**
| Perintah | Fungsi | Contoh Penggunaan | Penjelasan |
|----------|--------|------------------|------------|
| `systemctl` | Mengelola layanan | `systemctl restart apache2` | Memulai ulang layanan `apache2` |
| `uptime` | Waktu aktif sistem | `uptime` | Menunjukkan lama sistem berjalan |
| `df` | Melihat penggunaan disk | `df -h` | Menampilkan info penggunaan disk |

---

## 8️⃣ **Manajemen Paket**
| Perintah | Fungsi | Contoh Penggunaan | Penjelasan |
|----------|--------|------------------|------------|
| `apt` | Mengelola paket Debian | `sudo apt install nano` | Menginstal `nano` |
| `yum` | Mengelola paket RHEL | `sudo yum update` | Memperbarui semua paket |
| `pacman` | Mengelola paket Arch | `sudo pacman -S firefox` | Menginstal `firefox` |

---

## 9️⃣ **Keamanan & Forensik**
| Perintah | Fungsi | Contoh Penggunaan | Penjelasan |
|----------|--------|------------------|------------|
| `iptables` | Mengatur firewall | `sudo iptables -L` | Menampilkan aturan firewall |
| `fail2ban` | Mencegah brute force | `sudo fail2ban-client status` | Menampilkan status fail2ban |
| `chkrootkit` | Deteksi rootkit | `sudo chkrootkit` | Memeriksa rootkit dalam sistem |

---

## 🔟 **Logging & Monitoring**
| Perintah | Fungsi | Contoh Penggunaan | Penjelasan |
|----------|--------|------------------|------------|
| `dmesg` | Log kernel | `dmesg | tail -20` | Menampilkan 20 log kernel terakhir |
| `journalctl` | Log sistem | `journalctl -u nginx.service` | Log untuk layanan `nginx` |
| `vmstat` | Monitoring sistem | `vmstat 1 10` | Statistik sistem setiap 1 detik selama 10 kali |

---

> **Dokumen ini telah disusun sekomprehensif mungkin! Jika ada tambahan atau perbaikan, silakan beri tahu saya! 🚀**

