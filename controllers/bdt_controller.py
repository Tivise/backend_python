from flask import jsonify, request
from middleware.db import get_mysql_connection
from controllers.steam_controller import get_steam_user_information_local
from middleware.auth import token_required
import requests

##############################################################################
# Get_Games:
#
# Permet d'obtenir les jeux en fonction de leurs critères.
#
##############################################################################
def get_games():
    gameId = request.args.get('gameId')
    supportId = request.args.get('supportId')
    typeId = request.args.get('typeId')
    modeId = request.args.get('modeId')
    soloId = request.args.get('soloId')
    
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor(dictionary=True)

        # Construction de la requête SQL en fonction des paramètres
        query = 'SELECT * FROM BDT_Jeux '
        if soloId or supportId or typeId or modeId:
            query += 'JOIN BDT_Assoc ON BDT_Jeux.id = BDT_Assoc.id ' \
                     'JOIN BDT_Type ON BDT_Assoc.tid = BDT_Type.tid '
        conditions = []
        if gameId:
            conditions.append(f"BDT_Jeux.id = '{gameId}'")
        if soloId:
            conditions.append(f"BDT_Assoc.tid = '{soloId}'")
        if modeId:
            conditions.append(f"BDT_Assoc.tid = '{modeId}'")
        if typeId:
            conditions.append(f"BDT_Assoc.tid = '{typeId}'")

        if conditions:
            query += 'WHERE ' + ' AND '.join(conditions)

        print(query)
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()

        if data:
            return jsonify({'result' : data}), 200
        else:
            return jsonify({'msg': 'No data found for the given filter'}), 404
    except Exception as e:
        return jsonify({'msg': 'An error occurred while fetching ranking data', 'error': str(e)}), 500