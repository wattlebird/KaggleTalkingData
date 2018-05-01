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
    'ip_app_os_nclick': 'uint16',
    'ip_app_os_device_nclick': 'uint16',
    'ip_channel_nclick': 'uint32', 
    'ip_hour_day_nclick': 'uint16',
    'ip_day_nuniqhour': 'uint8',
    'ip_device_os_nuniqapp': 'uint8',
    'ip_nuniqapp': 'uint8',
    'ip_nuniqchannel': 'uint8',
    'ip_nuniqdevice': 'uint16',
    'app_nuniqchannel': 'uint8',
    'ip_app_channel_varhour': 'float32',
    'ip_app_os_varhour': 'float32',
    'ip_day_channel_varhour': 'float32',
    'ip_app_channel_avghour': 'float32'
}

train = pd.read_csv(DATA + 'train/train.csv', dtype=dtype, 
usecols=['ip', 'app', 'device', 'os', 'channel', 'is_attributed', 'hour', 'day'], engine='c')

c1 = pd.read_csv(FDATA+'feature/train/ip_app_nclick.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'app'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_app_os_nclick.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'app', 'os'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_app_os_device_nclick.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'app', 'os', 'device'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_channel_nclick.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'channel'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_hour_day_nclick.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'hour', 'day'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_day_nuniqhour.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'day'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_device_os_nuniqapp.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'device', 'os'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_nuniqapp.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_nuniqchannel.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_nuniqdevice.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/app_nuniqchannel.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['app'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_app_channel_varhour.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'app', 'channel'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_app_os_varhour.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'app', 'os'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_day_channel_varhour.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'day', 'channel'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_app_channel_avghour.csv', dtype=dtype)
train = train.merge(c1, how='left', on=['ip', 'app', 'channel'])
del c1

train.to_csv(FDATA+'feature/train/train_withcount.csv', index=False)
del train

test = pd.read_csv(DATA + 'train/test.csv', dtype=dtype, 
usecols=['ip', 'app', 'device', 'os', 'channel', 'is_attributed', 'hour', 'day'], engine='c')

c1 = pd.read_csv(FDATA+'feature/train/ip_app_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_app_os_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'os'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_app_os_device_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'os', 'device'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_channel_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'channel'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_hour_day_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'hour', 'day'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_day_nuniqhour.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'day'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_device_os_nuniqapp.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'device', 'os'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_nuniqapp.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_nuniqchannel.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_nuniqdevice.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/app_nuniqchannel.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['app'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_app_channel_varhour.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'channel'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_app_os_varhour.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'os'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_day_channel_varhour.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'day', 'channel'])
del c1

c1 = pd.read_csv(FDATA+'feature/train/ip_app_channel_avghour.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'channel'])
del c1

test.to_csv(FDATA+'feature/train/test_withcount.csv', index=False)
del test


test = pd.read_csv(DATA + 'test/train.csv', dtype=dtype, 
usecols=['ip', 'app', 'device', 'os', 'channel', 'is_attributed', 'hour', 'day'], engine='c')

c1 = pd.read_csv(FDATA+'feature/test/ip_app_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_app_os_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'os'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_app_os_device_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'os', 'device'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_channel_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'channel'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_hour_day_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'hour', 'day'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_day_nuniqhour.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'day'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_device_os_nuniqapp.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'device', 'os'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_nuniqapp.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_nuniqchannel.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_nuniqdevice.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/app_nuniqchannel.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['app'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_app_channel_varhour.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'channel'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_app_os_varhour.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'os'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_day_channel_varhour.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'day', 'channel'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_app_channel_avghour.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'channel'])
del c1

test.to_csv(FDATA+'feature/test/train_withcount.csv', index=False)

test = pd.read_csv(DATA + 'test/test.csv', dtype=dtype, 
usecols=['ip', 'app', 'device', 'os', 'channel', 'click_id', 'hour', 'day'], engine='c')

c1 = pd.read_csv(FDATA+'feature/test/ip_app_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_app_os_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'os'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_app_os_device_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'os', 'device'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_channel_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'channel'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_hour_day_nclick.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'hour', 'day'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_day_nuniqhour.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'day'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_device_os_nuniqapp.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'device', 'os'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_nuniqapp.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_nuniqchannel.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_nuniqdevice.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/app_nuniqchannel.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['app'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_app_channel_varhour.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'channel'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_app_os_varhour.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'os'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_day_channel_varhour.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'day', 'channel'])
del c1

c1 = pd.read_csv(FDATA+'feature/test/ip_app_channel_avghour.csv', dtype=dtype)
test = test.merge(c1, how='left', on=['ip', 'app', 'channel'])
del c1

test.to_csv(FDATA+'feature/test/test_withcount.csv', index=False)