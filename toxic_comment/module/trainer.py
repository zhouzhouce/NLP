
class Trainer1(object):
    def __init__(self):
        pass
        

    def _create_model(self, classes):
        # create a Naivebayes model using classes if 'model_name' is 'naivebayes'
        # otherwise, log warning unsupported model
        pass
            

    def metrics(self, predictions, labels):
        # calculate and return accuracy_score and classification_report using labels & predictions
        pass
        
        
    def fit(self, train_x, train_y):
        # fit model using train_x and train_y, and then return the model
        pass
    

    def validate(self, validate_x, validate_y):
        # predict the validate_x using naivebayes model and then calculate/return the metrics comparing validate_y?
        pass
    