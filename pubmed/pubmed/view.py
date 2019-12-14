from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from . import search_icd, search_author, cancer_info, lda_model
import json
from google.oauth2 import service_account
from django.views.decorators import csrf





key_word_pie = {}
def hello(request):
    context = {}
    context['content1'] = 'Hello World!'
    return render(request, 'index.html', context)

def icd(request):
    return render(request, 'ICD.html')



def icd_search(request):
    #   icd_result will return file_path, paired_result, CUI

    f_result = {'web': '', 'CUI': '', 'return_file': 'no', 'title': 'n', 'pubmed_id': 'n', 'error': 'n'}

    if request.POST:
        icd_code  = request.POST['q']
        icd_result = search_icd.search_icd(icd_code)
        if icd_result == None:
            f_result['error'] = 'y'
            return render(request, "ICD.html", f_result)
        f_result['CUI'] = icd_result['CUI']

        if 'http' in icd_result['file_path']:
            f_result['web'] = icd_result['file_path']

        else:
            file = pd.read_csv(icd_result['file_path'])
            f_result['title'] = json.dumps(file['title'].tolist())
            f_result['pubmed_id'] = json.dumps(file['pubmed_id'].tolist())
            f_result['return_file'] = 'yes'

    return render(request, "ICD.html", f_result)


def network(request):
    return render(request, 'authors.html')



def auth_search(request):
    context = {'nodes':'no', 'edges':'no', 'error':'false'}

    if request.POST:
        search_name = request.POST['network']
        try:
            nodes, edges = search_author.author_relationship(search_name)
            context['nodes'] = json.dumps(nodes)
            context['edges'] = json.dumps(edges)

        except:
            context['error'] = 'true'

    return render(request, 'authors.html', context)



def cancer(request):
    context = {}
    word, journal, literature, keyword_pie = cancer_info.cancer_info()
    context['word']= json.dumps(word)
    context['journal'] = json.dumps(journal)
    context['literature'] = json.dumps(literature)
    ld = lda_model.read_lda_model()
    context['lda'] = json.dumps(ld)
    key_word_pie['key_pie'] = json.dumps(keyword_pie)

    return render(request, 'cancer.html', context)



def keywords(request):
    return render(request, 'keywords.html', key_word_pie)
