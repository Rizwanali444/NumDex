"""
NumDex — numinfo1.py
Repository: Rizwanali444/NumDex
Commit: f1a4480f8de36f80a01b6022f0d10dd21344a36e

Author / Coder Details (START — DO NOT REMOVE)
------------------------------------------------
Author  : Rizwan Ali
Handle  : Rizwanali444 (GitHub)
Nick    : ShadowX
Country : Pakistan 🇵🇰
Contact : github.com/Rizwanali444
About   : Developer of NumDex — Mobile & CNIC Lookup tool
Date    : 2025-12-05

Important note for users:
If you use, modify, fork, or redistribute this file or code derived from it,
please keep the Author / Coder Details block intact and give clear credit to:
Rizwan Ali (Rizwanali444) — https://github.com/Rizwanali444

.
------------------------------------------------
"""

import requests
from bs4 import BeautifulSoup
import time
import os
import platform
import random
import json
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def type_print(text, delay=0.004, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def rainbow_print(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for i, char in enumerate(text):
        print(colors[i % len(colors)] + char, end='', flush=True)
        time.sleep(0.002)
    print(Style.RESET_ALL)

def gradient_line():
    rainbow_print("━" * 50)

def show_user_info():
    proc = platform.processor() or "Unknown"
    try:
        import socket, urllib.request
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        public_ip = urllib.request.urlopen("https://api.ipify.org").read().decode().strip()
    except:
        local_ip = "Unknown"
        public_ip = "Unknown"
    try:
        brand = os.popen("getprop ro.product.brand").read().strip()
        model = os.popen("getprop ro.product.model").read().strip()
    except:
        brand = model = "Unknown"
    try:
        battery_output = os.popen("termux-battery-status").read()
        battery_data = json.loads(battery_output)
        battery = f"{battery_data['percentage']}% ({battery_data['status']})"
    except:
        battery = "Unknown"

    info_lines = [
        (Fore.GREEN, "📱 Device Information"),
        (Fore.BLUE, "━" * 45),
        (Fore.RED, f"📱 Device     : {brand} {model}"),
        (Fore.GREEN, f"🔋 Battery    : {battery}"),
        (Fore.BLUE, f"🌐 Local IP   : {local_ip}"),
        (Fore.RED, f"🌍 Public IP  : {public_ip}"),
        (Fore.GREEN, f"💻 OS         : {platform.system()}"),
        (Fore.BLUE, f"📟 Machine    : {platform.machine()}"),
        (Fore.RED, f"🔧 CPU        : {proc}"),
        (Fore.GREEN, f"⏰ Time       : {time.strftime('%H:%M:%S')}"),
        (Fore.BLUE, f"📅 Date       : {time.strftime('%d-%m-%Y')}"),
        (Fore.RED, "━" * 45)
    ]
    for color, line in info_lines:
        type_print(line, delay=0.01, color=color)

def loading_dots(msg="🔍 Searching"):
    for i in range(3):
        print(Fore.YELLOW + msg + '.' * (i + 1), end='\r', flush=True)
        time.sleep(0.5)
    print(Style.RESET_ALL)

def save_to_file(data):
    with open("results.txt", "a", encoding="utf-8") as f:
        f.write(data + "\n")

def logo():
    type_print("███    ██ ██    ██ ███    ███ ██████  ███████ ██   ██", color=Fore.GREEN)
    type_print("████   ██ ██    ██ ████  ████ ██   ██ ██       ██ ██", color=Fore.BLUE)
    type_print("██ ██  ██ ██    ██ ██ ████ ██ ██   ██ █████     ███", color=Fore.RED)
    type_print("██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██       ██ ██", color=Fore.GREEN)
    type_print("██   ████  ██████  ██      ██ ██████  ███████ ██   ██", color=Fore.BLUE)
    type_print("🔥 INFO TOOL v1.0 (Developed by RIZWAN ALI) 🔥", color=Fore.RED)

    details = [
        (Fore.GREEN, "👑 Owner Details"),
        (Fore.BLUE, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"),
        (Fore.RED, "🧑 Name         : Rizwan Ali"),
        (Fore.GREEN, "📛 Nickname     : ShadowX"),
        (Fore.BLUE, "🌐 Country      : Pakistan 🇵🇰"),
        (Fore.RED, "🤝 Best Friend  : Isaan Turak ,Itz Chuza 🐣"),
        (Fore.GREEN, "🔗 GitHub       : github.com/Rizwanali444"),
        (Fore.BLUE, "🛠 Tool Details"),
        (Fore.RED, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"),
        (Fore.GREEN, "📌 Tool Name      : NumDex"),
        (Fore.BLUE, "🎯 Purpose        : Mobile & CNIC Lookup"),
        (Fore.RED, "🧠 Built With     : Python, BeautifulSoup"),
        (Fore.GREEN, "🔒 Security       : No API Used — Fast & Safe"),
        (Fore.BLUE, "📂 Log Output     : results.txt"),
        (Fore.RED, "🧪 Version        : v0.1 (Beta)"),
        (Fore.GREEN, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    ]
    for color, line in details:
        type_print(line, delay=0.001, color=color)

def numinfo(mobile_number):
    try:
        session = requests.Session()

        headers = {
            'authority': 'freshsimownerdetails.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://freshsimownerdetails.com',
            'referer': 'https://freshsimownerdetails.com/SimDetails.php',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            
        }

        data = {
            'number': mobile_number.strip(),
            'search': ''
        }

        response = session.post(
            "https://freshsimownerdetails.com/SecureInfo.php",
            headers=headers,
            data=data
        )

        soup = BeautifulSoup(response.text, 'html.parser')

        rows = soup.find_all("tr")
        if len(rows) <= 1:
            type_print(f"[❌] Koi data nahi mila for: {mobile_number}", color=Fore.LIGHTRED_EX)
            return

        for tr in rows[1:]:
            tds = tr.find_all("td")
            if len(tds) >= 4:
                number = tds[0].text.strip()
                name = tds[1].text.strip()
                cnic = tds[2].text.strip()
                address = tds[3].text.strip()

                type_print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", color=Fore.MAGENTA)
                type_print(f"[+] 📞 Number  : {number}", color=Fore.GREEN)
                type_print(f"[+] 🧑 Name    : {name}", color=Fore.BLUE)
                type_print(f"[+] 🆔 CNIC    : {cnic}", color=Fore.RED)
                type_print(f"[+] 🏠 Address : {address}", color=Fore.GREEN)
                type_print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", color=Fore.MAGENTA)

                save_to_file(f"{number} | {name} | {cnic} | {address}")

    except Exception as e:
        type_print(f"[!] Error for {mobile_number}: {e}", color=Fore.RED)
def main():
    clear_screen()
    logo()
    show_user_info()
    gradient_line()

    while True:
        answer = input(f"\n{Fore.LIGHTBLUE_EX}[❓] Kya aap data search karna chahte hain? (yes/no): {Style.RESET_ALL}").strip().lower()
        if answer == 'no':
            type_print("\n👋 Shukriya! INFO TOOL Band kar diya gaya hai.\n", color=Fore.MAGENTA)
            break
        elif answer == 'yes':
            mobile = input(f"{Fore.LIGHTCYAN_EX}[📲] Enter Mobile/CNIC: {Style.RESET_ALL}").strip()
            if mobile:
                loading_dots("🔍 Searching")
                type_print(f"\n[✔] Result for: {mobile}\n", color=Fore.YELLOW)
                numinfo(mobile)
            else:
                type_print("[⚠] Galat input! Number ya CNIC daalein.", color=Fore.LIGHTRED_EX)
        else:
            type_print("[⚠] Sirf 'yes' ya 'no' enter karein.", color=Fore.LIGHTRED_EX)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------
# License & Credits (END — DO NOT REMOVE)
# ----------------------------------------------------------------------
# Copyright (c) 2025 Rizwan Ali (Rizwanali444)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# use, copy, modify, merge, publish, distribute, and/or sublicense copies of
# the Software, subject to the following condition:
#
# Attribution Requirement:
# If you redistribute the Software, in source or binary form, or any
# derivative work, you MUST include the original Author / Coder Details block
# at the top of this file (or an equivalent prominent attribution in
# documentation or about pages) that names: Rizwan Ali (Rizwanali444)
# and links to: https://github.com/Rizwanali444/NumDex
#
# DISCLAIMER:
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY.
#
# Recommended credit line:
# "NumDex — Mobile & CNIC Lookup by Rizwan Ali (Rizwanali444) — https://github.com/Rizwanali444/NumDex"
#
# ----------------------------------------------------------------------

