from DataPreparator.Enums.GroupAffiliation import GroupAffiliation
from DatabaseConnector.Services.DataLoader import DataLoader
from DetectionApproach.MarkovChain.Chain import Chain


class MarkovChainTrainer:
    markov_chain = Chain()
    data_loader = DataLoader()

    def train_chain(self, session_ids):
        training_pattern = self.data_loader.get_request_pattern(session_ids)
        chain = self.markov_chain.build(training_pattern)

        return chain

    def group_ids_in_bot_and_human(self, session_ids):
        human_set = []
        bot_set = []

        for session_id in session_ids:
            is_bot = self.data_loader.is_session_from_bot(session_id)

            if is_bot is True:
                bot_set.append(session_id)

            if is_bot is False:
                human_set.append(session_id)

        return human_set, bot_set
