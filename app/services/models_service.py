from flask.json import jsonify, request
from .conn_cur_service import conn_cur, end_conn_cur
from http import HTTPStatus

class AnimeTable:

    table_header = ['id', 'anime', 'released_date', 'seasons']
    required_fields = ['anime', 'released_date', 'seasons']

    @staticmethod
    def create_table() -> None:
        conn, cur = conn_cur()

        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS animes
                    (
                        id BIGSERIAL PRIMARY KEY,
                        anime VARCHAR(100) NOT NULL UNIQUE,
                        released_date DATE NOT NULL,
                        seasons INTEGER NOT NULL
                    )
            """
        )

        end_conn_cur(conn, cur)

    def check_fields(self, data: dict):
        required_keys = ["anime", "released_date", "seasons"]
        recived_keys = data.keys()

        return [required for required in required_keys if required not in recived_keys]

    def analyze_fields(self, data: dict):
        required_keys = ["anime", "released_date", "seasons"]
        recived_keys = data.keys()

        result =  [recived for recived in recived_keys if recived not in required_keys]

        return result

    def create_anime(self, data: dict):
        conn, cur = conn_cur()
        self.create_table()

        required_keys = ["anime", "released_date", "seasons"]
        recived_keys = data.keys()

        result =  [recived for recived in recived_keys if recived not in required_keys]


        if AnimeTable.analyze_fields(self, data):
            raise KeyError(
                {
                    "available_keys": ["anime", "released_date", "seasons"],
                    "wrong_keys_sended": list(result)
                }, HTTPStatus.UNPROCESSABLE_ENTITY
            )

        data['anime'] = data['anime'].title()

        cur.execute(
            """
                INSERT INTO animes
                    (anime, released_date, seasons)
                VALUES
                    (%(anime)s, %(released_date)s, %(seasons)s)
                RETURNING *
            """,
            data,
        )
        query = cur.fetchone()

        end_conn_cur(conn, cur)

        result = dict(zip(self.table_header, query))

        result["released_date"] = result["released_date"].strftime("%d/%m/%Y")

        return result
    
    def return_data(self):
        conn, cur = conn_cur()

        if AnimeTable.create_table() == False:
            return {"data": []}, HTTPStatus.OK

        cur.execute("SELECT * FROM animes")

        query = cur.fetchall()

        end_conn_cur(conn, cur)

        result = [dict(zip(self.table_header, show_table)) for show_table in query]

        for data in result:
            data["released_date"] = data["released_date"].strftime("%d/%m/%Y")

        return result

    def select_id(self, anime_id):
        conn, cur = conn_cur()
        
        cur.execute("SELECT * FROM animes WHERE id = %(anime_id)s", {"anime_id": anime_id})

        query = cur.fetchone()

        end_conn_cur(conn, cur)

        result = dict(zip(self.table_header, query))
        
        result["released_date"] = result["released_date"].strftime("%d/%m/%Y")

        return result

    def update_anime(self, data: dict, anime_id: int):
        conn, cur = conn_cur()
        return_data = self.select_id(anime_id)

        if AnimeTable.analyze_fields(self, data):
            raise KeyError(
                {
                    "available_keys": ["anime", "released_date", "seasons"],
                    "wrong_keys_sended": list(data.keys())
                }, HTTPStatus.UNPROCESSABLE_ENTITY
            )

        update_data = request.get_json()        
        return_data.update(update_data)

        data = return_data
        data['anime'] = data['anime'].title()
        data["anime_id"] = anime_id

        cur.execute(
            """
                UPDATE animes
                SET anime = %(anime)s,
                    released_date = %(released_date)s,
                    seasons = %(seasons)s
                        WHERE id = %(anime_id)s
                RETURNING *
            """,
           data,
        )
        query = cur.fetchone()

        end_conn_cur(conn, cur)

        result = dict(zip(self.table_header, query))

        result["released_date"] = result["released_date"].strftime("%d/%m/%Y")

        return result

    def delete_anime(self, anime_id: int):
        conn, cur = conn_cur()
        return_data = self.select_id(anime_id)

        if return_data:
            cur.execute(
                """
                    DELETE FROM animes
                        WHERE id = %(anime_id)s
                """,
                {"anime_id": anime_id},
            )

            end_conn_cur(conn, cur)

            return "No content", HTTPStatus.NO_CONTENT