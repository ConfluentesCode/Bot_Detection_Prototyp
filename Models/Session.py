from sqlalchemy import *
from DatabaseConnector.DatabaseSettings import Base


class Session(Base):
    __tablename__ = "Session"

    session_id = Column(Integer, primary_key=True)
    ip_address = Column(String)
    id = Column(Integer, )
