gawk -F "," -f 3_to_vw.awk ~/Data/TalkingData/train/train_final.csv | gzip -c > ~/Data/TalkingData/train/train.vw.gz
gawk -F "," -f 3_to_vw.awk ~/Data/TalkingData/train/test_final.csv | gzip -c > ~/Data/TalkingData/train/test.vw.gz

gawk -F "," -f 3_to_vw.awk ~/Data/TalkingData/test/train_final.csv | gzip -c > ~/Data/TalkingData/test/train.vw.gz
gawk -F "," -f 3_to_vw_test.awk ~/Data/TalkingData/test/test_final.csv | gzip -c > ~/Data/TalkingData/test/test.vw.gz