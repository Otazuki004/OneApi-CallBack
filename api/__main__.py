import os
from api import app
from quart_cors import cors
import asyncio
from quart import request, jsonify, Blueprint

app = cors(app, allow_origin="*")

from .routes.callback import callback_bp

app.register_blueprint(callback)
@app.route('/')
def home():
    return jsonify({'success': 'server online'})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
