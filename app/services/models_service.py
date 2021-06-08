from flask.json import jsonify
from .conn_cur_service import conn_cur, end_conn_cur

class AnimeTable:

    table_header = ['id', 'anime', 'released_date', 'seasons']

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

        