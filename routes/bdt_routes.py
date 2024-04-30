from flask import Flask

from controllers.bdt_controller import get_games

def initialize_bdt_routes(app: Flask):
    app.add_url_rule('/bdt/GetGames', view_func=get_games, methods=['GET'])

