from DatabaseConnector.Services.DataSaver import DataSaver
from DatabaseConnector.Services.DataLoader import DataLoader
from DataPreparator.Services.BotSessionIdentifier import BotSessionIdentifier
from DataPreparator.Services.RequestTypeExtractor import RequestTypeExtractor


class UserSessionBuilder:
    data_loader = DataLoader()
    data_saver = DataSaver()
    session_identifier = BotSessionIdentifier()

    def create_user_sessions(self, user_ip_list: list):

        for current_user_ip in user_ip_list:
            self.create_user_session_from_access_logs(current_user_ip)

    def create_user_session_from_access_logs(self, user_ip):
        session_access_logs = self.data_loader.get_user_session_from_ip(user_ip)

        session_ip = session_access_logs[0].ip_address
        session_user_agent = session_access_logs[0].user_agent

        is_bot_session = self.session_identifier.is_user_session_from_bot(session_user_agent, session_ip)

        self.data_saver.save_user_session(session_ip, session_user_agent, is_bot_session)
        self.safe_requests_of_session(session_access_logs, user_ip)

    def safe_requests_of_session(self, user_access_log, user_ip):
        session_id = self.get_session_id_of_user(user_ip)
        type_extractor = RequestTypeExtractor()

        for session_request in user_access_log:
            request_type = type_extractor.get_request_type_from_resource(session_request.resource)
            self.data_saver.save_request_from_session(session_request, request_type, session_id)

    def get_session_id_of_user(self, ip_address):
        result = self.data_loader.get_session_id_from_ip_address(ip_address)

        return result
