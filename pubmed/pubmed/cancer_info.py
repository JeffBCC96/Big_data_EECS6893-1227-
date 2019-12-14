import pandas as pd


def cancer_info():
    info_for_cancer = pd.read_json('/Users/marong/Desktop/big_data_project/pubmed/total_cancer.json')
    bg_color = ['rgba(226, 13, 13, 0.2)','rgba(87, 248, 87, 0.2)','rgba(153, 102, 255, 0.2)','rgba(255, 159, 64, 0.2)',
                'rgba(12, 19, 102, 0.2)','rgba(215, 78, 100, 0.2)','rgba(54, 29, 235, 0.2)','rgba(54, 162, 235, 0.2)',
                'rgba(50, 206, 86, 0.2)','rgba(75, 192, 192, 0.2)']
    #  data: {labels: [years], datasets: [{data: [], label: 'keyword', 'borderColor:xxx', fill:false}]}
    data = {'labels': [], 'datasets': []}
    data_for_journal = {'labels': [], 'datasets': []}
    literature_info = {'labels': [], 'datasets': [{'label': '# of published articles', 'data': [], 'backgroundColor':bg_color}]}
    journal_dict = {}
    key_dict = {}
    each_year_pie = {}
    total_keywords = set()
    total_journals = set()

    for year in info_for_cancer.keys():
        data['labels'].append(year)
        data_for_journal['labels'].append(year)
        literature_info['labels'].append(year)
        each_year_pie[year] = {'labels':[], 'datasets':[{'label': "#keywords", 'data': []}]}
        literature_info['datasets'][0]['data'].append(info_for_cancer[year]['total_articles'])
        key_dict[year] = {}
        journal_dict[year] = {}
        for keyword in info_for_cancer[year]['keywords']:
            key_name = keyword[0]
            total_keywords.add(key_name)
            each_year_pie[year]['labels'].append(key_name)
            each_year_pie[year]['datasets'][0]['data'].append(keyword[1])
            key_dict[year][key_name] = keyword[1] / info_for_cancer[year]['total_articles']

        for journal in info_for_cancer[year]['journal']:
            journal_name = journal[0]
            total_journals.add(journal[0])
            journal_dict[year][journal_name] = journal[1] / info_for_cancer[year]['total_articles']

    for key in total_keywords:
        key_info ={'fill': 'false', 'data':[]}
        key_info['label'] = key
        for year in key_dict.keys():
            try:
                key_info['data'].append(key_dict[year][key])
            except:
                key_info['data'].append(0)

        data['datasets'].append(key_info)

    for journal in total_journals:
        key_info = {'fill': 'false', 'data': []}
        key_info['label'] = journal
        for year in journal_dict.keys():
            try:
                key_info['data'].append(journal_dict[year][journal])
            except:
                key_info['data'].append(0)

        data_for_journal['datasets'].append(key_info)

    return data, data_for_journal, literature_info, each_year_pie



