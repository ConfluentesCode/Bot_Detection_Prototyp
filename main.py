from Constants import Constants
from Services.AccessLogReader import AccessLogReader
from Services.UserSessionBuilder import UserSessionBuilder
from Services.DataSaver import DataSaver
from Services.DataLoader import DataLoader


file_path = Constants.ACCESS_LOG_FILE_PATH

if __name__ == '__main__':
    # get information from access logs
    file_reader = AccessLogReader()
    access_log_list = file_reader.read_csv_file(file_path)

    # write information from access log in sqlite database
    if Constants.FILL_DATABASE_TOGGLE:
        data_saver = DataSaver()
        data_saver.save_access_log_list(access_log_list)

    # get data from sqlite database
    data_loader = DataLoader()
    user_ip_list = data_loader.get_users_from_access_log()

    # create Sessions from AccessLogs

    session_builder = UserSessionBuilder()
    session_builder.create_user_sessions(user_ip_list)

