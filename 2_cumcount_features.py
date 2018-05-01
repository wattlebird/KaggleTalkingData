import pandas as pd
import numpy as np
from setting import *
import gc

gc.enable()

train = pd.read_csv(DATA + 'train/train.csv', dtype={
    'ip'            : 'uint32',
    'app'           : 'uint16',
    'device'        : 'uint16',
    'os'            : 'uint16',
    'channel'       : 'uint16',
    'is_attributed' : 'uint8',
    'click_id'      : 'uint32'
}, usecols=['ip', 'app', 'device', 'os', 'channel', 'hour', 'day'], engine='c')

test = pd.read_csv(DATA + 'train/test.csv', dtype={
    'ip'            : 'uint32',
    'app'           : 'uint16',
    'device'        : 'uint16',
    'os'            : 'uint16',
    'channel'       : 'uint16',
    'is_attributed' : 'uint8',
    'click_id'      : 'uint32'
}, usecols=['ip', 'app', 'device', 'os', 'channel', 'hour', 'day'], engine='c')

train = pd.concat([train, test])
del test

train['ip_ccos'] = train[['ip', 'os']].groupby('ip')['os'].cumcount()
train['ip_device_os_ccapp'] = train[['ip', 'device', 'os', 'app']].groupby(['ip', 'device', 'os'])['app'].cumcount()
train[['ip_ccos', 'ip_device_os_ccapp']].to_csv(DATA+'runtime/train/cumcount.csv', index=False)

test_gap = pd.read_csv(DATA + 'test/test_gap.csv', dtype={
    'ip'            : 'uint32',
    'app'           : 'uint16',
    'device'        : 'uint16',
    'os'            : 'uint16',
    'channel'       : 'uint16',
    'is_attributed' : 'uint8',
    'click_id'      : 'uint32'
}, usecols=['ip', 'app', 'device', 'os', 'channel', 'hour', 'day'], engine='c')

test = pd.read_csv(DATA + 'test/test.csv', dtype={
    'ip'            : 'uint32',
    'app'           : 'uint16',
    'device'        : 'uint16',
    'os'            : 'uint16',
    'channel'       : 'uint16',
    'is_attributed' : 'uint8',
    'click_id'      : 'uint32'
}, usecols=['ip', 'app', 'device', 'os', 'channel', 'hour', 'day'], engine='c')

train = pd.concat([train, test_gap, test])
del test, test_gap

train['ip_ccos'] = train[['ip', 'os']].groupby('ip')['os'].cumcount()
train['ip_device_os_ccapp'] = train[['ip', 'device', 'os', 'app']].groupby(['ip', 'device', 'os'])['app'].cumcount()
train[['ip_ccos', 'ip_device_os_ccapp']].to_csv(DATA+'runtime/test/cumcount.csv', index=False)