from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Playground.DatabaseConnector import base

import a
import b
import c

engine = create_engine(
    'sqlite:////Users/bjarneschroeder/PycharmProjects/Bot_Detection_Prototyp/DatabaseConnector/Database/Test.db')
base.Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)
session = Session()

a1 = a.AccessLog("test", "test", "test", "test", "test", "test", "test", "test")

# a2 = AccessLog.AccessLog()
# a2.ip_address = 'test2'
# a2.timestamp = 'test2'
# a2.http_method = 'test2'
# a2.http_version = 'tesst2'
# a2.status_code = 'test2'
# a2.url = 'test'
# a2.endpoint = 'test2'
# a2.user_agent = 'test'
# a2.id = 2

# session.add(a2)
session.commit()

