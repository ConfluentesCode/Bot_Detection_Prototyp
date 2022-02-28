from sqlalchemy import *
from DatabaseConnector.DatabaseSettings import Base


class Result(Base):
    __tablename__ = "Result"

    result_id = Column(Integer, primary_key=True)
    group_id = Column(Integer)
    session_id = Column(Integer, ForeignKey('Session.session_id'))
    is_bot_decision = Column(Boolean, nullable=True)
    human_prob = Column(Float)
    bot_prob = Column(Float)
