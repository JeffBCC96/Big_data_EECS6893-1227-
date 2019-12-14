# UMLS API requires getting TGT every 8 hours: https://documentation.uts.nlm.nih.gov/rest/authentication.html
# Or just get every run (below)
import getpass
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import os
from os import path


headers = {"Content-Type": "application/x-www-form-urlencoded"}

# user = input("Please enter your username: ")
# pw = getpass.getpass("Please enter your password: ")
user = 'jeffma'
pw = 'Mr13812283066'

params = {"username": user,
         "password" : pw}

TGT_URL = "https://utslogin.nlm.nih.gov/cas/v1/tickets"

response = (requests.post(TGT_URL, headers = headers, params = params)).text
ticketgetter = BeautifulSoup(response, 'lxml')
TGT = ticketgetter.form['action']


# icd-query     # ICD10: Cauda equina syndrome; Brain Injuries Traumatic
def search_icd(icd):
    """
        return dict {CUI,file_path, paired_results}

    """

    # request info
    f_search = {'paired_results': {}, 'file_path': ''}
    headers_ST = {"Content-Type": "application/x-www-form-urlencoded"}
    params = {"service": "http://umlsks.nlm.nih.gov"}

    # search the query
    queryString = icd
    ST = requests.post(TGT, headers=headers_ST, params=params)
    URL = "https://uts-ws.nlm.nih.gov/rest/search/current?string={}&ticket={}".format(queryString, ST.text)
    response = requests.get(URL)
    j = json.loads(response.text)


    # parse cui & select the first cui

        # TODO we can keep searching the cui, until finding the most accurate one.
    try:
        mth_cui = []
        for i in j['result']['results']:
            if i['rootSource'] == 'MTH':
                mth_cui.append((i['ui'], i['name']))

        CUI = mth_cui[0][0]
        f_search['CUI'] = CUI

        ST = requests.post(TGT, headers=headers_ST, params=params)
        URL_cui = "https://uts-ws.nlm.nih.gov/rest/content/current/CUI/{}/atoms?sabs=ICD10CM,MSH&ticket={}".format(CUI,
                                                                                                                   ST.text)
        response_2 = requests.get(URL_cui)
        r2 = json.loads(response_2.text)

    except:
        return None



    # find related files
    Mesh_terms = []
    icd_terms = []
    found_file = 'Sorry, we can not find the local files'

    for atom in r2['result']:
        if atom['rootSource'] == 'MSH':
            for i in r2['result']:
                if i['rootSource'] == 'ICD10CM':
                    Mesh_terms.append(atom["name"])
                    icd_terms.append(i["name"])


    # Print all the matched pairs
    paired_results = list(zip(Mesh_terms, icd_terms))
    # print(f'Here we found {len(paired_results)} paired results')
    for i, v in enumerate(paired_results):
        # print(f'Matched: ICD10CM({v[1]}) ---> MeSH({v[0]})')
        f_search['paired_results'][i] = 'ICD10: ' + v[1] + ' with MeSH :' + v[0]
        # f_search['paired_results'][i] = f'Matched: ICD10CM({v[1]}) with MeSH({v[0]})'

    # return the files for the required Mesh terms
    for item in paired_results:
        mesh_path = ' '.join(item[0].split(',')) + '.csv'
        try:
            found_file = pd.read_csv(os.path.join('/Users/marong/Desktop/big_data_project/Mesh_terms', mesh_path))
            f_search['file_path'] = os.path.join('/Users/marong/Desktop/big_data_project/Mesh_terms', mesh_path)
            break
        except:
            pass
            # print(f'MeSH term: {mesh_path} not_found')

    if f_search['file_path'] == '':
        if paired_results:
            f_search['file_path'] = f"https://www.ncbi.nlm.nih.gov/pubmed/?term={'+'.join(paired_results[0][0].split(' '))}"
        else:
            f_search['file_path'] = f"https://www.ncbi.nlm.nih.gov/pubmed/?term={'+'.join(queryString.split(' '))}"

    return f_search

