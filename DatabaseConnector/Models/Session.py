from sqlalchemy import *
from sqlalchemy.orm import relationship
from DatabaseConnector.DatabaseSettings import Base
from DataPreparator.Enums.GroupAffiliation import GroupAffiliation


class Session(Base):
    __tablename__ = "Session"

    session_id = Column(Integer, primary_key=True)
    session_ip_address = Column(String)
    session_useragent = Column(String)
    is_Bot = Column(Boolean, nullable=True)
    group_affiliation = Column(Enum(GroupAffiliation))
    requests = relationship('Request', backref='request_session')
    result = relationship('Result', backref='result_session')
