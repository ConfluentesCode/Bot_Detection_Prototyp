from sklearn.model_selection import KFold
from DatabaseConnector.Services.DataLoader import DataLoader
import numpy as np


class KFoldCrossValidator:
    data_loader = DataLoader()

    def split_session_ids_with_k_fold(self, number_of_splits):
        kfold = KFold(n_splits=number_of_splits)
        kfold_test_set_list = []

        session_id_list = self.data_loader.get_all_session_ids()

        session_id_array = np.asarray(session_id_list)

        for train_index, test_index in kfold.split(session_id_array):
            session_ids_train, session_ids_test = session_id_array[train_index], session_id_array[test_index]

            kfold_test_set_list.append(tuple((session_ids_train.tolist(), session_ids_test.tolist())))

        return kfold_test_set_list
