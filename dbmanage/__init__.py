"""
LexiconCognito

dbmanage,
Interface for SQLite database management.
"""

import sqlite3

class database:
    """
    Class containing database management functions.
    Do not use this class for non-sync or non-serial processing!
    """
    def __init__(self):
        """
        Initiation function for database class, connects to db file.
        """
        self.manage = sqlite3.connect("main.db", check_same_thread = False)

    def generate(self):
        """
        Generates tables for database. Should only be ran once.
        """
        with open("schema.sql") as generate_script: self.manage.executescript(generate_script.read())

    def close(self):
        """
        Close self.manage database connection.
        """
        self.manage.close()
