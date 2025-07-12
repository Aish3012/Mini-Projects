from motor.motor_asyncio import AsyncIOMotorClient
import os   
from dotenv import load_dotenv
load_dotenv()

print("connecting to MongoDB")
print(os.getenv("mongoUrl"))
client = AsyncIOMotorClient(os.getenv('mongoUrl'))
#client=AsyncIOMotorClient("mongodb+srv://aish:aish3012@cluster0.soi2vbt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db=client["MyProduct"]
collection = db["Products"]
isDelete=False 
       

