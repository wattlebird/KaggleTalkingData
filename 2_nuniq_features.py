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

#cu1 = train[['ip', 'channel']].groupby('ip')['channel'].nunique()
#cu2 = train[['ip', 'device', 'os', 'app']].groupby(['ip', 'device', 'os'])['app'].nunique()
#cu3 = train[['ip', 'day', 'hour']].groupby(['ip', 'day'])['hour'].nunique()
#cu4 = train[['ip', 'app']].groupby('ip')['app'].nunique()
#cu5 = train[['ip', 'device']].groupby('ip')['device'].nunique()
#cu6 = train[['app', 'channel']].groupby('app')['channel'].nunique()
#cu1.rename('ip_nuniqchannel').to_csv(DATA+'feature/train/ip_nuniqchannel.csv', header=True, index=True)
#cu2.rename('ip_device_os_nuniqapp').to_csv(DATA+'feature/train/ip_device_os_nuniqapp.csv', header=True, index=True)
#cu3.rename('ip_day_nuniqhour').to_csv(DATA+'feature/train/ip_day_nuniqhour.csv', header=True, index=True)
#cu4.rename('ip_nuniqapp').to_csv(DATA+'feature/train/ip_nuniqapp.csv', header=True, index=True)
#cu5.rename('ip_nuniqdevice').to_csv(DATA+'feature/train/ip_nuniqdevice.csv', header=True, index=True)
#cu6.rename('app_nuniqchannel').to_csv(DATA+'feature/train/app_nuniqchannel.csv', header=True, index=True)
#del cu1,cu2,cu3,cu4,cu5,cu6

#cu7 = train[['device', 'os', 'ip']].groupby(['device', 'os'])['ip'].nunique()
#cu8 = train[['device', 'os', 'hour']].groupby(['device', 'os'])['hour'].nunique()
#cu9 = train[['device', 'os', 'channel', 'ip']].groupby(['device', 'os', 'channel'])['ip'].nunique()
#cu10 = train[['device', 'os', 'channel', 'hour']].groupby(['device', 'os', 'channel'])['hour'].nunique()
#cu11 = train[['device', 'os', 'app', 'ip']].groupby(['device', 'os', 'app'])['ip'].nunique()
#cu12 = train[['device', 'os', 'app', 'hour']].groupby(['device', 'os', 'app'])['hour'].nunique()
#cu7.rename('device_os_nuniqip').to_csv(DATA+'feature/train/device_os_nuniqip.csv', header=True, index=True)
#cu8.rename('device_os_nuniqhour').to_csv(DATA+'feature/train/device_os_nuniqhour.csv', header=True, index=True)
#cu9.rename('device_os_channel_nuniqip').to_csv(DATA+'feature/train/device_os_channel_nuniqip.csv', header=True, index=True)
#cu10.rename('device_os_channel_nuniqhour').to_csv(DATA+'feature/train/device_os_channel_nuniqhour.csv', header=True, index=True)
#cu11.rename('device_os_app_nuniqip').to_csv(DATA+'feature/train/device_os_app_nuniqip.csv', header=True, index=True)
#cu12.rename('device_os_app_nuniqhour').to_csv(DATA+'feature/train/device_os_app_nuniqhour.csv', header=True, index=True)
#del cu7,cu8,cu9,cu10,cu11,cu12

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

#cu1 = train[['ip', 'channel']].groupby('ip')['channel'].nunique()
#cu2 = train[['ip', 'device', 'os', 'app']].groupby(['ip', 'device', 'os'])['app'].nunique()
#cu3 = train[['ip', 'day', 'hour']].groupby(['ip', 'day'])['hour'].nunique()
#cu4 = train[['ip', 'app']].groupby('ip')['app'].nunique()
#cu5 = train[['ip', 'device']].groupby('ip')['device'].nunique()
#cu6 = train[['app', 'channel']].groupby('app')['channel'].nunique()
#cu1.rename('ip_nuniqchannel').to_csv(DATA+'feature/test/ip_nuniqchannel.csv', header=True, index=True)
#cu2.rename('ip_device_os_nuniqapp').to_csv(DATA+'feature/test/ip_device_os_nuniqapp.csv', header=True, index=True)
#cu3.rename('ip_day_nuniqhour').to_csv(DATA+'feature/test/ip_day_nuniqhour.csv', header=True, index=True)
#cu4.rename('ip_nuniqapp').to_csv(DATA+'feature/test/ip_nuniqapp.csv', header=True, index=True)
#cu5.rename('ip_nuniqdevice').to_csv(DATA+'feature/test/ip_nuniqdevice.csv', header=True, index=True)
#cu6.rename('app_nuniqchannel').to_csv(DATA+'feature/test/app_nuniqchannel.csv', header=True, index=True)
#del cu1,cu2,cu3,cu4,cu5,cu6

cu7 = train[['device', 'os', 'ip']].groupby(['device', 'os'])['ip'].nunique()
cu8 = train[['device', 'os', 'hour']].groupby(['device', 'os'])['hour'].nunique()
cu9 = train[['device', 'os', 'channel', 'ip']].groupby(['device', 'os', 'channel'])['ip'].nunique()
cu10 = train[['device', 'os', 'channel', 'hour']].groupby(['device', 'os', 'channel'])['hour'].nunique()
cu11 = train[['device', 'os', 'app', 'ip']].groupby(['device', 'os', 'app'])['ip'].nunique()
cu12 = train[['device', 'os', 'app', 'hour']].groupby(['device', 'os', 'app'])['hour'].nunique()
cu7.rename('device_os_nuniqip').to_csv(DATA+'feature/test/device_os_nuniqip.csv', header=True, index=True)
cu8.rename('device_os_nuniqhour').to_csv(DATA+'feature/test/device_os_nuniqhour.csv', header=True, index=True)
cu9.rename('device_os_channel_nuniqip').to_csv(DATA+'feature/test/device_os_channel_nuniqip.csv', header=True, index=True)
cu10.rename('device_os_channel_nuniqhour').to_csv(DATA+'feature/test/device_os_channel_nuniqhour.csv', header=True, index=True)
cu11.rename('device_os_app_nuniqip').to_csv(DATA+'feature/test/device_os_app_nuniqip.csv', header=True, index=True)
cu12.rename('device_os_app_nuniqhour').to_csv(DATA+'feature/test/device_os_app_nuniqhour.csv', header=True, index=True)
del cu7,cu8,cu9,cu10,cu11,cu12