from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

Engine = create_engine(
        "postgresql://igarashi:tomoe123@localhost:5432/mydb", echo=True)

session = scoped_session(
        sessionmaker(
            autocommit = False,
            autoflush = False,
            bind = Engine                                       )
    )

Base = declarative_base()
Base.query = session.query_property()

from flask import Flask

app = Flask(__name__)
app.config.from_object('testapp.config')

import testapp.views
