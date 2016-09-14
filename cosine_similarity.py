#!/usr/bin/env python
#-*- encoding: utf-8 -*-
from itertools import combinations
from math import sqrt
from rosette.api import API, DocumentParameters

import numpy as np

def post_text_embedding(
    content,
    language=None,
):
    api = API(user_key="[your key here]", service_url='https://stage.rosette.com/rest/v1/')
    params = DocumentParameters()
    params["content"] = content
    params["language"] = language
    return api.text_embedding(params)

def similarity(v1,v2):
    if not isinstance(v1, np.ndarray):
        v1 = np.array(v1)
    if not isinstance(v2, np.ndarray):
        v2 = np.array(v2)
    return np.divide(
        np.dot(v1, v2),
        sqrt(np.dot(v1,v1)) * sqrt(np.dot(v2,v2))
    )

def embedding(query):
    result = post_text_embedding(query, language='eng').get('embedding')
    if result:
        return np.array(result)
    else:
        return None

def compare(*queries):
    for q1, q2 in combinations(queries, 2):
        theta = similarity(embedding(q1), embedding(q2))
        print 'cos(θ)("{}", "{}"):'.format(q1, q2), theta.round(3)

def get_queries():
    for line in sys.stdin:
        if line:
            yield line.rstrip()

if __name__ == '__main__':
    queries = get_queries()
    compare(*queries)

