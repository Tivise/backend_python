from flask import jsonify, request
from middleware.db import get_mysql_connection
from controllers.steam_controller import get_steam_user_information_local
from middleware.auth import token_required
import requests

##############################################################################
# get_game_user_information:
#
# Permet d'obtenir les differentes information d'un utilisateur (username,
# kills, deaths, level, experience, etc) lie a son compte de jeu.
#
# Parametres: steamID
# Requirements: Authentification token
##############################################################################
@token_required
def get_game_user_information(steamID):
    print(steamID)
    if steamID:

        try:
            conn = get_mysql_connection()
            cursor = conn.cursor()

            query = f'SELECT accountId, username, mail, coin, redzap, vip, level, win, lose, avatarId, kills, userId, experience FROM user WHERE accountId = \'{steamID}\''
            cursor.execute(query)
            game_user_data = cursor.fetchone()
            cursor.close()

            # Compte trouvé
            if game_user_data:
                print("Envois des données utilisateurs")
                return jsonify(game_user_data), 200

            # Creer un compte de jeu a son compte STEAM
            else:
                return create_game_account(steamID)

        except Exception as e:
            # En cas d'erreur, imprimez l'erreur ou retournez un message d'erreur approprié
            return jsonify({'msg': 'An error occurred while fetching Steam user data', 'error': str(e)}), 500


    else:
        return jsonify({'msg': 'Missing steamID'}), 400


##############################################################################
# create_game_account:
# 
# Permet de creer un compte de jeu si l'utilisateur Steam n'en a pas encore.
# 
# Parameter: steamID
##############################################################################
def create_game_account(steamID):
    try:
        conn = get_mysql_connection()
        player_data = get_steam_user_information_local(steamID)
        cursor = conn.cursor()
        query = "INSERT INTO user (accountId, username ,password ,mail) VALUES ('"+steamID+"', '"+player_data['personaname']+"', '---', '---')"
        cursor.execute(query)

        query2 = f'SELECT accountId, username, mail, coin, redzap, vip, level, win, lose, avatarId, kills, userId, experience FROM user WHERE accountId = \'{steamID}\''
        cursor.execute(query2)
        game_user_data = cursor.fetchone()

        cursor.close()
        return jsonify(game_user_data), 200

    except Exception as e:
        return jsonify({'msg':'An error occured while creating an account for the user: ' + steamID}), 400


##############################################################################
# set_game_user_mail:
#
# Permet de modifier les differentes information d'un utilisateur (username,
# kills, deaths, level, experience, etc) lie a son compte de jeu.
#
# Parametres: steamID, mail
# Requirements: Authentification token
##############################################################################
@token_required
def set_game_user_mail():
    steamID = request.args.get('steamID')
    mail = request.args.get('mail')
    if steamID and mail:

        try:
            conn = get_mysql_connection()
            cursor = conn.cursor()

            query = f'UPDATE user SET mail = \'{mail}\' WHERE accountId = \'{steamID}\''
            cursor.execute(query)
            cursor.close()
            return jsonify({'msg' : 'Mail updated'}), 200

        except Exception as e:
            # En cas d'erreur, imprimez l'erreur ou retournez un message d'erreur approprié
            return jsonify({'msg': 'An error occurred while editing game user mail', 'error': str(e)}), 500


    else:
        return jsonify({'msg': 'Missing steamID'}), 400


##############################################################################
# delete_game_user_mail:
#
# Permet de supprimer le compte de jeu d'un joueur
#
# Parametres: steamID
# Requirements: Authentification token
##############################################################################
@token_required
def delete_game_user():
    steamID = request.args.get('steamID')
    if steamID:
        try:
            conn = get_mysql_connection()
            cursor = conn.cursor()

            query = f'DELETE FROM user WHERE accountId = \'{steamID}\''
            cursor.execute(query)
            cursor.close()
            return jsonify({'msg' : 'User deleted'}), 200

        except Exception as e:
            # En cas d'erreur, imprimez l'erreur ou retournez un message d'erreur approprié
            return jsonify({'msg': 'An error occurred while removing an user', 'error': str(e)}), 500


    else:
        return jsonify({'msg': 'Missing steamID'}), 400