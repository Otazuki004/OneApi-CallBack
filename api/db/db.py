from api import DATABASE
import logging

cb = DATABASE['cb']

class db:
  async def add(self, user_id, token):
    db = cb
    user_id = int(user_id)
    user = await db.find_one({"_id": user_id})
    if user: return
    await db.update_one({"_id": 1}, {"$addToSet": {"users": user_id}}, upsert=True)
    await db.update_one(
      {"_id": user_id},
      {"$set": {"token": token}},
      upsert=True
    )
