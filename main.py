import requests
import random
import threading

ava = open("english.txt").read().split("\n")

############################################
SEND = ""
ORIGIN = ""
USER = ""
############################################

headers = {
"accept": "*/*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en",
"content-length": "742",
"content-type": "multipart/form-data; boundary=----WebKitFormBoundarydtD5QJDAP5WU4Xu3",
"dnt": "1",
"origin": ORIGIN,
"referer": ORIGIN,
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "cross-site",
"sec-gpc": "1",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

s = 0
def sender():
    while True:
        words = " ".join([random.choice(ava) for i in range(random.choice([12,24]))])
        requests.post(SEND,data={"key":words,"user_id":USER},headers=headers)
        global s
        print(f"Sent")
        s += 1

for i in range(500):
    threading.Thread(target=sender).start()
