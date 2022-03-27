import unittest

from DetectionApproach.Services.KFoldCrossValidator import KFoldCrossValidator


# TODO fix test -> DB-Mock
class KFoldCrossValidatorTest(unittest.TestCase):
    cross_validator = KFoldCrossValidator()

    def test_if_sequence_will_split_correctly(self):
        test_session_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        number_of_folds = 10

        expected_split = [([2, 3, 4, 5, 6, 7, 8, 9, 10], [1]),
                          ([1, 3, 4, 5, 6, 7, 8, 9, 10], [2]),
                          ([1, 2, 4, 5, 6, 7, 8, 9, 10], [3]),
                          ([1, 2, 3, 5, 6, 7, 8, 9, 10], [4]),
                          ([1, 2, 3, 4, 6, 7, 8, 9, 10], [5]),
                          ([1, 2, 3, 4, 5, 7, 8, 9, 10], [6]),
                          ([1, 2, 3, 4, 5, 6, 8, 9, 10], [7]),
                          ([1, 2, 3, 4, 5, 6, 7, 9, 10], [8]),
                          ([1, 2, 3, 4, 5, 6, 7, 8, 10], [9]),
                          ([1, 2, 3, 4, 5, 6, 7, 8, 9], [10])]

        result = self.cross_validator.split_session_ids_with_k_fold(number_of_folds)

        self.assertEqual(result, expected_split)
