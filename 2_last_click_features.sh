#gawk -F"," -f 2_last_ip.awk ~/Data/TalkingData/train/train.csv ~/Data/TalkingData/train/test.csv > ~/Data/TalkingData/runtime/train/last_ip.csv
#gawk -F"," -f 2_last_ip_channel.awk ~/Data/TalkingData/train/train.csv ~/Data/TalkingData/train/test.csv > ~/Data/TalkingData/runtime/train/last_ip_channel.csv
#gawk -F"," -f 2_last_ip_app.awk ~/Data/TalkingData/train/train.csv ~/Data/TalkingData/train/test.csv > ~/Data/TalkingData/runtime/train/last_ip_app.csv
#gawk -F"," -f 2_last_channel.awk ~/Data/TalkingData/train/train.csv ~/Data/TalkingData/train/test.csv > ~/Data/TalkingData/runtime/train/last_channel.csv
#gawk -F"," -f 2_last_app_device.awk ~/Data/TalkingData/train/train.csv ~/Data/TalkingData/train/test.csv > ~/Data/TalkingData/runtime/train/last_app_device.csv
#gawk -F"," -f 2_last_app_channel.awk ~/Data/TalkingData/train/train.csv ~/Data/TalkingData/train/test.csv > ~/Data/TalkingData/runtime/train/last_app_channel.csv
#gawk -F"," -f 2_last_all.awk ~/Data/TalkingData/train/train.csv ~/Data/TalkingData/train/test.csv > ~/Data/TalkingData/runtime/train/last_all.csv
gawk -F"," -f 2_last_device_os.awk ~/Data/TalkingData/train/train.csv ~/Data/TalkingData/train/test.csv > /media/ike/CE94F7F894F7E13F/Data/TalkingData/runtime/train/last_device_os.csv
gawk -F"," -f 2_last_app_device_os.awk ~/Data/TalkingData/train/train.csv ~/Data/TalkingData/train/test.csv > /media/ike/CE94F7F894F7E13F/Data/TalkingData/runtime/train/last_app_device_os.csv
gawk -F"," -f 2_last_channel_device_os.awk ~/Data/TalkingData/train/train.csv ~/Data/TalkingData/train/test.csv > /media/ike/CE94F7F894F7E13F/Data/TalkingData/runtime/train/last_channel_device_os.csv
gawk -F"," -f 2_last_app_device_os_channel.awk ~/Data/TalkingData/train/train.csv ~/Data/TalkingData/train/test.csv > /media/ike/CE94F7F894F7E13F/Data/TalkingData/runtime/train/last_app_device_os_channel.csv


#gawk -F"," -f 2_last_ip.awk ~/Data/TalkingData/test/train.csv ~/Data/TalkingData/test/test_gap.csv ~/Data/TalkingData/test/test.csv > ~/Data/TalkingData/runtime/test/last_ip.csv
#gawk -F"," -f 2_last_ip_channel.awk ~/Data/TalkingData/test/train.csv ~/Data/TalkingData/test/test_gap.csv ~/Data/TalkingData/test/test.csv > ~/Data/TalkingData/runtime/test/last_ip_channel.csv
#gawk -F"," -f 2_last_ip_app.awk ~/Data/TalkingData/test/train.csv ~/Data/TalkingData/test/test_gap.csv ~/Data/TalkingData/test/test.csv > ~/Data/TalkingData/runtime/test/last_ip_app.csv
#gawk -F"," -f 2_last_channel.awk ~/Data/TalkingData/test/train.csv ~/Data/TalkingData/test/test_gap.csv ~/Data/TalkingData/test/test.csv > ~/Data/TalkingData/runtime/test/last_channel.csv
#gawk -F"," -f 2_last_app_device.awk ~/Data/TalkingData/test/train.csv ~/Data/TalkingData/test/test_gap.csv ~/Data/TalkingData/test/test.csv > ~/Data/TalkingData/runtime/test/last_app_device.csv
#gawk -F"," -f 2_last_app_channel.awk ~/Data/TalkingData/test/train.csv ~/Data/TalkingData/test/test_gap.csv ~/Data/TalkingData/test/test.csv > ~/Data/TalkingData/runtime/test/last_app_channel.csv
#gawk -F"," -f 2_last_all.awk ~/Data/TalkingData/test/train.csv ~/Data/TalkingData/test/test_gap.csv ~/Data/TalkingData/test/test.csv > ~/Data/TalkingData/runtime/test/last_all.csv
gawk -F"," -f 2_last_device_os.awk ~/Data/TalkingData/test/train.csv ~/Data/TalkingData/test/test_gap.csv ~/Data/TalkingData/test/test.csv > /media/ike/CE94F7F894F7E13F/Data/TalkingData/runtime/test/last_device_os.csv
gawk -F"," -f 2_last_app_device_os.awk ~/Data/TalkingData/test/train.csv ~/Data/TalkingData/test/test_gap.csv ~/Data/TalkingData/test/test.csv > /media/ike/CE94F7F894F7E13F/Data/TalkingData/runtime/test/last_app_device_os.csv
gawk -F"," -f 2_last_channel_device_os.awk ~/Data/TalkingData/test/train.csv ~/Data/TalkingData/test/test_gap.csv ~/Data/TalkingData/test/test.csv > /media/ike/CE94F7F894F7E13F/Data/TalkingData/runtime/test/last_channel_device_os.csv
gawk -F"," -f 2_last_app_device_os_channel.awk ~/Data/TalkingData/test/train.csv ~/Data/TalkingData/test/test_gap.csv ~/Data/TalkingData/test/test.csv > /media/ike/CE94F7F894F7E13F/Data/TalkingData/runtime/test/last_app_device_os_channel.csv
