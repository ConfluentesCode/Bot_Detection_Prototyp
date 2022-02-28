from DatabaseConnector.Services.DataLoader import DataLoader
from DatabaseConnector.Services.DataSaver import DataSaver
from DetectionApproach.MarkovChain.MarkovChainTester import MarkovChainTester
from DetectionApproach.MarkovChain.MarkovChainTrainer import MarkovChainTrainer
from DetectionApproach.Services.KFoldCrossValidator import KFoldCrossValidator
from DetectionApproach.Services.ScoringParametersCalculator import ScoringParametersCalculator

if __name__ == '__main__':
    kfold = KFoldCrossValidator()
    chain_trainer = MarkovChainTrainer()
    chain_tester = MarkovChainTester()
    parameter_calculator = ScoringParametersCalculator()
    data_loader = DataLoader()
    data_saver = DataSaver()
    fold_group_id = 0

    all_session_ids = data_loader.get_all_session_ids()

    kfold_sets = kfold.split_session_ids_in_k_fold(10, all_session_ids)

    for kfold_set in kfold_sets:
        fold_group_id += 1
        train_set = kfold_set[0]
        test_set = kfold_set[1]

        split_list = chain_trainer.group_ids_in_bot_and_human(train_set)

        human_train_ids = split_list[0]
        bot_train_ids = split_list[1]

        human_chain = chain_trainer.train_chain(human_train_ids)
        bot_chain = chain_trainer.train_chain(bot_train_ids)

        chain_tester.test_trained_chain(fold_group_id, human_chain, bot_chain, test_set)

        parameter_calculator.calculate_scoring_parameters('MarkovChain', fold_group_id)


