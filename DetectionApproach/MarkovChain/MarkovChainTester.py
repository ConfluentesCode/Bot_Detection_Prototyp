from DatabaseConnector.Services.DataLoader import DataLoader
from DatabaseConnector.Services.DataSaver import DataSaver
from DetectionApproach.MarkovChain.MarkovProbabilityCalculator import MarkovProbabilityCalculator
from DetectionApproach.Services.RequestTypeConverter import RequestTypeConverter


class MarkovChainTester:
    data_loader = DataLoader()
    data_saver = DataSaver()
    type_converter = RequestTypeConverter()
    probability_calculator = MarkovProbabilityCalculator()

    def test_trained_chain(self, human_chain, bot_chain):
        test_pattern_with_id_list = self.data_loader.get_session_ids_and_pattern_from_test_set()

        for test_pattern_with_id in test_pattern_with_id_list:
            test_result = self.compare_probabilities_of_session(human_chain, bot_chain, test_pattern_with_id)
            self.data_saver.save_test_result(test_result)

    def compare_probabilities_of_session(self, human_chain, bot_chain, test_pattern_with_id):
        session_id = test_pattern_with_id[0]
        request_pattern = test_pattern_with_id[1]

        human_prob = self.probability_calculator.calculate_pattern_probability(human_chain, request_pattern)
        bot_prob = self.probability_calculator.calculate_pattern_probability(bot_chain, request_pattern)

        if bot_prob > human_prob:
            return session_id, True

        if bot_prob < human_prob:
            return session_id, False

        return session_id, None

