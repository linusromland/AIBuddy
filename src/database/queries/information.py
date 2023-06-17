""" Information queries. """

from sqlite3 import Connection


def create_table(conn: Connection) -> None:
    """ Create the information table. """
    print("Creating information table if not exists...")

    conn.execute('''CREATE TABLE IF NOT EXISTS information
                    (name TEXT, birthday TEXT, city TEXT, country TEXT)''')
    conn.commit()


def set_information(conn: Connection, name: str, birthday: str, city: str, country: str) -> None:
    """ Set the information. """

    conn.execute("DELETE FROM information")
    conn.execute("INSERT INTO information (name, birthday, city, country) VALUES (?, ?, ?, ?)",
                 (name, birthday, city, country))
    conn.commit()


def get_information(conn: Connection) -> dict | None:
    """ Get the information. """

    cursor = conn.cursor()
    cursor.execute("SELECT name, birthday, city, country FROM information")
    row = cursor.fetchone()

    if row:
        return {"name": row[0], "birthday": row[1], "city": row[2], "country": row[3]}
    return None
