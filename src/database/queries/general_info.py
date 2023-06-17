""" General Information queries. """

from sqlite3 import Connection


def create_table(conn: Connection) -> None:
    """ Create the information table. """
    print("Creating information table if not exists...")

    conn.execute('''CREATE TABLE IF NOT EXISTS general_information
                    (name TEXT, birthday TEXT, city TEXT, country TEXT)''')
    conn.commit()

    information = get_information(conn)

    if information is None:
        print("No information found. Creating default information...")
        set_information(conn, "name", "John Doe")
        set_information(conn, "birthday", "2nd of January 2000")
        set_information(conn, "city", "Boston, MA")
        set_information(conn, "country", "United States of America")


def set_information(conn: Connection, key: str, value: str) -> None:
    """ Set the information. """

    print(f"Setting {key} to {value}...")

    if key not in ["name", "birthday", "city", "country"]:
        raise ValueError(
            "Invalid key. Valid keys are: name, birthday, city or country")

    # there should only be one row. If there is no row, insert one. If there is one, update it.
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, birthday, city, country FROM general_information")
    row = cursor.fetchone()

    if not row:
        cursor.execute(
            "INSERT INTO general_information VALUES (?, ?, ?, ?)", (None, None, None, None))

    cursor.execute(
        f"UPDATE general_information SET {key} = ?", (value,))

    cursor.close()

    conn.commit()


def get_information(conn: Connection) -> dict | None:
    """ Get the information. """

    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, birthday, city, country FROM general_information")
    row = cursor.fetchone()

    if row:
        return {"name": row[0], "birthday": row[1], "city": row[2], "country": row[3]}
    return None
