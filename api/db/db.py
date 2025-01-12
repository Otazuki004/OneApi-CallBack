from api import DATABASE
import logging

cb = DATABASE['cb']

class db:
  async def add(self, user_id: int, token):
    db = cb
    user = await db.find_one({"_id": user_id})
    if user: return
    await db.update_one({"_id": 1}, {"$addToSet": {"users": user_id}}, upsert=True)
    await db.update_one(
      {"_id": user_id},
      {"$set": {"token": token}},
      upsert=True
    )
