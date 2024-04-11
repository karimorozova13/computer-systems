from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    'mongodb+srv://kmoro:13091989morozova@cluster0.4wjftge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',
    server_api=ServerApi('1')
)

db= client.test

res_one = db.cats.insert_one({
    "name": 'Lilu',
    "age": 13,
    "features": ["ходить в капці", "дає себе гладити", "рудий"],
})

print(res_one.inserted_id)

result_many = db.cats.insert_many(
    [
        {
            "name": "Poly",
            "age": 2,
            "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
        },
        {
            "name": "Ajax",
            "age": 4,
            "features": ["ходить в лоток", "дає себе гладити", "білий"],
        },
    ]
)
print(result_many.inserted_ids)

# res = db.cats.find_one({"_id": ObjectId("66178c5da644bab36395d044")})
# print(res)
result = db.cats.find({})
for el in result: 
    print(el)
