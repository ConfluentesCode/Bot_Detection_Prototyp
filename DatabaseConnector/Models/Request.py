from sqlalchemy import *

from DatabaseConnector.DatabaseSettings import Base
from DataPreparator.Enums.RequestType import RequestType


class Request(Base):
    __tablename__ = "Request"

    request_id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    http_method = Column(String)
    resource = Column(String)
    status_code = Column(String)
    referer = Column(String)
    request_type = Column(Enum(RequestType))
    session_id = Column(Integer, ForeignKey('Session.session_id'))

