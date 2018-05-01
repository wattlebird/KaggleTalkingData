import pandas as pd
import numpy as np
from scipy.stats import skew
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

#s1 = train[['ip', 'day', 'channel', 'hour']].groupby(['ip', 'day', 'channel'])['hour'].var()
#s2 = train[['ip', 'app', 'os', 'hour']].groupby(['ip', 'app', 'os'])['hour'].var()
#s3 = train[['ip', 'app', 'channel', 'hour']].groupby(['ip', 'app', 'channel'])['hour'].var()
#s4 = train[['ip', 'app', 'channel', 'hour']].groupby(['ip', 'app', 'channel'])['hour'].mean()
#s1.rename('ip_day_channel_varhour').to_csv(DATA+'feature/train/ip_day_channel_varhour.csv', header=True, index=True)
#s2.rename('ip_app_os_varhour').to_csv(DATA+'feature/train/ip_app_os_varhour.csv', header=True, index=True)
#s3.rename('ip_app_channel_varhour').to_csv(DATA+'feature/train/ip_app_channel_varhour.csv', header=True, index=True)
#s4.rename('ip_app_channel_avghour').to_csv(DATA+'feature/train/ip_app_channel_avghour.csv', header=True, index=True)

s5 = train[['device', 'os', 'channel', 'hour']].groupby(['device', 'os', 'channel'])['hour'].var()
s6 = train[['device', 'os', 'app', 'hour']].groupby(['device', 'os', 'app'])['hour'].var()
s7 = train[['device', 'os', 'hour']].groupby(['device', 'os'])['hour'].var()
s5.rename('device_os_channel_varhour').to_csv(DATA+'feature/train/device_os_channel_varhour.csv', header=True, index=True)
s6.rename('device_os_app_varhour').to_csv(DATA+'feature/train/device_os_app_varhour.csv', header=True, index=True)
s7.rename('device_os_varhour').to_csv(DATA+'feature/train/device_os_varhour.csv', header=True, index=True)


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

#s1 = train[['ip', 'day', 'channel', 'hour']].groupby(['ip', 'day', 'channel'])['hour'].var()
#s2 = train[['ip', 'app', 'os', 'hour']].groupby(['ip', 'app', 'os'])['hour'].var()
#s3 = train[['ip', 'app', 'channel', 'hour']].groupby(['ip', 'app', 'channel'])['hour'].var()
#s4 = train[['ip', 'app', 'channel', 'hour']].groupby(['ip', 'app', 'channel'])['hour'].mean()
#s1.rename('ip_day_channel_varhour').to_csv(DATA+'feature/test/ip_day_channel_varhour.csv', header=True, index=True)
#s2.rename('ip_app_os_varhour').to_csv(DATA+'feature/test/ip_app_os_varhour.csv', header=True, index=True)
#s3.rename('ip_app_channel_varhour').to_csv(DATA+'feature/test/ip_app_channel_varhour.csv', header=True, index=True)
#s4.rename('ip_app_channel_avghour').to_csv(DATA+'feature/test/ip_app_channel_avghour.csv', header=True, index=True)

s5 = train[['device', 'os', 'channel', 'hour']].groupby(['device', 'os', 'channel'])['hour'].var()
s6 = train[['device', 'os', 'app', 'hour']].groupby(['device', 'os', 'app'])['hour'].var()
s7 = train[['device', 'os', 'hour']].groupby(['device', 'os'])['hour'].var()
s5.rename('device_os_channel_varhour').to_csv(DATA+'feature/test/device_os_channel_varhour.csv', header=True, index=True)
s6.rename('device_os_app_varhour').to_csv(DATA+'feature/test/device_os_app_varhour.csv', header=True, index=True)
s7.rename('device_os_varhour').to_csv(DATA+'feature/test/device_os_varhour.csv', header=True, index=True)
