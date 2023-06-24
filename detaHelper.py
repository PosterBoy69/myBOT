import json
from aiohttp import ClientSession

apiKey = "d0nth6gssya_SBHxdhEBG2dK7D32zNr9wSxniLqJXnHK"
baseAPI = "https://database.deta.sh/v1/"
projectID = "d0nth6gssya"
baseName = "Posters"
mainApi = f"{baseAPI}{projectID}/{baseName}/"


async def getHeaders() -> dict:
    return {
        'Content-Type': 'application/json',
        'X-API-Key': apiKey,
    }


async def createEntry(basicPayload: dict):

    payload = json.dumps({"items": [basicPayload]})

    createHeaders = await getHeaders()

    async with ClientSession() as sess:
        resp = await sess.put(f'{mainApi}items', data=payload, headers=createHeaders)
        return await resp.json()
