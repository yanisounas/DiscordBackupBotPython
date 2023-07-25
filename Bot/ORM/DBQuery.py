from mysql.connector import cursor as mysql_cursor, MySQLConnection, CMySQLConnection
from sqlite3 import Connection as SQLiteConnection, Cursor as SQLiteCursor


class DbQuery:
    def __init__(self, db: SQLiteConnection | MySQLConnection | CMySQLConnection):
        self._db = db
        self._cursor = self._db.cursor()

    @property
    def cursor(self) -> SQLiteCursor | mysql_cursor.CursorBase | mysql_cursor.MySQLCursor:
        return self._cursor
