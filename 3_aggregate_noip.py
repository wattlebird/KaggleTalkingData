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
    'ip_app_channel_avghour': 'float32',
    'app_device_os_nclick': 'uint32',
    'channel_device_os_nclick': 'uint32',
    'channel_day_hour_nclick': 'uint32',
    'device_os_app_nuniqhour': 'uint8',
    'device_os_app_nuniqip': 'uint32',
    'device_os_app_varhour': 'float32',
    'device_os_channel_nuniqhour': 'uint8',
    'device_os_channel_nuniqip': 'uint32',
    'device_os_channel_varhour': 'float32',
    'device_os_day_hour_nclick': 'uint32',
    'device_os_nclick': 'uint32',
    'device_os_nuniqhour': 'uint8',
    'device_os_nuniqip': 'uint32',
    'device_os_varhour': 'float32'
}


# on train set
train = pd.read_csv(FDATA + 'feature/train/train_withcount.csv', dtype=dtype, engine='c')

c = pd.read_csv(FDATA+'feature/train/app_device_os_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['app', 'device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/train/channel_device_os_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['channel', 'device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/train/channel_day_hour_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['channel', 'day', 'hour'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_day_hour_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'day', 'hour'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_app_nuniqhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'app'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_channel_nuniqhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'channel'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_nuniqhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_app_nuniqip.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'app'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_nuniqip.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_channel_nuniqip.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'channel'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_channel_varhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'channel'])
del c


c = pd.read_csv(FDATA+'feature/train/device_os_app_varhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'app'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_varhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os'])
del c

train.to_csv(FDATA+'feature/train/train_noip.csv', index=False)
train = pd.read_csv(FDATA + 'feature/train/test_withcount.csv', dtype=dtype, engine='c')

c = pd.read_csv(FDATA+'feature/train/app_device_os_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['app', 'device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/train/channel_device_os_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['channel', 'device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/train/channel_day_hour_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['channel', 'day', 'hour'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_day_hour_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'day', 'hour'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_app_nuniqhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'app'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_channel_nuniqhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'channel'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_nuniqhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_app_nuniqip.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'app'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_nuniqip.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_channel_nuniqip.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'channel'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_channel_varhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'channel'])
del c


c = pd.read_csv(FDATA+'feature/train/device_os_app_varhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'app'])
del c

c = pd.read_csv(FDATA+'feature/train/device_os_varhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os'])
del c

train.to_csv(FDATA+'feature/train/test_noip.csv', index=False)

# on test set
train = pd.read_csv(FDATA + 'feature/test/train_withcount.csv', dtype=dtype, engine='c')

c = pd.read_csv(FDATA+'feature/test/app_device_os_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['app', 'device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/test/channel_device_os_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['channel', 'device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/test/channel_day_hour_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['channel', 'day', 'hour'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_day_hour_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'day', 'hour'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_app_nuniqhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'app'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_channel_nuniqhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'channel'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_nuniqhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_app_nuniqip.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'app'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_nuniqip.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_channel_nuniqip.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'channel'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_channel_varhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'channel'])
del c


c = pd.read_csv(FDATA+'feature/test/device_os_app_varhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'app'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_varhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os'])
del c

train.to_csv(FDATA+'feature/test/train_noip.csv', index=False)
train = pd.read_csv(FDATA + 'feature/test/test_withcount.csv', dtype=dtype, engine='c')

c = pd.read_csv(FDATA+'feature/test/app_device_os_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['app', 'device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/test/channel_device_os_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['channel', 'device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/test/channel_day_hour_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['channel', 'day', 'hour'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_day_hour_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'day', 'hour'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_nclick.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_app_nuniqhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'app'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_channel_nuniqhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'channel'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_nuniqhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_app_nuniqip.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'app'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_nuniqip.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_channel_nuniqip.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'channel'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_channel_varhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'channel'])
del c


c = pd.read_csv(FDATA+'feature/test/device_os_app_varhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os', 'app'])
del c

c = pd.read_csv(FDATA+'feature/test/device_os_varhour.csv', dtype=dtype)
train = train.merge(c, how='left', on=['device', 'os'])
del c

train.to_csv(FDATA+'feature/test/test_noip.csv', index=False)