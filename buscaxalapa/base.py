from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgres://postgres:Barbara1621@localhost:5432/BuscaXalapa")

Session = sessionmaker(bind=engine)

Base = declarative_base()