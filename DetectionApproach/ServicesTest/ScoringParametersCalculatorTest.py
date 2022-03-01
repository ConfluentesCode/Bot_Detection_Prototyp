import unittest

from DetectionApproach.Services.ScoringParametersCalculator import ScoringParametersCalculator


class ScoringParametersCalculatorTest(unittest.TestCase):
    parameter_calculator = ScoringParametersCalculator()

    # False False
    true_negative = 10
    # True True
    true_positive = 15
    # False True
    false_positive = 20
    # True False
    false_negative = 25

    precision = 5

    recall = 10

    def test_if_precision_will_be_calculated_correctly(self):
        result = self.parameter_calculator.calculate_precision(self.true_positive, self.false_positive)

        self.assertEqual(result, 0.42857142857142855)

    def test_if_recall_will_be_calculated_correctly(self):
        result = self.parameter_calculator.calculate_recall(self.true_positive, self.false_negative)

        self.assertEqual(result, 0.375)

    def test_if_accuracy_will_be_calculated_correctly(self):
        result = self.parameter_calculator.calculate_accuracy(self.true_positive, self.false_negative,
                                                              self.true_negative, self.false_positive)

        self.assertEqual(result, 0.35714285714285715)

    def test_if_f1_will_be_calculated_correctly(self):
        result = self.parameter_calculator.calculate_f1(self.precision, self.recall)

        self.assertEqual(result, 6.666666666666667)
