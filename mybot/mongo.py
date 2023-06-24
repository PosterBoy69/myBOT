from pymongo import MongoClient
import json

client = MongoClient('mongodb+srv://posterboys:posterboys@cluster0.vfyxllj.mongodb.net/?retryWrites=true&w=majority')
db = client["wzmlXPosters"]
collection = db["Posters"]


async def insertIntoMONGO(jsonResp: json):
    itemList = jsonResp['processed']['items']
    post = collection.insert_one(itemList[0])
    print(post.inserted_id)
