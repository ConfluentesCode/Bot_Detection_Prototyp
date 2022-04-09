from DatabaseConnector.Services.DataLoader import DataLoader
from DetectionApproach.MarkovChain.Chain import Chain
import matplotlib.pyplot as plt
from datetime import datetime

markov_chain = Chain()
data_loader = DataLoader()

print('Start at', datetime.now())
print('Get all Bot Session Ids.')
bot_session_ids = data_loader.get_all_bot_session_ids()
print('Get Bot Pattern')
bot_training_pattern = data_loader.get_request_pattern(bot_session_ids)
print('Train Chain')
bot_start_vector, bot_transition_matrix = markov_chain.build(bot_training_pattern)

print('Bot Matrix')
for row in bot_transition_matrix: print(' '.join('{0:.2f}'.format(value) for value in row))
print('----------------')

plt.imshow(bot_transition_matrix, cmap=plt.cm.Blues, interpolation='nearest')
x = ['TEX', 'WEB', 'IMG', 'DOC', 'AV', 'PRO', 'COM', 'MAL', 'NOE']
y = ['TEX', 'WEB', 'IMG', 'DOC', 'AV', 'PRO', 'COM', 'MAL', 'NOE']
plt.xticks(range(len(x)), x, fontsize=12)
plt.yticks(range(len(y)), y, fontsize=12)
plt.colorbar()
plt.show()

print('Get all Human Session Ids.')
human_session_ids = data_loader.get_all_human_session_ids()
print('Get Human Pattern')
human_training_pattern = data_loader.get_request_pattern(human_session_ids)
print('Train Chain')
human_start_vector, human_transition_matrix = markov_chain.build(human_training_pattern)

print('Human Matrix')
for row in human_transition_matrix: print(' '.join('{0:.2f}'.format(value) for value in row))

plt.imshow(human_transition_matrix, cmap=plt.cm.Blues, interpolation='nearest')
x = ['TEX', 'WEB', 'IMG', 'DOC', 'AV', 'PRO', 'COM', 'MAL', 'NOE']
y = ['TEX', 'WEB', 'IMG', 'DOC', 'AV', 'PRO', 'COM', 'MAL', 'NOE']
plt.xticks(range(len(x)), x, fontsize=12)
plt.yticks(range(len(y)), y, fontsize=12)
plt.colorbar()
plt.show()
print('End at', datetime.now())
