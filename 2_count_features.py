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

train.groupby(['ip', 'app']).channel.count().rename('ip_app_nclick').to_frame().to_csv(DATA+'feature/train/ip_app_nclick.csv')
train.groupby(['ip', 'app', 'os']).channel.count().rename('ip_app_os_nclick').to_frame().to_csv(DATA+'feature/train/ip_app_os_nclick.csv')
train.groupby(['ip', 'app', 'os', 'device']).channel.count().rename('ip_app_os_device_nclick').to_frame().to_csv(DATA+'feature/train/ip_app_os_device_nclick.csv')
train.groupby(['ip', 'channel']).os.count().rename('ip_channel_nclick').to_frame().to_csv(DATA+'feature/train/ip_channel_nclick.csv')
train.groupby(['ip', 'hour', 'day']).channel.count().rename('ip_hour_day_nclick').to_frame().to_csv(DATA+'feature/train/ip_hour_day_nclick.csv')
train.groupby(['ip', 'hour', 'day', 'channel']).os.count().rename('ip_hour_day_channel_nclick').to_frame().to_csv(DATA+'feature/train/ip_hour_day_channel_nclick.csv')
train.groupby(['ip', 'hour', 'day', 'app']).os.count().rename('ip_hour_day_app_nclick').to_frame().to_csv(DATA+'feature/train/ip_hour_day_app_nclick.csv')
train.groupby(['ip', 'hour', 'day', 'app', 'channel']).os.count().rename('ip_hour_day_app_channel_nclick').to_frame().to_csv(DATA+'feature/train/ip_hour_day_app_channel_nclick.csv')

test = pd.read_csv(DATA + 'test/test.csv', dtype={
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

train.groupby(['ip', 'app']).channel.count().rename('ip_app_nclick').to_frame().to_csv(DATA+'feature/test/ip_app_nclick.csv')
train.groupby(['ip', 'app', 'os']).channel.count().rename('ip_app_os_nclick').to_frame().to_csv(DATA+'feature/test/ip_app_os_nclick.csv')
train.groupby(['ip', 'app', 'os', 'device']).channel.count().rename('ip_app_os_device_nclick').to_frame().to_csv(DATA+'feature/test/ip_app_os_device_nclick.csv')
train.groupby(['ip', 'channel']).os.count().rename('ip_channel_nclick').to_frame().to_csv(DATA+'feature/test/ip_channel_nclick.csv')
train.groupby(['ip', 'hour', 'day']).channel.count().rename('ip_hour_day_nclick').to_frame().to_csv(DATA+'feature/test/ip_hour_day_nclick.csv')
train.groupby(['ip', 'hour', 'day', 'channel']).os.count().rename('ip_hour_day_channel_nclick').to_frame().to_csv(DATA+'feature/test/ip_hour_day_channel_nclick.csv')
train.groupby(['ip', 'hour', 'day', 'app']).os.count().rename('ip_hour_day_app_nclick').to_frame().to_csv(DATA+'feature/test/ip_hour_day_app_nclick.csv')
train.groupby(['ip', 'hour', 'day', 'app', 'channel']).os.count().rename('ip_hour_day_app_channel_nclick').to_frame().to_csv(DATA+'feature/test/ip_hour_day_app_channel_nclick.csv')
