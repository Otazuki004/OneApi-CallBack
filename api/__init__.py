from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import logging
from variables import *
import os
from quart import Quart
from quart_cors import cors


logging.basicConfig(
    format="[API] %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)


# VARIABLES
MONGO_DB_URL = os.environ.get("MONGO_DB_URL") or VAR_MONGO_DB_URL

DATABASE = AsyncIOMotorClient(MONGO_DB_URL)["CallbackApi"]
app = Quart(__name__)
