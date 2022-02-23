from DataPreparator.Constants import PathConstants
from DataPreparator.Services.AccessLogReader import AccessLogReader
from DatabaseConnector.Services.DataSaver import DataSaver

file_path = PathConstants.ACCESS_LOG_FILE_PATH

if __name__ == '__main__':
    print('start proto-typ')

    # get information from access logs
    file_reader = AccessLogReader()
    access_log_list = file_reader.read_file(file_path)

    # write information from access log in sqlite database

    data_saver = DataSaver()
    data_saver.save_access_log_list(access_log_list)