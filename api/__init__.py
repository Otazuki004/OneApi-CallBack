from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import logging
import os
from quart import Quart
from quart_cors import cors


logging.basicConfig(
    format="[API] %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)


# VARIABLES
MONGO_DB_URL = "mongodb+srv://knight_rider:GODGURU12345@knight.jm59gu9.mongodb.net/?retryWrites=true&w=majority"

DATABASE = AsyncIOMotorClient(MONGO_DB_URL)["OneApi"]
app = Quart(__name__)
