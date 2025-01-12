from quart import request, jsonify, Blueprint
from api import *
import jwt
from time import time
import httpx
from ..db import *

callback_bp = Blueprint('callback', __name__)
db = db()

PRIVATE_KEY = "your-private-key"
APP_ID = "your-app-id"

async def generate_installation_token(installation_id):
    payload = {
        "iat": int(time()),
        "exp": int(time()) + 600,
        "iss": APP_ID,
    }
    jwt_token = jwt.encode(payload, PRIVATE_KEY, algorithm="RS256")
    url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Accept": "application/vnd.github+json",
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers)
        if response.status_code == 201:
            return response.json().get("token")
        return None

@app.route('/callback/', methods=['GET'])
async def callback():
  installation_id = request.args.get("installation_id")
  state = request.args.get("state")
  if not installation_id: return jsonify({"failed": "bro forgot installation_id"}), 404
  if str(state).isdigit():
    token = await generate_installation_token(installation_id)
    if token:
      await db.add(state, token)
      return jsonify({"okay": "u can talk with your gf now no issues!"}), 200
  return jsonify({"oh": "no use"}), 400
