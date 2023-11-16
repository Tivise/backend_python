from flask import Flask, request, jsonify
from routes.steam_routes import initialize_steam_routes
from routes.game_routes import initialize_game_routes
import jwt

from middleware.auth import token_required

app = Flask(__name__)
# JWT - TOKEN
app.config['JWT_SECRET_KEY'] = 'TU VOIS ROMAIN JE FAIS ATTENTION A L\'ENLEVER'
# get_jwt_identity(): recupere l'identite de l'utilisateur (a utiliser dans les middlewares).


# ROUTES
initialize_steam_routes(app)
initialize_game_routes(app)

# Exemple de route nécessitant un jeton JWT
@app.route('/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({'message': 'Protected route!'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', ssl_context=('/etc/letsencrypt/live/rivandy.com-0002/fullchain.pem', '/etc/letsencrypt/live/rivandy.com-0002/privkey.pem'), port=3003)