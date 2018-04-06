filepath=/home/ike/Data/TalkingData/
echo "Joining ip_app_nclick for test/train"
xsv join --left ip,app ${filepath}test/train.csv ip,app ${filepath}feature/test/ip_app_nclick.csv | xsv select '!ip[1],app[1]' > ${filepath}test/train.temp.csv
echo "Joining ip_app_os_nclick for test/train"
xsv join --left ip,app,os ${filepath}test/train.temp.csv ip,app,os ${filepath}feature/test/ip_app_os_nclick.csv | xsv select '!ip[1],app[1],os[1]' > ${filepath}test/train.temp2.csv
echo "Joining ip_app_os_device_nclick for test/train"
xsv join --left ip,app,os,device ${filepath}test/train.temp2.csv ip,app,os,device ${filepath}feature/test/ip_app_os_device_nclick.csv | xsv select '!ip[1],app[1],os[1],device[1]' > ${filepath}test/train.temp.csv
echo "Joining ip_channel_nclick for test/train"
xsv join --left ip,channel ${filepath}test/train.temp.csv ip,channel ${filepath}feature/test/ip_channel_nclick.csv | xsv select '!ip[1],channel[1]' > ${filepath}test/train.temp2.csv
echo "Joining ip_hour_day_nclick for test/train"
xsv join --left ip,hour,day ${filepath}test/train.temp2.csv ip,hour,day ${filepath}feature/test/ip_hour_day_nclick.csv | xsv select '!ip[1],hour[1],day[1]' > ${filepath}test/train.temp.csv
echo "Joining ip_hour_day_channel_nclick for test/train"
xsv join --left ip,hour,day,channel ${filepath}test/train.temp.csv ip,hour,day,channel ${filepath}feature/test/ip_hour_day_channel_nclick.csv | xsv select '!ip[1],hour[1],day[1],channel[1]' > ${filepath}test/train.temp2.csv
echo "Joining ip_hour_day_app_nclick for test/train"
xsv join --left ip,hour,day,app ${filepath}test/train.temp2.csv ip,hour,day,app ${filepath}feature/test/ip_hour_day_app_nclick.csv | xsv select '!ip[1],hour[1],day[1],app[1]' > ${filepath}test/train.temp.csv
echo "Joining ip_hour_day_app_channel_nclick for test/train"
xsv join --left ip,hour,day,app,channel ${filepath}test/train.temp.csv ip,hour,day,app,channel ${filepath}feature/test/ip_hour_day_app_channel_nclick.csv | xsv select '!click_time,ip[1],hour[1],day[1],app[1],channel[1]' > ${filepath}test/train.ready.csv
echo "Removing temp files"
rm ${filepath}test/train.temp.csv ${filepath}test/train.temp2.csv

echo "Joining ip_app_nclick for test/test"
xsv join --left ip,app ${filepath}test/test.csv ip,app ${filepath}feature/test/ip_app_nclick.csv | xsv select '!ip[1],app[1]' > ${filepath}test/test.temp.csv
echo "Joining ip_app_os_nclick for test/test"
xsv join --left ip,app,os ${filepath}test/test.temp.csv ip,app,os ${filepath}feature/test/ip_app_os_nclick.csv | xsv select '!ip[1],app[1],os[1]' > ${filepath}test/test.temp2.csv
echo "Joining ip_app_os_device_nclick for test/test"
xsv join --left ip,app,os,device ${filepath}test/test.temp2.csv ip,app,os,device ${filepath}feature/test/ip_app_os_device_nclick.csv | xsv select '!ip[1],app[1],os[1],device[1]' > ${filepath}test/test.temp.csv
echo "Joining ip_channel_nclick for test/test"
xsv join --left ip,channel ${filepath}test/test.temp.csv ip,channel ${filepath}feature/test/ip_channel_nclick.csv | xsv select '!ip[1],channel[1]' > ${filepath}test/test.temp2.csv
echo "Joining ip_hour_day_nclick for test/test"
xsv join --left ip,hour,day ${filepath}test/test.temp2.csv ip,hour,day ${filepath}feature/test/ip_hour_day_nclick.csv | xsv select '!ip[1],hour[1],day[1]' > ${filepath}test/test.temp.csv
echo "Joining ip_hour_day_channel_nclick for test/test"
xsv join --left ip,hour,day,channel ${filepath}test/test.temp.csv ip,hour,day,channel ${filepath}feature/test/ip_hour_day_channel_nclick.csv | xsv select '!ip[1],hour[1],day[1],channel[1]' > ${filepath}test/test.temp2.csv
echo "Joining ip_hour_day_app_nclick for test/test"
xsv join --left ip,hour,day,app ${filepath}test/test.temp2.csv ip,hour,day,app ${filepath}feature/test/ip_hour_day_app_nclick.csv | xsv select '!ip[1],hour[1],day[1],app[1]' > ${filepath}test/test.temp.csv
echo "Joining ip_hour_day_app_channel_nclick for test/test"
xsv join --left ip,hour,day,app,channel ${filepath}test/test.temp.csv ip,hour,day,app,channel ${filepath}feature/test/ip_hour_day_app_channel_nclick.csv | xsv select '!click_time,ip[1],hour[1],day[1],app[1],channel[1]' > ${filepath}test/test.ready.csv
echo "Removing temp files"
rm ${filepath}test/test.temp.csv ${filepath}test/test.temp2.csv