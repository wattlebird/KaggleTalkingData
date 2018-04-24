import numpy as np
from sklearn.metrics import roc_auc_score
import pandas as pd
from setting import *

y = pd.read_csv(DATA + 'train/test.csv', dtype={
    'ip'            : 'uint32',
    'app'           : 'uint16',
    'device'        : 'uint16',
    'os'            : 'uint16',
    'channel'       : 'uint16',
    'is_attributed' : 'uint8',
    'click_id'      : 'uint32'
}, usecols=['is_attributed'], engine='c')

yp = pd.read_csv(DATA+'train/test_prob.csv', header=None, engine='c')
print(roc_auc_score(y.is_attributed.values, yp.values))