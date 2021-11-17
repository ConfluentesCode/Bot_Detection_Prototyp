from Constants import Constants
from Services.AccessLogReader import AccessLogReader
from Services.DataSaver import DataSaver

file_path = Constants.ACCESS_LOG_FILE_PATH

if __name__ == '__main__':
    # get information from access logs
    file_reader = AccessLogReader()
    access_log_list = file_reader.read_csv_file(file_path)

    # write information in sqlite database
    data_saver = DataSaver()
    data_saver.save_access_logs(access_log_list)

    print('test')
