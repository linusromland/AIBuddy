""" Database connection and setup. """

import os
import sqlite3
from sqlite3 import Connection
from database.queries.information import create_table as create_information_table
from database.queries.interests import create_table as create_interests_table


DB_PATH = os.getenv("DB_PATH", "aibuddy")


def create_connection() -> Connection:
    """ Create a connection to the database. """
    return sqlite3.connect(DB_PATH + ".sqlite3")


def create_tables(conn: Connection) -> None:
    """ Create all tables in the database. """

    print("Setting up database...")
    create_information_table(conn)
    create_interests_table(conn)
    print("Database setup complete.")
