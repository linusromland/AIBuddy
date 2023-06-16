""" Database queries for interests table. """
from sqlite3 import Connection


def create_table(conn: Connection) -> None:
    """ Create the interests table. """

    conn.execute('''CREATE TABLE IF NOT EXISTS interests
                    (id INTEGER PRIMARY KEY, interest TEXT)''')
    conn.commit()


def add_interest(conn: Connection, interest: str) -> None:
    """ Add an interest. """

    conn.execute("INSERT INTO interests (interest) VALUES (?)", (interest,))
    conn.commit()


def remove_interest(conn: Connection, interest: str) -> None:
    """ Remove an interest. """

    conn.execute("DELETE FROM interests WHERE interest = ?", (interest,))
    conn.commit()


def get_all_interests(conn: Connection) -> list:
    """ Get all interests. """

    cursor = conn.cursor()
    cursor.execute("SELECT interest FROM interests")
    rows = cursor.fetchall()

    return [row[0] for row in rows] if rows else []
