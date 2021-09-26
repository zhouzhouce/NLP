import os
import csv
import numpy as np
from sklearn.metrics import classification_report


class Predictor1(object):
    def __init__(self):
        pass

    def predict(self, test_x):
        pass

    def predict_prob(self, test_x):
        pass

    def save_result(self, test_ids, probs):
        # write result header, (test_ids x probs) into 'output_path' row by row
        # step 1: open or create a 'output_path' file with 'w' mode to write
        # step 2: write header into the file first using csv.writer(), header is 
        #        ['id','toxic','severe_toxic','obscene','threat','insult','identity_hate']
        # step 3: interately write each record of (test_ids x probs) into the file using writer.writerow() method
        pass
                 