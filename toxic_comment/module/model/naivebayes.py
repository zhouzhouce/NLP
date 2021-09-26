import numpy as np
from sklearn.naive_bayes import MultinomialNB

class Naivebayes(object):
    def __init__(self):
        # initialize models for each class
        pass

    def fit(self, train_x, train_y):
        # fit models for each class using train_x and class_labels
        pass
    

    def predict(self, test_x):
        # calculate and return predictions for test_x using each model
        # here the predictions is a matrix of [test_x.row, classes.len]
        pass

    def predict_prob(self, test_x):
        # similar to the predict() method, calculate and return the probs for text_x using each model
        pass
