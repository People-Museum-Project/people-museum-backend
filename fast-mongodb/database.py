from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb+srv://alusi:alusi@cluster0.3nizdcf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["your_database_name"]
person_collection = db["person"]
people_collection = db["people_collection"]
user_collection = db["user"]
comments_collection = db["comments"]
