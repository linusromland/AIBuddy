""" Check if a user has the required permission level. """
from sqlite3 import Connection
from database.queries.admin import get_all_admins, add_admin


def check_permission(conn: Connection, discord_id: str, full_admin: bool) -> bool:
    """ Check if a user has the required permission level. """
    admins = get_all_admins(conn)

    if len(admins) == 0:
        add_admin(conn, discord_id, 2)
        return True

    admin = next(
        (admin for admin in admins if admin["discord_id"] == discord_id), None)

    if admin:
        return admin["permission_level"] == 2 if full_admin else admin["permission_level"] >= 1
    return False
