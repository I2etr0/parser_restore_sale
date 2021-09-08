import time
import requests
from parser import result


def first(text: str):
    token = "BOT_token"
    url = "https://api.telegram.org/bot"
    channel_id = "chat_id"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })

    if r.status_code != 200:
        raise Exception("post_text error")

# Send message for second person
# def second(text: str):
#     token = "BOT_token"
#     url = "https://api.telegram.org/bot"
#     channel_id = "chat_id"
#     url += token
#     method = url + "/sendMessage"

#     r = requests.post(method, data={
#         "chat_id": channel_id,
#         "text": text
#     })

#     if r.status_code != 200:
#         raise Exception("post_text error")


def start():
    if __name__ == '__main__':
        first(result)
        second(result)
        time.sleep(3600)
        start()


start()
