from flask.json import jsonify
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

    def create_anime(self, data: dict):
        conn, cur = conn_cur()
        self.create_table()

        if AnimeTable.check_fields(self, data):
            raise KeyError(
                {
                    "available_keys": ["anime", "released_date", "seasons"],
                    "wrong_keys_sended": list(data.keys())
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

        try:
            return (result,)

        except:
            AnimeTable.create_table()
            return {"error": "Not Found"}, HTTPStatus.NOT_FOUND

    def update_anime(self, data: dict, anime_id: int):
        conn, cur = conn_cur()

        if AnimeTable.check_fields(data):
            raise KeyError(
                {
                    "available_keys": ["anime", "released_date", "seasons"],
                    "wrong_keys_sended": list(data.keys())
                }, HTTPStatus.UNPROCESSABLE_ENTITY
            )

        data["anime_id"] = anime_id

        cur.execute(
            """
                UPDATE animes
                SET anime = %(anime)s
                    WHERE id = %(anime_id)s
                RETURNING *
            """,
            data,
        )
        query = cur.fetchone()

        end_conn_cur(conn, cur)

        return dict(zip(self.table_header, query))

    def delete_anime(self, anime_id: int):
        conn, cur = conn_cur()

        if self.select_id(anime_id):
            cur.execute(
                """
                    DELETE FROM animes
                        WHERE id = %(anime_id)s
                """,
                {"anime_id": anime_id},
            )

            end_conn_cur(conn, cur)

            return "No content", HTTPStatus.NO_CONTENT

        return {"error": "Not Found"}, HTTPStatus.NOT_FOUND