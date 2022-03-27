from DatabaseConnector.Services.DataLoader import DataLoader
from sklearn.model_selection import StratifiedKFold
import numpy as np


class StratifiedKFoldCrossValidator:
    data_loader = DataLoader()

    def split_session_ids_with_stratified_k_fold(self, split_number):
        kfold = StratifiedKFold(n_splits=split_number)
        session_id_list, ground_truth_list = self.data_loader.get_all_session_ids_with_ground_truth()
        stratified_kfold_test_set_list = []

        session_id_array = np.asarray(session_id_list)
        ground_truth_array = np.asarray(ground_truth_list)

        for train_index, test_index in kfold.split(session_id_array, ground_truth_array):
            session_ids_train, session_ids_test = session_id_array[train_index], session_id_array[test_index]

            stratified_kfold_test_set_list.append(tuple((session_ids_train.tolist(), session_ids_test.tolist())))

        return stratified_kfold_test_set_list



