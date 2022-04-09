from DetectionApproach.Services.ProcessHelperService.RequestTypeConverter import RequestTypeConverter


class TransitionMatrixCreator:
    converter = RequestTypeConverter()

    def build(self, request_pattern_list):
        integer_request_pattern = self.request_pattern_converter(request_pattern_list)
        transition_matrix = self.create_transition_matrix(integer_request_pattern)

        return transition_matrix

    # in manner of https://stackoverflow.com/questions/46657221/generating-markov-transition-matrix-in-python/46657489
    def create_transition_matrix(self, transitions):
        number_of_states = self.get_number_of_states(transitions)

        matrix = [[0] * number_of_states for _ in range(number_of_states)]

        for transition_pattern in transitions:
            for (i, j) in zip(transition_pattern, transition_pattern[1:]):
                matrix[i][j] += 1

        for row in matrix:
            row_sum = sum(row)
            if row_sum > 0:
                row[:] = [cell_sum / row_sum for cell_sum in row]
        return matrix

    @staticmethod
    def get_number_of_states(transitions):
        global_number_of_states = 0

        for number_list in transitions:
            number_of_states = 1 + max(number_list)

            if number_of_states > global_number_of_states:
                global_number_of_states = number_of_states

        return global_number_of_states

    def request_pattern_converter(self, request_pattern_list):
        converted_resource_pattern_list = []

        for resource_pattern in request_pattern_list:
            converted_resource_pattern = self.converter.convert_request_pattern(resource_pattern)

            converted_resource_pattern_list.append(converted_resource_pattern)

        return converted_resource_pattern_list

    @staticmethod
    def matrix_printer(matrix):
        for row in matrix: print(' '.join('{0:.2f}'.format(value) for value in row))
