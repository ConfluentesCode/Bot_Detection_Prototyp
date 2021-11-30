from Services.DataSaver import DataSaver
from Services.DataLoader import DataLoader


class UserSessionBuilder:
    data_loader = DataLoader()
    data_saver = DataSaver()

    def create_user_sessions_from_access_log(self, user_list: list):

        for user in user_list:
            session_access_logs = self.data_loader.get_user_session_from_ip(user)
            session_information = session_access_logs[0]
            self.data_saver.save_user_session(session_information)
            session_id = self.get_session_id_of_created_session(session_information.ip_address)

            for session_request in session_access_logs:
                self.data_saver.save_request_from_session(session_request, session_id)

    def get_session_id_of_created_session(self, ip_address):
        result = self.data_loader.get_session_id_from_ip_address(ip_address)

        return result
