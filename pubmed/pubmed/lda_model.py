import pandas as pd

# x: 'name': 'value': xxx, category:

def read_lda_model():
    lda_model = pd.read_json('/Users/marong/Desktop/big_data_project/pubmed/lda_model_1211.json')
    data = []

    topics = ['brain radiology', 'cancer caused by viruses', 'breast cancer', 'cell', 'patients\' survival rate',
              'liver cancer', 'melanoma', 'genetic profiling', 'chemotherapy', 'prostate cancer']

    for i in range(len(lda_model['test'])):
        topic = topics[i]
        for x in range(len(lda_model['test'][i])):
            top = {}
            top['x'] = lda_model['test'][i][x]
            top['value'] = lda_model['weight'][i][x]
            top['category'] = topic
            data.append(top)

    return data

