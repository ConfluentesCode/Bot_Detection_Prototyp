from DatabaseConnector.DatabaseSettings import SessionCreator
from Models.AccessLog import AccessLog
from Models.Session import Session
from Models.Request import Request


# TODO ORM verstehen

class DataSaver:
    session_creator = SessionCreator()

    def save_access_log_list(self, access_log_entry_list: list):
        for access_log_entry in access_log_entry_list:
            access_log_model = AccessLog(ip_address=access_log_entry[0], timestamp=access_log_entry[1],
                                         http_method=access_log_entry[2], uri=access_log_entry[3],
                                         status_code=access_log_entry[4], http_version=access_log_entry[5],
                                         endpoint=access_log_entry[6], user_agent=access_log_entry[7])
            self.session_creator.add(access_log_model)

        self.session_creator.commit()

    # Annahme ist, dass der user-agent waehrend der sesssion identisch bleibt und die ip-addresse nur einmal auftaucht
    def save_user_session(self, ip_address, user_agent, is_bot):
        session_model = Session(session_ip_address=ip_address,
                                session_useragent=user_agent, is_Bot=is_bot)
        self.session_creator.add(session_model)
        self.session_creator.commit()

    def save_request_from_session(self, session_access_log, request_type, session_id):
        request_model = Request(uri=session_access_log.uri, request_type=request_type, endpoint=session_access_log.endpoint,  timestamp=session_access_log.timestamp, status_code=session_access_log.status_code,
                                session_id=session_id)
        self.session_creator.add(request_model)
        self.session_creator.commit()
