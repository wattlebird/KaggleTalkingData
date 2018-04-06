import pandas as pd
import numpy as np
from setting import *
import datetime
import gc

train = pd.read_csv(DATA + 'train.csv', dtype={
    'ip'            : 'uint32',
    'app'           : 'uint16',
    'device'        : 'uint16',
    'os'            : 'uint16',
    'channel'       : 'uint16',
    'is_attributed' : 'uint8',
    'click_id'      : 'uint32'
}, usecols=['ip', 'app', 'device', 'os', 'channel', 'click_time', 'is_attributed'], parse_dates=[5], engine='c')
train['hour'] = train.click_time.dt.hour.astype('uint8')
train['day'] = train.click_time.dt.day.astype('uint8')
train = train[train.click_time >= datetime.datetime(2017, 11, 8, 4, 0, 0)][['is_attributed', 'ip', 'app', 'device', 'os', 'channel', 'hour', 'day', 'click_time']]
valid = train[train.click_time >= datetime.datetime(2017, 11, 9, 4, 0, 0)]
train = train[train.click_time < datetime.datetime(2017, 11, 9, 4, 0, 0)]
valid.sort_values(by='click_time').to_csv(DATA+'valid/valid.csv', index=False)
train.sort_values(by='click_time').to_csv(DATA+'train/train.csv', index=False)

del train, valid
gc.collect()

test = pd.read_csv(DATA + 'test.csv', dtype={
    'ip'            : 'uint32',
    'app'           : 'uint16',
    'device'        : 'uint16',
    'os'            : 'uint16',
    'channel'       : 'uint16',
    'is_attributed' : 'uint8',
    'click_id'      : 'uint32'
}, usecols=['click_id', 'ip', 'app', 'device', 'os', 'channel', 'click_time'])
test['hour'] = pd.to_datetime(test.click_time).dt.hour.astype('uint8')
test['day'] = pd.to_datetime(test.click_time).dt.day.astype('uint8')
test[['click_id', 'ip', 'app', 'device', 'os', 'channel', 'hour', 'day', 'click_time']].to_csv(DATA+'test/test.csv', index=False)