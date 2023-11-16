from flask import jsonify, request
from flask_jwt_extended import jwt_required
import requests

STEAM_WEB_API_KEY = '------------'



##############################################################################
# get_steam_user_information:
#
# Permet d'obtenir les differentes information d'un utilisateur (username, mail, avatar,
# profileURL, etc) lie a son compte Steam.
#
# Parametres: steamID
# Requirements: Authentification token
##############################################################################
@jwt_required()
def get_steam_user_information():
    steamID = request.args.get('steamID')
    if steamID:
        try:
            response = requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={STEAM_WEB_API_KEY}&steamids={steamID}")
            if response.status_code == 200:
                player_data = response.json().get('response', {}).get('players', [])[0]
                return jsonify(player_data), 200
        except requests.RequestException as e:
            return jsonify({'msg': f'Request to Steam API failed: {str(e)}'}), 500

    else:
        return jsonify({'msg': 'Missing steamID'}), 400

def get_steam_user_information_local(steamID):
    if steamID:
        try:
            response = requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={STEAM_WEB_API_KEY}&steamids={steamID}")
            if response.status_code == 200:
                player_data = response.json().get('response', {}).get('players', [])[0]
                return player_data

        except requests.RequestException as e:
            return jsonify({'msg': f'Request to Steam API failed: {str(e)}'}), 500

    else:
        return None
