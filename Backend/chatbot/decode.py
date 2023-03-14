#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 11:05:48 2023

@author: armsy326
"""
import os
import re
from analysis import get_shape, get_info, get_columns, yearly_reports,total_items_per_row
from predict import predict_for_years

###executes 5 major fucnctions for decoding the dataset

def data(query):
    
    clean_command = query.split()
    #print(clean_command[0])
    if clean_command[1] == 'shape':
        
        res = get_shape()
        
        return res
    
    elif clean_command[1] == 'info':
        
        #res = get_info()
        
        return "Failed to process, result for the moment.Try again later."
    
    elif clean_command[1] == 'columns':
        
        res = get_columns()
        
        return res
    
def predict(query):
    query = query.split()
    
    if query[2].isdigit():

        value = predict_for_years(query[2])
        return value
    else:

        return "Could not understand your query. To get prediction for  number of years,type something like 'predict for 2 years.'"
#doesnot work like expected 
def total(query):
    query = query.split()
    
    if query[2] == 'yearly':

        res = yearly_reports()

        return res
    
def allocation(query):

    split_query = query.split()
    print(split_query[2])
    try:
        res = total_items_per_row(f"{split_query[2]}")
        return res
    
    except Exception as e:
        
        return "Could not understand your query. To get prediction for  number of years,type something like 'Allocation in 201201'"
    
