from flask import Flask

from controllers.game_controller import get_game_user_information
from controllers.game_controller import set_game_user_mail
from controllers.game_controller import delete_game_user
from controllers.game_controller import get_ranking

def initialize_game_routes(app: Flask):
    app.add_url_rule('/game/GetGameUserInformation', view_func=get_game_user_information, methods=['GET'])
    app.add_url_rule('/game/SetGameUserMail', view_func=set_game_user_mail, methods=['PATCH'])
    app.add_url_rule('/game/DeleteGameUser', view_func=delete_game_user, methods=['DELETE'])
    app.add_url_rule('/game/GetRanking', view_func=get_ranking, methods=['GET'])

