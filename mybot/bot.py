from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession
from re import findall
from os import remove

from regexHelper import detect_patterns, removeInvalidChars
from downloadUploadUtils import dwnPoster, upload_image
from detaHelper import createEntry
from mongo import insertIntoMONGO

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION")
FROM_ = config("FROM_CHANNEL")

FROM = [int(i) for i in FROM_.split()]

try:
    User = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    User.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

print("Bot Started !")


@User.on(events.NewMessage(chats=FROM))
async def forward_new_post(event):
    print("New Message Detected !!")
    msg = event.message.message
    links = findall(r'(https?://\S+)', msg)
    if len(links) > 0:
        for link in links:
            msg = msg.replace(link, '')

        msgStatus = detect_patterns(msg)
        if msgStatus:
            msg = removeInvalidChars(msg)
        print(msg)
        msgID = event.message.id

        downloadStatus = dwnPoster(links[0], msgID)
        if downloadStatus:
            uploadedLink = upload_image(msgID)
            if uploadedLink:
                payload = {
                    "messageID": msgID,
                    "name": msg,
                    "telegraph_link": uploadedLink,
                    "other_links": links
                }
                resp = await createEntry(payload)
                print(resp)
                await insertIntoMONGO(resp)
                remove(f"downloads/image{msgID}.jpg")
    else:
        print("No link in new Message !")
        return None


# Run the client until interrupted
User.run_until_disconnected()
