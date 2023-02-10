from functions.string_operations import StringDelete
from functions.databaseLink import SQLExecute, OpenSQLConnection
from functions.lists import Last, Riffle, Rest
from functions.matrices_and_arrays import ConstantArray
from functions.string_operations import StringJoin, ToString
from functions.monitoring import TimeTagMessage
import os
import fnmatch


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


_directory = 'D:\Mir Books Processing'
_booksHave = []
books = find('*', _directory)
for data in books:
    data = StringDelete(data, [_directory, '\\', '.pdf', '.djvu']).split(' - ')
    _booksHave.append(data)

_sqlConnection = OpenSQLConnection('D:\Programming\_databases\collections.db')
_sqlCursor = _sqlConnection.cursor()
_extraTab = "\t" * 16


def nameExtract(_name: str):
    if "." in _name:
        _name = _name.split('.')
        _lastName = Last(_name)
        del _name[-1]
        _name = Riffle(_name, ConstantArray(".", len(_name))) + ["."]
        _name = StringJoin(_name)
        return [_name, _lastName]
    if "." not in _name:
        return _name.split(' ')


print(f"Found a total of {_booksHave.__len__()} books\n")

_updateDatabasesQ = True
_bookTrack01 = 1
_bookLength = _booksHave.__len__()

TimeTagMessage("Starting Books, Authors, Associations Upload")
if True:
    for book in _booksHave:
        authorList = Rest(book)
        book = book[0]
        _bookSQLResults = SQLExecute(_sqlConnection, "SELECT * FROM books WHERE bookName = '%s'" % book).fetchall()
        _prefix = f" | Book {_bookTrack01} off {_bookLength}"
        if _bookSQLResults.__len__() == 0:
            _bookId = SQLExecute(_sqlConnection, "SELECT Max(bookID) + 1 FROM books").fetchall()[0][0]
            TimeTagMessage(
                f" |{_prefix} | Book not found in the table. Inserting into books.\t | {book}")
            _sqlQuery = "INSERT INTO books (bookID, bookName, series) VALUES (" + str(
                _bookId) + ", '" + book + "', NULL)"
            if _updateDatabasesQ:
                _sqlConnection.cursor().execute(_sqlQuery)
                _sqlConnection.commit()
            elif not _updateDatabasesQ:
                print(f"{_sqlQuery}\n")
        else:
            _bookId = _bookSQLResults[0][0]
            TimeTagMessage(f"{_prefix} | Book already exists in the table. Moving on.\t\t\t\t\t\t | {book}")

        _authorTrack = 1
        _authorLength = authorList.__len__()
        for _author in authorList:
            _nameExtract = nameExtract(_author)
            _authorSQLResults = SQLExecute(_sqlConnection,
                                           "SELECT * FROM authors WHERE firstName = '" +
                                           _nameExtract[0] + "' AND lastName = '" + _nameExtract[1] + "'").fetchall()
            _prefix = f" | Book {_bookTrack01} off {_bookLength} | Author {_authorTrack} off {_authorLength}"
            if _authorSQLResults.__len__() == 0:
                _authorId = SQLExecute(_sqlConnection, "SELECT Max(authorID) + 1 FROM authors").fetchall()[0][0]
                TimeTagMessage(f"{_prefix} | Author not found in the table. Inserting into authors.\t | {_author}")
                _sqlQuery = "INSERT INTO authors (authorID, firstName, lastName) VALUES (" + str(_authorId) + ", '" + \
                            _nameExtract[0] + "', '" + _nameExtract[1] + "')"
                if _updateDatabasesQ:
                    _sqlConnection.cursor().execute(_sqlQuery)
                    _sqlConnection.commit()
                elif not _updateDatabasesQ:
                    print(f"{_sqlQuery}\n")
            else:
                _authorId = _authorSQLResults[0][0]
                TimeTagMessage(f"{_prefix} | Author already exists in the table. Moving on.\t | {_author}")

            _authorBookSQLResults = "SELECT * FROM authorBook WHERE bookFK =" + str(
                _bookId) + " AND authorFK = " + str(_authorId)
            _authorBookSQLResults = SQLExecute(_sqlConnection, _authorBookSQLResults).fetchall()
            if _authorBookSQLResults.__len__() == 0:
                print(f"{_extraTab}Association not found in the table. Now creating the link.")
                print("-" * 150)
                _getMaxId = "SELECT max(ID) + 1 FROM authorBook"
                authorBookID = SQLExecute(_sqlConnection, _getMaxId).fetchall()[0][0]
                authorBookID = ToString(authorBookID)
                authorFK = ToString(_authorId)
                bookFK = ToString(_bookId)
                linkQuery = "INSERT INTO authorBook (ID, authorFK, bookFK) VALUES (" + authorBookID + ", " + authorFK + \
                            ', ' + bookFK + ")"
                if _updateDatabasesQ:
                    _sqlConnection.cursor().execute(linkQuery)
                    _sqlConnection.commit()
                elif not _updateDatabasesQ:
                    print(linkQuery + "\n")
            else:
                print(f"{_extraTab}| Author-Book association found in the table. I am moving on!")
                print("-" * 150)

            _authorTrack += 1
        _bookTrack01 += 1
