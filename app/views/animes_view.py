from flask import Flask, request, jsonify, Blueprint
from ..services.models_service import AnimeTable
from psycopg2 import errors

bp_animes = Blueprint('animes', __name__, url_prefix='/api')

@bp_animes.route('/animes', methods=['GET', 'POST'])
def get_create():
    animes = AnimeTable()
    
    if request.method == 'POST':
        data = request.get_json()

        try:
            return animes.create_anime(data), 201

        except KeyError as e:
            return {"avaliable_keys": ["anime", "released_date", "seasons"],
            "wrong_keys_sended": [
                f'\"{e.args[0]}\"'
                ]}, 422

        except errors.UniqueViolation as _:
            return {"error": "anime is already exists"}, 422

    return jsonify({"data": animes.return_data()}), 200

@bp_animes.route('/animes/<int:anime_id>', methods=['GET'])
def filter(anime_id):
    animes = AnimeTable()

    return animes.select_id(anime_id)