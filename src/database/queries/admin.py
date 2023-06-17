""" Admin queries. """

from sqlite3 import Connection


def create_table(conn: Connection) -> None:
    """ Create the admin table. """
    print("Creating admin table if not exists...")

    conn.execute('''CREATE TABLE IF NOT EXISTS admins
                    (discord_id TEXT PRIMARY KEY, permission_level INTEGER)''')
    conn.commit()


def add_admin(conn: Connection, discord_id: str, permission_level: int) -> None:
    """ Add an admin. """

    conn.execute("INSERT INTO admins (discord_id, permission_level) VALUES (?, ?)",
                 (discord_id, permission_level))
    conn.commit()


def remove_admin(conn: Connection, discord_id: str) -> None:
    """ Remove an admin. """

    conn.execute("DELETE FROM admins WHERE discord_id = ?", (discord_id,))
    conn.commit()


def get_admin(conn: Connection, discord_id: str) -> dict | None:
    """ Get admin details by discord_id. """

    cursor = conn.cursor()
    cursor.execute(
        "SELECT discord_id, permission_level FROM admins WHERE discord_id = ?", (discord_id,))
    row = cursor.fetchone()

    if row:
        return {"discord_id": row[0], "permission_level": row[1]}
    return None


def get_all_admins(conn: Connection) -> list[dict]:
    """ Get all admins. """

    cursor = conn.cursor()
    cursor.execute("SELECT discord_id, permission_level FROM admins")

    admins = []
    for row in cursor.fetchall():
        admins.append({"discord_id": row[0], "permission_level": row[1]})

    return admins
