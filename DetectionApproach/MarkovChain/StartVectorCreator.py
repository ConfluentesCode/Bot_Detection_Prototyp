from DataPreparator.Enums.RequestType import RequestType
from DetectionApproach.Services.RequestTypeConverter import RequestTypeConverter


class StartVectorCreator:
    converter = RequestTypeConverter()

    def build(self, request_pattern_list):
        initial_state_list = self.get_first_states_of_transitions(request_pattern_list)
        start_vector = self.create_start_vector(initial_state_list)

        return start_vector

    @staticmethod
    def create_start_vector(state_list):
        vector_size = len([enum.value for enum in RequestType])
        start_vector = [0] * vector_size
        number_of_sessions = len(state_list)

        for request_type_value in state_list:
            start_vector[request_type_value] += 1

        start_vector[:] = [value / number_of_sessions for value in start_vector]

        return start_vector

    def get_first_states_of_transitions(self, pattern_list):
        initial_state_list = []

        for pattern in pattern_list:
            converted_pattern = self.converter.convert_request_pattern(pattern)
            first_state = converted_pattern[0]
            initial_state_list.append(first_state)

        return initial_state_list
