from sqlalchemy import *
from Playground.DatabaseConnector.base import Base

class B(Base):
    __tablename__ = "B"
    id    = Column(Integer, primary_key=True)
    A_id  = Column(Integer, ForeignKey("AccessLog.id"))