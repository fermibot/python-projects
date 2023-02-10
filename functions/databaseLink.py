import sqlite3


def OpenSQLConnection(_databasePath):
    return sqlite3.connect(_databasePath)


def SQLExecute(_sqlConnection, _query: str):
    return _sqlConnection.cursor().execute(_query)
