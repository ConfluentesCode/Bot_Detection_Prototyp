import unittest
from DetectionApproach.MarkovChain.StartVectorCreator import StartVectorCreator
from DataPreparator.Enums.RequestType import RequestType


class StartVectorCreatorTest(unittest.TestCase):
    vector_creator = StartVectorCreator()

    def test_if_start_vector_will_calculate_correctly(self):
        list_of_request_patterns = [[RequestType.TEXT, RequestType.NOE, RequestType.NOE],
                                    [RequestType.TEXT, RequestType.NOE], [RequestType.WEB], [RequestType.IMG],
                                    [RequestType.DOC, RequestType.NOE], [RequestType.AV, RequestType.NOE],
                                    [RequestType.PROG], [RequestType.COMPRESSED, RequestType.NOE],
                                    [RequestType.MALFORMED], [RequestType.NOE, RequestType.NOE]]

        expected_start_vector = [0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

        result = self.vector_creator.build(list_of_request_patterns)

        self.assertEqual(expected_start_vector, result)



