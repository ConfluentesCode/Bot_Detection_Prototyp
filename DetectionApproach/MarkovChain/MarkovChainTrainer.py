from DataPreparator.Enums.GroupAffiliation import GroupAffiliation
from DatabaseConnector.Services.DataLoader import DataLoader
from DetectionApproach.MarkovChain.Chain import Chain


class MarkovChainTrainer:
    markov_chain = Chain()
    data_loader = DataLoader()

    def train_human_chain(self):
        human_training_pattern = self.data_loader.get_request_pattern(False, GroupAffiliation.TRAINING)
        human_chain = self.markov_chain.build(human_training_pattern)

        return human_chain

    def train_bot_chain(self):
        bot_training_pattern = self.data_loader.get_request_pattern(True, GroupAffiliation.TRAINING)
        bot_chain = self.markov_chain.build(bot_training_pattern)

        return bot_chain
