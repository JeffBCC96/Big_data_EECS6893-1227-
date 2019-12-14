from google.oauth2 import service_account

import pandas_gbq

credentials = service_account.Credentials.from_service_account_file('/Users/marong/Desktop/big_data_project/pubmed/bigdata-d7b584548bdd.json')


# search author
# SELECT * FROM `bigdata-259800.authorinfo.author_edges` where lower(source) like '%laila%a%' LIMIT 1000

# top authors :
# Institute
# the Fred Hutchinson Cancer Research Center, Seattle (D.D., T.S., E.W., L.E.)
# FHI 360, Durham, NC (A.M., S.G., N.D.S.)

# Person
# Heinz-Josef Lenz, MD, University of Southern California, Los Angeles, CA      3824
# Rachel Tam, PhD and Shilpi Mahajan, PhD, Genentech, South San Francisco, CA     3824
# Charles David Blanke, MD, Oregon Health and Science University Hospital, Portland 3824



def author_relationship(name):
    pandas_gbq.context.credentials = credentials
    pandas_gbq.context.project = "bigdata-259800"

    nodes_info = {}
    nodes, edges = [], []
    p_name = name.split(' ')
    name = ''.join(['%' + i for i in p_name]) + '%'
    # print(name)

    SQL = f"SELECT * FROM `bigdata-259800.authorinfo.author_edges` where lower(source) like '%{name.lower()}%' limit 200"
    df = pandas_gbq.read_gbq(SQL)

    # print(df)
    au_info = df.source[0].split('-')
    source_node = au_info[0]
    try:
        contact_info = ''.join(au_info[1:])
    except:
        contact_info = ''

    nodes_info[source_node] = {'id': 0, 'num': 0, 'info': contact_info}

    error_symbol = ['none', '@', 'and', 'or']

    for i in range(len(df.target)):
        current_node = df.target[i]
        split_info = current_node.split('-')
        node_name = split_info[0]

        if True in [True for i in error_symbol if i in node_name.lower()]: continue
        if len(split_info) > 1:
            c_info = ' '.join(split_info[1:])
        else:
            c_info = ''

        try:
            nodes_info[node_name]['num'] += 1
        except:
            nodes_info[node_name] = {'id': i+1, 'num': 1, 'info':c_info}

    for i in nodes_info.keys():
        if i == source_node:
            title = 'Contact info: ' + nodes_info[i]['info'] + '\n;' + '# Friends: ' + str(len(nodes_info.keys()) - 1)
        else:
            title = 'Contact info: ' + nodes_info[i]['info']

        nodes.append({'id':nodes_info[i]['id'], 'label': i, 'title': title})

        if i != source_node:
            edges.append({'from': 0, 'to': nodes_info[i]['id'], 'width': nodes_info[i]['num'],
                          'label': str(nodes_info[i]['num']), 'font': {'size': 0}})
    return nodes, edges

