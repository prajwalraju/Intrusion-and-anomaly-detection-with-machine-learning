# About: predict.py
# Author: walid.daboubi@gmail.com
# Version: 2.0 - 2022/08/14

import argparse
import pickle

from utilities import *

# parser = argparse.ArgumentParser()
# parser.add_argument('-l', '--log_line', help = 'The log line you want to assess', required = True)
# parser.add_argument('-t', '--log_type', help = 'apache or nginx', required = True)
# parser.add_argument('-m', '--model', help = 'The trained model', required = True)

# args = vars(parser.parse_args())
def predict(log_line, log_type, model):
    url,encoded = encode_log_line(log_line,log_type,False)
    formatted_encoded = [encoded[feature] for feature in FEATURES]
    model = pickle.load(open(model, 'rb'))
    return model.predict([formatted_encoded])
