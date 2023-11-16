from flask import Flask
from controllers.steam_controller import get_steam_user_information

def initialize_steam_routes(app: Flask):
    app.add_url_rule('/steam/GetSteamUserInformation', view_func=get_steam_user_information, methods=['GET'])

