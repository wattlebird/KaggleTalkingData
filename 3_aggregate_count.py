import pandas as pd
import numpy as np
from setting import *
import gc

gc.enable()

dtype={
    'ip'            : 'uint32',
    'app'           : 'uint16',
    'device'        : 'uint16',
    'os'            : 'uint16',
    'channel'       : 'uint16',
    'hour'          : 'uint8',
    'click_id'      : 'uint32',
    'ip_app_nclick' : 'uint32',
    'ip_app_os_nclick': 'uint32',
    'ip_app_os_device_nclick': 'uint32',
    'ip_channel_nclick': 'uint32', 
    'ip_hour_day_nclick': 'uint32',
    'ip_hour_day_channel_nclick': 'uint32',
    'ip_hour_day_app_nclick': 'uint32', 
    'ip_hour_day_app_channel_nclick': 'uint32'
}

train = pd.read_csv(DATA + 'train/train.csv', dtype=dtype, 
usecols=['ip', 'app', 'device', 'os', 'channel', 'is_attributed', 'hour', 'day'], engine='c')

c1 = pd.read_csv(DATA+'feature/train/ip_app_nclick.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'app'])
del c1

c1 = pd.read_csv(DATA+'feature/train/ip_app_os_nclick.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'app', 'os'])
del c1

c1 = pd.read_csv(DATA+'feature/train/ip_app_os_device_nclick.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'app', 'os', 'device'])
del c1

c1 = pd.read_csv(DATA+'feature/train/ip_channel_nclick.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'channel'])
del c1

c1 = pd.read_csv(DATA+'feature/train/ip_hour_day_nclick.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'hour', 'day'])
del c1

c1 = pd.read_csv(DATA+'feature/train/ip_hour_day_channel_nclick.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'hour', 'day', 'channel'])
del c1

c1 = pd.read_csv(DATA+'feature/train/ip_hour_day_app_nclick.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'hour', 'day', 'app'])
del c1

c1 = pd.read_csv(DATA+'feature/train/ip_hour_day_app_channel_nclick.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'hour', 'day', 'app', 'channel'])
del c1

train.to_csv(DATA+'train/train_withcount.csv', index=False)

test = pd.read_csv(DATA + 'train/test.csv', dtype=dtype, 
usecols=['ip', 'app', 'device', 'os', 'channel', 'is_attributed', 'hour', 'day'], engine='c')

c1 = pd.read_csv(DATA+'feature/train/ip_app_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app'])
del c1

c1 = pd.read_csv(DATA+'feature/train/ip_app_os_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'os'])
del c1

c1 = pd.read_csv(DATA+'feature/train/ip_app_os_device_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'os', 'device'])
del c1

c1 = pd.read_csv(DATA+'feature/train/ip_channel_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'channel'])
del c1

c1 = pd.read_csv(DATA+'feature/train/ip_hour_day_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'hour', 'day'])
del c1

c1 = pd.read_csv(DATA+'feature/train/ip_hour_day_channel_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'hour', 'day', 'channel'])
del c1

c1 = pd.read_csv(DATA+'feature/train/ip_hour_day_app_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'hour', 'day', 'app'])
del c1

c1 = pd.read_csv(DATA+'feature/train/ip_hour_day_app_channel_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'hour', 'day', 'app', 'channel'])
del c1

test.to_csv(DATA+'train/test_withcount.csv', index=False)
del test


test = pd.read_csv(DATA + 'test/test.csv', dtype=dtype, 
usecols=['ip', 'app', 'device', 'os', 'channel', 'click_id', 'hour', 'day'], engine='c')

c1 = pd.read_csv(DATA+'feature/test/ip_app_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app'])
del c1

c1 = pd.read_csv(DATA+'feature/test/ip_app_os_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'os'])
del c1

c1 = pd.read_csv(DATA+'feature/test/ip_app_os_device_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'os', 'device'])
del c1

c1 = pd.read_csv(DATA+'feature/test/ip_channel_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'channel'])
del c1

c1 = pd.read_csv(DATA+'feature/test/ip_hour_day_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'hour', 'day'])
del c1

c1 = pd.read_csv(DATA+'feature/test/ip_hour_day_channel_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'hour', 'day', 'channel'])
del c1

c1 = pd.read_csv(DATA+'feature/test/ip_hour_day_app_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'hour', 'day', 'app'])
del c1

c1 = pd.read_csv(DATA+'feature/test/ip_hour_day_app_channel_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'hour', 'day', 'app', 'channel'])
del c1

test.to_csv(DATA+'test/test_withcount.csv', index=False)