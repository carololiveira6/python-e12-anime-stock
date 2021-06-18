from flask import Flask, request, jsonify, Blueprint
from ..services.models_service import AnimeTable
from psycopg2 import errors
from http import HTTPStatus

bp_animes = Blueprint('animes', __name__)

@bp_animes.route('/animes', methods=['GET', 'POST'])
def get_create():

    animes = AnimeTable()
    
    if request.method == 'POST':
        data = request.get_json()

        try:
            return animes.create_anime(data), HTTPStatus.CREATED

        except KeyError as e:
            return e.args[0], HTTPStatus.UNPROCESSABLE_ENTITY

        except errors.UniqueViolation as _:
            return {"error": "anime is already exists"}, HTTPStatus.UNPROCESSABLE_ENTITY

    return jsonify({"data": animes.return_data()}), HTTPStatus.OK

@bp_animes.route('/animes/<int:anime_id>', methods=['GET'])
def filter(anime_id):

    animes = AnimeTable()

    try:
        return {"data": [animes.select_id(anime_id)]},  HTTPStatus.OK

    except:
        return {"error": "Not Found"}, HTTPStatus.NOT_FOUND

@bp_animes.route('/animes/<int:anime_id>', methods=['PATCH'])
def update(anime_id):

    animes = AnimeTable()
    data = request.get_json()

    try:
        return animes.update_anime(data, anime_id)

    except KeyError as e:
        return e.args

    except TypeError as _:
        return {"error": "Not Found"}, HTTPStatus.NOT_FOUND

@bp_animes.route("/animes/<int:anime_id>", methods=["DELETE"])
def delete(anime_id: int):
    animes = AnimeTable()

    try:
        return animes.delete_anime(anime_id)
    
    except:
        return {"error": "Not Found"}, HTTPStatus.NOT_FOUND
