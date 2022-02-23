from DatabaseConnector.DatabaseSettings import Base, engine

import AccessLog
import Session
import Request
import Result

# Models must be imported here to bind them in .creat_all() method.
# SQLAlchemy DatabaseCreator must be in the same folder as Models for unknown reasons
# TODO Base problem clarification

Base.metadata.create_all(engine, checkfirst=True)

