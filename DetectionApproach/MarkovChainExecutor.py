from DetectionApproach.MarkovChain.MarkovChainTester import MarkovChainTester
from DetectionApproach.MarkovChain.MarkovChainTrainer import MarkovChainTrainer
from DetectionApproach.Services.ScoringParametersCalculator import ScoringParametersCalculator

if __name__ == '__main__':
    chain_trainer = MarkovChainTrainer()
    chain_tester = MarkovChainTester()
    parameter_calculator = ScoringParametersCalculator()

    human_chain = chain_trainer.train_human_chain()
    bot_chain = chain_trainer.train_bot_chain()

    chain_tester.test_trained_chain(human_chain, bot_chain)

    parameter_calculator.calculate_scoring_parameters('Markov Chain')
