from sqlalchemy import *
from Playground.DatabaseConnector.base import Base


class a(Base):
    __tablename__ = "A"

    id = Column(Integer, primary_key=True)
    text = Column(String)




