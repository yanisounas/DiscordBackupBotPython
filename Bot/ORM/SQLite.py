import sqlite3

from Bot.ORM.DBQuery import DbQuery


class SQLite:
    """ SQLite connection class """
    def __init__(self, database: str):
        """ database: str -> Name of the database file with or without .db extension """
        self._database = database
        self._query = None
        self._connection = None

    def connect(self):
        return self

    @property
    def database(self) -> str:
        return self._database

    @property
    def Query(self) -> DbQuery:
        if self._connection is None:
            self.connect()

        self._query = DbQuery(self._connection) if self._query is None else self._query
        return self._query
