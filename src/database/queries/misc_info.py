""" Database queries for Misc. Information table. """
from sqlite3 import Connection


def create_table(conn: Connection) -> None:
    """ Create the Misc. Information table. """
    print("Creating interests table if not exists...")

    conn.execute('''CREATE TABLE IF NOT EXISTS misc_information
                    (id INTEGER PRIMARY KEY, info TEXT)''')
    conn.commit()


def add_misc_info(conn: Connection, info: str) -> None:
    """ Add an interest. """

    conn.execute("INSERT INTO misc_information (info) VALUES (?)", (info,))
    conn.commit()


def remove_misc_info(conn: Connection, info_id: int) -> None:
    """ Remove an interest. """

    conn.execute("DELETE FROM misc_information WHERE id=?", (info_id,))
    conn.commit()


def get_all_misc_info(conn: Connection) -> list[dict]:
    """ Get all interests. """

    cursor = conn.cursor()
    cursor.execute("SELECT id, info FROM misc_information")
    rows = cursor.fetchall()

    return [{"id": row[0], "info": row[1]} for row in rows]
