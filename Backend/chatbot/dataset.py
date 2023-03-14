#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:21:53 2023

@author: armsy326
"""
import time
import numpy as np
salutations = [
              "hello",
              "hi",   
              "yoo", 
              "hey",    
              "good morning",    
              "good evening", 
              "good afternoon"]

salutation_feedback = [    
  "Hello! What can I help you with?",    
  "Hi! What would you like to know?",    
  "Hey! How can I assist you today?",    
  "Good morning/afternoon/evening! What can I help you with?",    
  "Greetings! Is there something specific you would like to know?"]

salutations1 = ["bye", "goodbye", "good bye","see you later"]

salutation_feedback1 = [
  "See you later, thanks for visiting", 
  "Have a nice day", 
  "Bye! Come back again soon."]




unknown_query_responses = [       
                  "I'm sorry, but I only have the information you give me.",    
                  "I'm sorry, I'm not a genius, just a highly advanced robot.",    
                  "I'm sorry, my database is vast, but not infinite.", 
                  "I'm sorry, I don't know the answer to that, but I'm sure Google does.",    
                  "I'm sorry, I'm just a computer program, not a philosopher.",    
                  "I'm sorry, I don't have all the answers, just most of them.",    
                  "I'm sorry, I'm not a psychic, just a highly educated AI.",
                  "I'm sorry, I don't have the answer to that. Maybe try asking a different source?",    
                 "Sorry, I couldn't find any information on that. Can you please provide more context?",    
                 "I'm sorry, I don't have the answer you're looking for. Maybe try rephrasing your question?",    
                 "Sorry, I'm not sure what you're asking. Can you please clarify?",    
                 "I'm sorry, but I don't have an answer for that. Perhaps try asking someone else?",    
                 "My apologies, I couldn't find any information on that topic. Could you try asking a different way?"
                  ]
