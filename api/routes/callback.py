from quart import request, jsonify, Blueprint
from api import *
import httpx
from ..db.db import *

callback_bp = Blueprint('callback', __name__)
db = db()

@app.route('/callback/', methods=['GET'])
async def callback():
  installation_id = request.args.get("installation_id")
  state = request.args.get("state")
  if not installation_id: return jsonify({"failed": "bro forgot installation_id"}), 404
  if str(state).isdigit():
    await db.add(state, installation_id)
    return jsonify({"okay": "u can talk with your gf now no issues!"}), 200
  return jsonify({"oh": "no use"}), 400
