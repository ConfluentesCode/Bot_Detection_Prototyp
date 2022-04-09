from DatabaseConnector.DatabaseSettings import Base, engine

import AccessLog
import Session
import Request
import Result
import ScoringParameters

# Models must be imported here to bind them in .creat_all() method.
# SQLAlchemy DatabaseCreator must be in the same folder as Models for unknown reasons

Base.metadata.create_all(engine, checkfirst=True)

