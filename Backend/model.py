#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 12:21:53 2023

@author: armsy326
"""

import gensim
from gensim import corpora
from process import preprocess
from dataset import data,unknown_query_responses
import random


corpus  = []

accurate_queries = {}
threshold  = 0.5

def load_dataset():
    corpus.clear()
    for queries in data['questions']:
        cleaned_queries = preprocess(queries)
        corpus.append(cleaned_queries)

load_dataset()

###use simple preprocess

def process(sentence):
    accurate_queries.clear()
    cleaned_question = preprocess(sentence)
    sentence = gensim.utils.simple_preprocess(cleaned_question)
    token_corpus   =[gensim.utils.simple_preprocess(doc) for doc in corpus]

    ##create a dictionary #take corpus as an argument

    dictionary = corpora.Dictionary(token_corpus)

    #convert to bow

    sent_bow  = dictionary.doc2bow(sentence)
    corpus_bow = [dictionary.doc2bow(doc) for doc in token_corpus]


    #convert to tf-idf

    tfidf = gensim.models.TfidfModel(corpus_bow, dictionary=dictionary)

    sent_tfidf = tfidf[sent_bow]

    corpus_tfidf  = tfidf[corpus_bow]

    ##check similarity 

    similarity  = [gensim.matutils.cossim(sent_tfidf, doc) for doc in corpus_tfidf]

#filtered_sent  = [doc for sim,doc in zip(similarity, corpus) if sim >= 0.5]

    for sim,doc in zip(similarity, corpus):
        if sim >= threshold:
            accurate_queries[doc] = sim
    #sorting the dictionaries
    if len(accurate_queries) > 1:
        sorted_queries = sorted(accurate_queries.items(), key=lambda x: x[1], reverse=True)
        
        key_index  = corpus.index(sorted_queries[0][0])
        
        return data['answers'][key_index]
        
    elif len(accurate_queries) == 1: 
        key = list(accurate_queries.keys())[0]

        key_index  = corpus.index(key)
        
        return data['answers'][key_index]

    else:
        feedback = random.choice(unknown_query_responses)
        return feedback
