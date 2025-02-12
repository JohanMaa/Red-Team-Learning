#!/bin/bash

echo "Masukkan IP target atau range (contoh: 192.168.1.1/24): "
read target

echo "Scanning dengan Nmap..."
nmap -sS -Pn -T4 -p 1-1000 $target -oN hasil_scan.txt

echo "Scan selesai. Hasil disimpan di hasil_scan.txt"

