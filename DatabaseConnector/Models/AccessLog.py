from sqlalchemy import *
from DatabaseConnector.DatabaseSettings import Base


class AccessLog(Base):
    __tablename__ = "AccessLog"

    access_log_id = Column(Integer, primary_key=True)
    ip_address = Column(String)
    timestamp = Column(DateTime)
    http_method = Column(String)
    endpoint = Column(String)
    http_version = Column(String)
    status_code = Column(String)
    uri = Column(String)
    user_agent = Column(String)

