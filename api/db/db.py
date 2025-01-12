from api import DATABASE
import logging

cb = DATABASE['cb']

class db:
  async def add(self, user_id, token, installation_id):
    db = cb
    user_id = int(user_id)
    user = await db.find_one({"_id": user_id})
    if not user:
      await db.update_one({"_id": 1}, {"$addToSet": {"users": user_id}}, upsert=True)
    await db.update_one(
      {"_id": user_id},
      {"$set": {"token": token, "installation_id": installation_id}},
      upsert=True
    )
