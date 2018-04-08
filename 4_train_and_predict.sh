lightgbm config=lightgbm.train.config train=/home/ike/Data/TalkingData/test/train_ready.csv output_model=/home/ike/Data/TalkingData/test/lightgbm.model
lightgbm config=lightgbm.test.config data=/home/ike/Data/TalkingData/test/test_ready.csv output_result=/home/ike/Data/TalkingData/test/test_result.csv
sed -i '1i is_attributed' /home/ike/Data/TalkingData/test/test_result.csv
paste -d"," /home/ike/Data/TalkingData/test/test.csv /home/ike/Data/TalkingData/test/test_result.csv | cut -d"," -f1,10 > /home/ike/Data/TalkingData/result_040702.csv