from sqlalchemy import *
from Playground.DatabaseConnector.base import Base


class C(Base):
    __tablename__ = "C"
    id = Column(Integer, primary_key=True)
    A_id = Column(Integer, ForeignKey("AccessLog.id"))
