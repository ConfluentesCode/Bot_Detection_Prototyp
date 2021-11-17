from sqlalchemy import *
from DatabaseConnector.DatabaseSettings import Base


class AccessLog(Base):
    __tablename__ = "AccessLog"

    id = Column(Integer, primary_key=True)
    ip_address = Column(String)
    timestamp = Column(String)
    http_method = Column(String)
    endpoint = Column(String)
    http_version = Column(String)
    status_code = Column(String)
    url = Column(String)
    user_agent = Column(String)

