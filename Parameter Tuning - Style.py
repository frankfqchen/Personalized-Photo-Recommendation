from src.parameter_tuning import *
from src.support_functions import *

samples = ['sample_data_1', 'sample_data_2', 'sample_data_3', 'sample_data_4', 'sample_data_5']
sample_data_list = load_samples(samples, data_folder='data')

model = 'StyleNN2'
metrics = ['P@K', 'R@K', 'RPrec', 'AvgP']
parameters = {
    'sim_method_r': 'cosine',
    'sim_method_p': 'euclidean',
    'id': 0
}

for i, sample_data in enumerate(sample_data_list):
    print('Dataset #' + str(i+1))
    parameters['id'] = i+1
    recsys = RecSys(model, sample_data)
    recsys.predict_all(**parameters)