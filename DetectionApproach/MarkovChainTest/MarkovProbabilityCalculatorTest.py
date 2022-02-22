import unittest

from DataPreparator.Enums.RequestType import RequestType
from DetectionApproach.MarkovChain.MarkovProbabilityCalculator import MarkovProbabilityCalculator


class MarkovProbabilityCalculatorTest(unittest.TestCase):
    calculator = MarkovProbabilityCalculator()

    def test_if_chain_calculate_probability_correctly(self):
        test_pattern = [RequestType.TEXT, RequestType.NOE, RequestType.DOC, RequestType.IMG, RequestType.WEB,
                        RequestType.IMG]
        test_chain = [[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                      [[0, 0, 0, 0, 0, 0, 0, 0.9, 0.1],
                       [0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5],
                       [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.2, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]]]

        result = self.calculator.calculate_pattern_probability(test_chain, test_pattern)

        self.assertEqual(0.008000000000000002, result)
