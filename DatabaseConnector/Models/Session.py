from sqlalchemy import *
from sqlalchemy.orm import relationship
from DatabaseConnector.DatabaseSettings import Base


class Session(Base):
    __tablename__ = "Session"

    session_id = Column(Integer, primary_key=True)
    session_ip_address = Column(String)
    session_useragent = Column(String)
    is_Bot = Column(Boolean, nullable=True)
    requests = relationship('Request', backref='request_session')
