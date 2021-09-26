import re
import string
import pandas as pd
import numpy as np  
    
    
class Preprocessor():
    def __init__(self):
        pass
        

    @staticmethod
    def clean_text(text):
        # clean text by converting text to all-lower-case, strip spaces, remove '\n'
        # split text into words using regular expression
        # create a filter_table that mapping all punctuation to None using str.maketrans() method
        # translate each word using filter_table to get clean_words, return clean_words
        pass
    

    def _parse(self, data_frame, is_test = False):
        # parse 'comment_text' into data set X by applying clean_text() method
        # for test set, data set Y is id columns, otherwise Y is the probs (by dropping 'id', comment_text', and first row?)
        
        # return X and Y data set tuple
        pass
    

    def _load_data(self):
        # load data set and pre-process "comment_text" column, fill empty cell in this column with 'unknown'
        
        
        # parse and split data set into train / validate data set (x, y separetely) using train_test_split() method,
        # 'split_ratio', 'random_seed'


        # load test set data and pre-process "comment_text" column, fill empty cell in this column with 'unknown'
        
        
        # parse test data?
        pass
        

    def process(self):
        # get 'input_convertor'
        # get data_x, data_y, train_x, train_y, validate_x, validate_y, test_x which are calculated in _load_data() method
        
        # if input_convertor is 'count_vectorization', vectorize train_x, validate_x using count_vectorization() method
        
        # return above data sets...
        pass
        

    def count_vectorization(self, train_x, validate_x, test_x):
        # calculate and return vectorized train_x, validate_x, test_x using 
        #    CountVectorizer(tokenizer, preprocessor), fit_transform(), transform() methods?
        
        # return train_x, validate_x, test_x
        pass
