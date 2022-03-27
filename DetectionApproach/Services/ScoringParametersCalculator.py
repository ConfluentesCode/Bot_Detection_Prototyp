from DatabaseConnector.Services.DataLoader import DataLoader
from DatabaseConnector.Services.DataSaver import DataSaver


class ScoringParametersCalculator:
    data_loader = DataLoader()
    data_saver = DataSaver()

    def calculate_scoring_parameters(self, detection_approach, group_id):
        # False False
        true_negative = 0
        # True True
        true_positive = 0
        # False True
        false_positive = 0
        # True False
        false_negative = 0

        result_session_ids = self.data_loader.get_result_session_ids_from_group(group_id)

        for result_session_id in result_session_ids:
            decision_result = self.data_loader.get_ground_truth_and_decision(result_session_id)

            ground_truth_decision = decision_result[0]
            detection_decision = decision_result[1]

            if ground_truth_decision is None or detection_decision is None:
                continue

            if ground_truth_decision is False and detection_decision is False:
                true_negative += 1
            elif ground_truth_decision is True and detection_decision is True:
                true_positive += 1
            elif ground_truth_decision is False and detection_decision is True:
                false_positive += 1
            elif ground_truth_decision is True and detection_decision is False:
                false_negative += 1

        precision = self.calculate_precision(true_positive, false_positive)
        recall = self.calculate_recall(true_positive, false_negative)
        accuracy = self.calculate_accuracy(true_positive, false_negative, true_negative, false_positive)
        f1 = self.calculate_f1(precision, recall)

        self.data_saver.save_performance_parameter(detection_approach, precision, recall, accuracy, f1)

    @staticmethod
    def calculate_precision(true_positive, false_positive):
        try:
            return true_positive / (true_positive + false_positive)
        except ZeroDivisionError:
            return 0

    @staticmethod
    def calculate_recall(true_positive, false_negative):
        try:
            return true_positive / (true_positive + false_negative)
        except ZeroDivisionError:
            return 0

    @staticmethod
    def calculate_accuracy(true_positive, false_negative, true_negative, false_positive):
        try:
            return (true_positive + true_negative) / (true_positive + true_negative + false_positive + false_negative)
        except ZeroDivisionError:
            return 0

    @staticmethod
    def calculate_f1(precision, recall):
        try:
            return 2 * precision * recall / (precision + recall)
        except ZeroDivisionError:
            return 0
