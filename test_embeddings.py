#!/usr/bin/env python
#-*- encoding: utf-8 -*-

from cosine_similarity import *

text_qs = {
    'Paris' : post_text_embedding('Paris', language='eng').get('embedding'),
    'France' : post_text_embedding('France', language='eng').get('embedding'),
    'London' : post_text_embedding('London', language='eng').get('embedding'),
    'England' : post_text_embedding('England', language='eng').get('embedding')
}

def test(d):
    for q1, q2 in combinations(d.keys(), 2):
        theta = similarity(d[q1], d[q2])
        print 'θ("{}", "{}"):'.format(q1, q2), theta.round(3)

if __name__ == '__main__':
    test(text_qs)
    print 'θ("{}", "{}") > θ("{}", "{}") ?'.format('Paris', 'France', 'London', 'France'), similarity(text_qs['Paris'], text_qs['France']) > similarity(text_qs['London'], text_qs['France'])
    print 'θ("{}", "{}") > θ("{}", "{}") ?'.format('England', 'London', 'England', 'France'), similarity(text_qs['England'], text_qs['London']) > similarity(text_qs['England'], text_qs['France'])
    print '-' * 80