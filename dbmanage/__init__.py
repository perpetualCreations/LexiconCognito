"""
LexiconCognito

dbmanage,
Interface for SQLite database management.
"""

import sqlite3

class database:
    """
    Class containing database management functions.
    """
    def __init__(self, database_path):
        """
        Initiation function for database class, connects to given database file.
        :param database_path: str, path to database file
        """
        self.manage = sqlite3.connect(database_path)

    def generate(self, schema_path):
        """
        Generates tables for database. Should only be ran once.
        :param schema_path: str, path to SQL schema
        """
        self.manage.executescript(schema_path)

    def close(self):
        """
        Close self.manage database connection.
        """
        self.manage.close()
