import yaml
import logging
import argparse
from module import Preprocessor, Trainer, Predictor

            
if __name__ == "__main__":
    # build customized command line using argparse.ArgumentParser
    # add arguments '--config' & '--log_level'
    # execute the parser
    
    
    # handle log, FORMAT, logging.basicConfig(), get logger
    logger = None

   
    # open config file, try....
    with open("./config/config.yaml", 'r') as config_file:
        try:
            # 1) load config file
            
            # 2) create preprocessor and pro-process the data set into data_x, data_y, train_x, train_y, validate_x, validate_y, test_x
            
            # 3) create trainer
            # fit train_x, traint_y
            
            # validate the validate data set and get the accuracy & classification report by validating the data
            # log accuracy & cls_report
            # train the model
            
            # 4)create predictor
            # predict the probabilty and save results
            pass
            
        except:
            pass  