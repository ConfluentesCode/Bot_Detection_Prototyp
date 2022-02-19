from sklearn.model_selection import train_test_split
from DatabaseConnector.Services.DataLoader import DataLoader
from DatabaseConnector.Services.DataSaver import DataSaver
from DataPreparator.Enums.GroupAffiliation import GroupAffiliation


class DataSplitter:
    data_loader = DataLoader()
    data_saver = DataSaver()

    def divide_into_test_and_training_set(self, bot_test_rate, human_test_rate):
        self.divide_bot_sessions_into_test_and_training_set(bot_test_rate)
        self.divide_human_sessions_into_test_and_training_set(human_test_rate)

    def divide_bot_sessions_into_test_and_training_set(self, test_rate):
        bot_session_id_list = self.data_loader.get_session_ids_from_sessions(True)

        bot_training_set, bot_test_set = train_test_split(bot_session_id_list, test_size=test_rate)

        self.save_training_set_group(bot_training_set)
        self.save_test_set_group(bot_test_set)

    def divide_human_sessions_into_test_and_training_set(self, test_rate):
        human_session_id_list = self.data_loader.get_session_ids_from_sessions(False)

        human_training_set, human_test_set = train_test_split(human_session_id_list, test_size=test_rate)

        self.save_training_set_group(human_training_set)
        self.save_test_set_group(human_test_set)

    def save_training_set_group(self, training_set):
        for training_session_id in training_set:
            self.data_saver.save_group_affiliation(training_session_id, GroupAffiliation.TRAINING)

    def save_test_set_group(self, test_set):
        for test_session_id in test_set:
            self.data_saver.save_group_affiliation(test_session_id, GroupAffiliation.TEST)
