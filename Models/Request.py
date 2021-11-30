from sqlalchemy import *
from DatabaseConnector.DatabaseSettings import Base


class Request(Base):
    __tablename__ = "Request"

    request_id = Column(Integer, primary_key=True)
    request = Column(String)
    timestamp = Column(DateTime)
    session_id = Column(Integer, ForeignKey('Session.session_id'))

