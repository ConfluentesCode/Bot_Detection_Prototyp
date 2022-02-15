from DetectionApproach.MarkovChain.StartVectorCreator import StartVectorCreator
from DetectionApproach.MarkovChain.TransitionMatrixCreator import TransitionMatrixCreator


class Chain:
    start_vector_creator = StartVectorCreator()
    transition_matrix_creator = TransitionMatrixCreator()

    def build(self, transitions):
        start_vector = self.start_vector_creator.build(transitions)
        transition_matrix = self.transition_matrix_creator.build(transitions)

        return start_vector, transition_matrix
