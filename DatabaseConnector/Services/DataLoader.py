from DatabaseConnector.DatabaseSettings import SessionCreator
from DatabaseConnector.Models.AccessLog import AccessLog
from DatabaseConnector.Models.Session import Session
from DatabaseConnector.Models.Request import Request


class DataLoader:
    session_creator = SessionCreator()

    def get_users_from_access_log(self):
        query_results = self.session_creator.query(AccessLog.ip_address).group_by(AccessLog.ip_address).all()

        user_ip_address_list = [value for value, in query_results]

        return user_ip_address_list

    def get_user_session_from_ip(self, user_ip: str):
        user_session = self.session_creator.query(AccessLog).filter(AccessLog.ip_address == user_ip).all()

        return user_session

    def get_session_id_from_ip_address(self, ip_address):
        session = self.session_creator.query(Session).filter(Session.session_ip_address == ip_address).first()

        return session.session_id

    def get_request_pattern(self, is_bot_session):
        bot_pattern_list = []

        session_id_list = self.get_session_ids_from_sessions(is_bot_session)

        for session_id in session_id_list:
            request_pattern = self.get_request_pattern_from_session(session_id)
            bot_pattern_list.append(request_pattern)

        return bot_pattern_list

    def get_session_ids_from_sessions(self, is_bot_session):
        query_result = self.session_creator.query(Session.session_id).filter(Session.is_Bot == is_bot_session).all()

        session_list = [value for value, in query_result]

        return session_list

    def get_request_pattern_from_session(self, session_id):
        query_result = self.session_creator.query(Request.request_type).filter(Request.session_id == session_id).order_by(Request.timestamp)

        pattern_list = [value for value, in query_result]

        return pattern_list


