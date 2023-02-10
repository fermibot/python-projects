from sqlalchemy import (create_engine, MetaData, Table, Column, Integer)

from sqlalchemy.pool import NullPool


engine = create_engine("postgres://localhost/notes")
