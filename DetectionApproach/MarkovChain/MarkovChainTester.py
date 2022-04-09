from DatabaseConnector.Services.DataLoader import DataLoader
from DatabaseConnector.Services.DataSaver import DataSaver
from DetectionApproach.MarkovChain.MarkovProbabilityCalculator import MarkovProbabilityCalculator

class MarkovChainTester:
    data_loader = DataLoader()
    data_saver = DataSaver()
    probability_calculator = MarkovProbabilityCalculator()

    def test_trained_chain(self, group_id, human_chain, bot_chain, test_session_ids):
        test_pattern_with_id_list = self.data_loader.get_session_ids_and_pattern_from_id_list(test_session_ids)

        for test_pattern_with_id in test_pattern_with_id_list:
            test_result = self.compare_probabilities_of_session(human_chain, bot_chain, test_pattern_with_id)
            self.data_saver.save_test_result(group_id, test_result)

    def compare_probabilities_of_session(self, human_chain, bot_chain, test_pattern_with_id):
        session_id = test_pattern_with_id[0]
        request_pattern = test_pattern_with_id[1]

        human_prob = self.probability_calculator.calculate_pattern_probability(human_chain, request_pattern)
        bot_prob = self.probability_calculator.calculate_pattern_probability(bot_chain, request_pattern)

        if bot_prob > human_prob:
            return session_id, human_prob, bot_prob, True

        if bot_prob < human_prob:
            return session_id, human_prob, bot_prob, False

        return session_id, human_prob, bot_prob, None

