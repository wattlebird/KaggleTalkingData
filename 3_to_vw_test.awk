BEGIN {
    base = log(10)
}
NR != 1 {
    printf("|ip %d |app %d |device %d |os %d |channel %d |hour %d |frequency ip_app:%.4f ip_app_os:%.4f ip_app_os_device:%.4f ip_channel:%.4f ip_hour_day:%.4f ip_hour_day_channel:%.4f ip_hour_day_app:%d ip_hour_day_app_channel:%d |last_click last_ip:%.4f last_ip_channel:%.4f last_ip_app:%.4f last_channel:%.4f last_app_device:%.4f last_app_channel:%.4f last_all:%.4f\n", $2, $3, $4, $5, $6, $7, log(2+$9)/base, log(2+$10)/base, log(2+$11)/base, log(2+$12)/base, log(2+$13)/base, log(2+$14)/base, log(2+$15)/base, log(2+$16)/base, log(2+$17)/base, log(2+$18)/base, log(2+$19)/base, log(2+$20)/base, log(2+$21)/base, log(2+$22)/base, log(2+$23)/base)
}