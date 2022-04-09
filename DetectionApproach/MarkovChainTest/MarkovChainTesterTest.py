import unittest

from DataPreparator.Enums.RequestType import RequestType
from DetectionApproach.MarkovChain.MarkovChainTester import MarkovChainTester


class MarkovChainTesterTest(unittest.TestCase):
    chain_tester = MarkovChainTester()

    def test_if_chain_test_decide_correctly_by_equal_results(self):

        test_pattern = [1, [RequestType.TEXT, RequestType.NOE, RequestType.DOC, RequestType.IMG, RequestType.WEB,
                            RequestType.IMG]]

        test_human_chain = [[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                            [[0, 0, 0, 0, 0, 0, 0, 0.9, 0.1],
                             [0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5],
                             [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                             [0.0, 0.2, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]]]

        test_bot_chain = [[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                          [[0, 0, 0, 0, 0, 0, 0, 0.9, 0.1],
                           [0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5],
                           [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                           [0.0, 0.2, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]]]

        result = self.chain_tester.compare_probabilities_of_session(test_human_chain, test_bot_chain, test_pattern)

        result_id = result[0]
        result_decision = result[3]

        self.assertEqual(1, result_id)
        self.assertEqual(None, result_decision)

    def test_if_chain_test_decide_correctly_by_different_results(self):
        test_pattern = [1, [RequestType.TEXT, RequestType.NOE, RequestType.DOC, RequestType.IMG, RequestType.WEB,
                            RequestType.IMG]]

        test_human_chain = [[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                            [[0, 0, 0, 0, 0, 0, 0, 0.9, 0.1],
                             [0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5],
                             [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                             [0.0, 0.2, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]]]

        test_bot_chain = [[0.5, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                          [[0, 0, 0, 0, 0, 0, 0, 0.9, 0.5],
                           [0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5],
                           [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                           [0.0, 0.2, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0]]]

        result = self.chain_tester.compare_probabilities_of_session(test_human_chain, test_bot_chain, test_pattern)

        result_id = result[0]
        result_decision = result[3]

        self.assertEqual(1, result_id)
        self.assertEqual(True, result_decision)
