import time
import requests
from parser import result


def yar(text: str):
    token = "1778066183:AAGZ11m0RmOx-A9lBCnq1ourrzBqm8N3y38"
    url = "https://api.telegram.org/bot"
    channel_id = ["1093285445", "789730913"]
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })

    if r.status_code != 200:
        raise Exception("post_text error")

def ulya(text: str):
    token = "1778066183:AAGZ11m0RmOx-A9lBCnq1ourrzBqm8N3y38"
    url = "https://api.telegram.org/bot"
    channel_id = "789730913"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })

    if r.status_code != 200:
        raise Exception("post_text error")


def start():
    if __name__ == '__main__':
        yar(result)
        ulya(result)
        time.sleep(3600)
        start()


start()
