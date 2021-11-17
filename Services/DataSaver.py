from DatabaseConnector.DatabaseSettings import SessionCreator
from Models.AccessLog import AccessLog


class DataSaver:

    session_creator = SessionCreator()

    def save_access_logs(self, access_log_entry_list: list):
        for access_log_entry in access_log_entry_list:
            access_log_model = AccessLog(ip_address=access_log_entry[0], timestamp=access_log_entry[1],
                                         http_method=access_log_entry[2], url=access_log_entry[3],
                                         status_code=access_log_entry[4], http_version=access_log_entry[5],
                                         endpoint=access_log_entry[6], user_agent=access_log_entry[7])
            self.session_creator.add(access_log_model)

        self.session_creator.commit()
