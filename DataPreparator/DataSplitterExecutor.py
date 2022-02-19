from DataPreparator.Services.DataSplitter import DataSplitter

if __name__ == '__main__':
    splitter = DataSplitter()
    bot_test_data_rate = 0.2
    human_test_data_rate = 0.2

    splitter.divide_into_test_and_training_set(bot_test_data_rate, human_test_data_rate)
