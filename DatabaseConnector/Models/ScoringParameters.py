from sqlalchemy import *
from DatabaseConnector.DatabaseSettings import Base


class ScoringParameters(Base):
    __tablename__ = "ScoringParameters"

    scoring_id = Column(Integer, primary_key=True)
    test_date = Column(DateTime)
    detection_approach = Column(String)
    recall = Column(Float)
    precision = Column(Float)
    f1 = Column(Float)
    accuracy = Column(Float)



