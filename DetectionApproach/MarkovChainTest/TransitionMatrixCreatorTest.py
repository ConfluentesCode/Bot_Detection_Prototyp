import unittest

from DataPreparator.Enums.RequestType import RequestType
from DetectionApproach.MarkovChain.TransitionMatrixCreator import TransitionMatrixCreator


class TransitionMatrixCreatorTest(unittest.TestCase):
    creator = TransitionMatrixCreator()

    def test_if_empty_list_will_convert_correctly(self):
        emtpy_resource_pattern_list = []

        result = self.creator.request_pattern_converter(emtpy_resource_pattern_list)

        self.assertEqual(result, [])

    def test_if_one_request_pattern_will_convert_correctly(self):
        test_resource_pattern = [[RequestType.WEB, RequestType.NOE, RequestType.IMG, RequestType.NOE, RequestType.AV]]

        result = self.creator.request_pattern_converter(test_resource_pattern)

        self.assertEqual(result, [[1, 8, 2, 8, 4]])

    def test_if_list_of_request_pattern_will_convert_correctly(self):
        test_resource_pattern_list = [[RequestType.WEB, RequestType.NOE, RequestType.IMG],
                                      [RequestType.WEB, RequestType.NOE]]

        result = self.creator.request_pattern_converter(test_resource_pattern_list)

        self.assertEqual(result, [[1, 8, 2], [1, 8]])

    def test_if_transition_matrix_calculation_with_number_is_correct(self):
        test_transition = [
            [1, 1, 2, 6, 8, 5, 5, 7, 8, 8, 1, 1, 4, 5, 5, 0, 0, 0, 1, 1, 4, 4, 5, 1, 3, 3, 4, 5, 4, 1, 1]]
        expected_matrix = [[0.6666666666666666, 0.3333333333333333, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                           [0.0, 0.5, 0.125, 0.125, 0.25, 0.0, 0.0, 0.0, 0.0],
                           [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0],
                           [0.0, 0.2, 0.0, 0.0, 0.2, 0.6, 0.0, 0.0, 0.0],
                           [0.16666666666666666, 0.16666666666666666, 0.0, 0.0, 0.16666666666666666, 0.3333333333333333,
                            0.0, 0.16666666666666666, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
                           [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
                           [0.0, 0.3333333333333333, 0.0, 0.0, 0.0, 0.3333333333333333, 0.0, 0.0, 0.3333333333333333]]

        result = self.creator.create_transition_matrix(test_transition)

        self.assertEqual(result, expected_matrix)

    def test_if_transition_matrix_calculation_with_request_types_is_correct(self):
        request_pattern = [[RequestType.WEB, RequestType.NOE, RequestType.DOC],
                           [RequestType.IMG, RequestType.WEB, RequestType.IMG], [RequestType.DOC, RequestType.WEB]]
        expected_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5],
                           [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                           [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
        result = self.creator.build(request_pattern)

        self.assertEqual(result, expected_matrix)
