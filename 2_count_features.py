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

#train.groupby(['ip', 'app']).channel.count().rename('ip_app_nclick').to_frame().to_csv(DATA+'feature/train/ip_app_nclick.csv')
#train.groupby(['ip', 'app', 'os']).channel.count().rename('ip_app_os_nclick').to_frame().to_csv(DATA+'feature/train/ip_app_os_nclick.csv')
#train.groupby(['ip', 'app', 'os', 'device']).channel.count().rename('ip_app_os_device_nclick').to_frame().to_csv(DATA+'feature/train/ip_app_os_device_nclick.csv')
#train.groupby(['ip', 'channel']).os.count().rename('ip_channel_nclick').to_frame().to_csv(DATA+'feature/train/ip_channel_nclick.csv')
#train.groupby(['ip', 'hour', 'day']).channel.count().rename('ip_hour_day_nclick').to_frame().to_csv(DATA+'feature/train/ip_hour_day_nclick.csv')
#train.groupby(['ip', 'hour', 'day', 'channel']).os.count().rename('ip_hour_day_channel_nclick').to_frame().to_csv(DATA+'feature/train/ip_hour_day_channel_nclick.csv')
#train.groupby(['ip', 'hour', 'day', 'app']).os.count().rename('ip_hour_day_app_nclick').to_frame().to_csv(DATA+'feature/train/ip_hour_day_app_nclick.csv')
train.groupby(['device', 'os']).os.count().rename('device_os_nclick').to_frame().to_csv(DATA+'feature/train/device_os_nclick.csv')
train.groupby(['channel', 'device', 'os']).os.count().rename('channel_device_os_nclick').to_frame().to_csv(DATA+'feature/train/channel_device_os_nclick.csv')
train.groupby(['app', 'device', 'os']).os.count().rename('app_device_os_nclick').to_frame().to_csv(DATA+'feature/train/app_device_os_nclick.csv')
train.groupby(['device', 'os', 'day', 'hour']).os.count().rename('device_os_hour_nclick').to_frame().to_csv(DATA+'feature/train/device_os_hour_nclick.csv')
train.groupby(['channel', 'day', 'hour']).os.count().rename('channel_hour_nclick').to_frame().to_csv(DATA+'feature/train/channel_hour_nclick.csv')

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

#train.groupby(['ip', 'app']).channel.count().rename('ip_app_nclick').to_frame().to_csv(DATA+'feature/test/ip_app_nclick.csv')
#train.groupby(['ip', 'app', 'os']).channel.count().rename('ip_app_os_nclick').to_frame().to_csv(DATA+'feature/test/ip_app_os_nclick.csv')
#train.groupby(['ip', 'app', 'os', 'device']).channel.count().rename('ip_app_os_device_nclick').to_frame().to_csv(DATA+'feature/test/ip_app_os_device_nclick.csv')
#train.groupby(['ip', 'channel']).os.count().rename('ip_channel_nclick').to_frame().to_csv(DATA+'feature/test/ip_channel_nclick.csv')
#train.groupby(['ip', 'hour', 'day']).channel.count().rename('ip_hour_day_nclick').to_frame().to_csv(DATA+'feature/test/ip_hour_day_nclick.csv')
#train.groupby(['ip', 'hour', 'day', 'channel']).os.count().rename('ip_hour_day_channel_nclick').to_frame().to_csv(DATA+'feature/test/ip_hour_day_channel_nclick.csv')
#train.groupby(['ip', 'hour', 'day', 'app']).os.count().rename('ip_hour_day_app_nclick').to_frame().to_csv(DATA+'feature/test/ip_hour_day_app_nclick.csv')
train.groupby(['device', 'os']).ip.count().rename('device_os_nclick').to_frame().to_csv(DATA+'feature/test/device_os_nclick.csv')
train.groupby(['channel', 'device', 'os']).ip.count().rename('channel_device_os_nclick').to_frame().to_csv(DATA+'feature/test/channel_device_os_nclick.csv')
train.groupby(['app', 'device', 'os']).ip.count().rename('app_device_os_nclick').to_frame().to_csv(DATA+'feature/test/app_device_os_nclick.csv')
train.groupby(['device', 'os', 'day', 'hour']).ip.count().rename('device_os_day_hour_nclick').to_frame().to_csv(DATA+'feature/test/device_os_day_hour_nclick.csv')
train.groupby(['channel', 'day', 'hour']).ip.count().rename('channel_day_hour_nclick').to_frame().to_csv(DATA+'feature/test/channel_day_hour_nclick.csv')