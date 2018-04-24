gawk -f 1_format_second.awk ~/Data/TalkingData/test/train.csv > ~/Data/TalkingData/test/train_new.csv
rm ~/Data/TalkingData/test/train.csv
mv ~/Data/TalkingData/test/train_new.csv ~/Data/TalkingData/test/train.csv

gawk -f 1_format_second.awk ~/Data/TalkingData/test/test.csv > ~/Data/TalkingData/test/test_new.csv
rm ~/Data/TalkingData/test/test.csv
mv ~/Data/TalkingData/test/test_new.csv ~/Data/TalkingData/test/test.csv

gawk -f 1_format_second.awk ~/Data/TalkingData/train/train.csv > ~/Data/TalkingData/train/train_new.csv
rm ~/Data/TalkingData/train/train.csv
mv ~/Data/TalkingData/train/train_new.csv ~/Data/TalkingData/train/train.csv

gawk -f 1_format_second.awk ~/Data/TalkingData/train/test.csv > ~/Data/TalkingData/train/test_new.csv
rm ~/Data/TalkingData/train/test.csv
mv ~/Data/TalkingData/train/test_new.csv ~/Data/TalkingData/train/test.csv