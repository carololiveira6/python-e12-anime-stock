from flask.json import jsonify
from .conn_cur_service import conn_cur, end_conn_cur

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
                        season INTEGER NOT NULL
                    )
            """
        )

        end_conn_cur(conn, cur)

    def check_fields(self, data: dict):
        recived_keys = data.keys()

        return [required for required in self.required_fields if required not in recived_keys]

    def create_anime(self, data: dict):
        conn, cur = conn_cur()
        self.create_table()

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

        if AnimeTable.create_table(self) == False:
            return []

        cur.execute("SELECT * FROM animes")

        query = cur.fetchall()

        end_conn_cur(conn, cur)

        result = [dict(zip(self.table_header, show_table)) for show_table in query]

        for data in result:
            data["released_date"] = data["released_date"].strftime("%d/%m/%Y")

        return result

    def select_id(self, serie_id):
        conn, cur = conn_cur()

        try:
            
            cur.execute("SELECT * FROM aimes WHERE id = %(serie_id)s", {"serie_id": serie_id})

            query = cur.fetchone()

            end_conn_cur(conn, cur)

            result = dict(zip(self.table_header, query))
    
            return {"data": result}

        except:

            AnimeTable.create_table(self)
            return {"error": "Not Found"}, 404