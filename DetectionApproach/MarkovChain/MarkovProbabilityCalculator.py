import numpy

from DetectionApproach.Services.ProcessHelperService.RequestTypeConverter import RequestTypeConverter


class MarkovProbabilityCalculator:
    type_converter = RequestTypeConverter()

    def calculate_pattern_probability(self, markov_chain, request_pattern):
        transition_probability_list = []
        start_vector = markov_chain[0]

        start_probability = self.get_start_probability(start_vector, request_pattern)

        transition_probability_list.append(start_probability)

        transition_matrix = markov_chain[1]

        transition_probability_list = self.get_transition_probabilities(transition_probability_list, transition_matrix,
                                                                        request_pattern)

        transition_probability = numpy.prod(transition_probability_list)

        return transition_probability

    def get_start_probability(self, start_vector, request_pattern):
        converted_request_pattern = self.type_converter.convert_request_pattern(request_pattern)

        start_probability = start_vector[converted_request_pattern[0]]

        return start_probability

    def get_transition_probabilities(self, transition_probability_list, transition_matrix, request_pattern):
        converted_request_pattern = self.type_converter.convert_request_pattern(request_pattern)

        for (i, j) in zip(converted_request_pattern, converted_request_pattern[1:]):
            value = transition_matrix[i][j]
            transition_probability_list.append(value)

        return transition_probability_list
