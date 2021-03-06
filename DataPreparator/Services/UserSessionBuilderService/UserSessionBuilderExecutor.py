import datetime
from DataPreparator.Services.UserSessionBuilderService.UserSessionBuilder import UserSessionBuilder
from DatabaseConnector.Services.DataLoader import DataLoader

if __name__ == '__main__':
    print('start Session-Builder', datetime.datetime.now())

    # get data from sqlite database
    data_loader = DataLoader()
    user_ip_list = data_loader.get_users_from_access_log()
    print('get user list', datetime.datetime.now())


    # create Sessions from AccessLogs

    session_builder = UserSessionBuilder()
    session_builder.create_user_sessions(user_ip_list)
    print('build sessions', datetime.datetime.now())

    print('end Session-Builder', datetime.datetime.now())