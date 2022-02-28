from DatabaseConnector.DatabaseSettings import SessionCreator
from DatabaseConnector.Models.AccessLog import AccessLog
from DatabaseConnector.Models.Session import Session
from DatabaseConnector.Models.Request import Request
from DatabaseConnector.Models.Result import Result


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

    def get_request_pattern(self, session_id_list):
        pattern_list = []

        for session_id in session_id_list:
            request_pattern = self.get_request_pattern_from_session(session_id)
            pattern_list.append(request_pattern)

        return pattern_list

    def get_session_ids_from_sessions(self, is_bot_session):
        query_result = self.session_creator.query(Session.session_id).filter(Session.is_Bot == is_bot_session).all()

        session_list = [value for value, in query_result]

        return session_list

    def get_request_pattern_from_session(self, session_id):
        query_result = self.session_creator.query(Request.request_type).filter(
            Request.session_id == session_id).order_by(Request.timestamp)

        pattern_list = [value for value, in query_result]

        return pattern_list

    def get_session_ids_and_pattern_from_id_list(self, session_list):

        session_with_pattern_list = []

        for session in session_list:
            session_with_pattern = self.get_request_pattern_and_session_id(session)
            session_with_pattern_list.append(session_with_pattern)

        return session_with_pattern_list

    def get_request_pattern_and_session_id(self, session_id):
        query_result = self.session_creator.query(Request).filter(Request.session_id == session_id).with_entities(
            Request.request_type).order_by(Request.timestamp)

        pattern_list = [value for value, in query_result]

        return session_id, pattern_list

    def get_result_session_ids(self):
        query_results = self.session_creator.query(Result).with_entities(Result.session_id).all()

        result_session_ids = [value for value, in query_results]

        return result_session_ids

    def get_ground_truth_and_decision(self, session_id):
        query_result = self.session_creator.query(Session).join(Result).filter(Session.session_id == session_id).all()

        ground_truth_decision = query_result[0].is_Bot
        detection_decision = query_result[0].result[0].is_bot_chain_decision

        return ground_truth_decision, detection_decision

    def get_all_session_ids(self):
        query_result = self.session_creator.query(Session).with_entities(Session.session_id).all()

        session_id_list = [value for value, in query_result]

        return session_id_list

    def is_session_from_bot(self, session_id):
        result = self.session_creator.query(Session).filter(Session.session_id == session_id).with_entities(
            Session.is_Bot).first()

        return result.is_Bot
