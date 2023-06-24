import requests
from telegraph.upload import TelegraphApi
import os


telegraph = TelegraphApi(access_token='779370a118d081b27c38371717a6fdad927c2f0de4e12d13f4b2fb928e8f',
                         domain='graph.org')


def dwnPoster(link: str, msgID: int):
    try:
        response = requests.get(link, stream=True)
        with open(f"downloads/image{msgID}.jpg", "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
            return True
    except Exception as e:
        args = e.args
        print(args)
        return False


def upload_image(msgId: int):
    try:
        if os.path.exists(f"downloads/image{msgId}.jpg"):
            resp = telegraph.upload_file(f=f"downloads/image{msgId}.jpg")
            return f"https://telegra.ph{resp[0].get('src')}"
        else:
            return False
    except Exception as e:
        args = e.args
        print(args)
        return False
