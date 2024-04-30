from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.steam_routes import initialize_steam_routes
from routes.game_routes import initialize_game_routes
from routes.bdt_routes import initialize_bdt_routes
import jwt
import os

from middleware.auth import token_required

app = Flask(__name__)
CORS(app)
# JWT - TOKEN
# get_jwt_identity(): recupere l'identite de l'utilisateur (a utiliser dans les middlewares).


# ROUTES
initialize_steam_routes(app)
initialize_game_routes(app)
initialize_bdt_routes(app)

# Exemple de route nécessitant un jeton JWT
@app.route('/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({'message': 'Protected route!'})

app.debug = False

host = '0.0.0.0'
port = 3003
cert_path = '/etc/letsencrypt/live/rivandy.com-0002/fullchain.pem'
key_path = '/etc/letsencrypt/live/rivandy.com-0002/privkey.pem'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', ssl_context=('/etc/letsencrypt/live/rivandy.com-0002/fullchain.pem', '/etc/letsencrypt/live/rivandy.com-0002/privkey.pem'), port=3003)
