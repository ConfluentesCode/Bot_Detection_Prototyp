from sklearn.model_selection import KFold


class KFoldCrossValidator:

    @staticmethod
    def split_session_ids_in_k_fold(number_of_splits, session_id_list):
        kfold = KFold(n_splits=number_of_splits)
        kfold_test_set_list = []

        for train_index_array, test_index_array in kfold.split(session_id_list):

            train_index = train_index_array.tolist()
            test_index = test_index_array.tolist()

            train_ids = [x + 1 for x in train_index]
            test_ids = [x + 1 for x in test_index]

            kfold_test_set_list.append(tuple((train_ids, test_ids)))

        return kfold_test_set_list
