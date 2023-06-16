from sqlite3 import Connection


def create_table(conn: Connection) -> None:
    conn.execute('''CREATE TABLE IF NOT EXISTS interests
                    (id INTEGER PRIMARY KEY, interest TEXT)''')
    conn.commit()


def add_interest(conn: Connection, interest: str) -> None:
    conn.execute("INSERT INTO interests (interest) VALUES (?)", (interest,))
    conn.commit()


def remove_interest(conn: Connection, interest: str) -> None:
    conn.execute("DELETE FROM interests WHERE interest = ?", (interest,))
    conn.commit()


def get_all_interests(conn: Connection) -> list:
    cursor = conn.cursor()
    cursor.execute("SELECT interest FROM interests")
    rows = cursor.fetchall()

    return [row[0] for row in rows] if rows else []
