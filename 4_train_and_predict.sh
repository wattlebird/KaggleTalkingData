lightgbm config=lightgbm.train.config train=/home/ike/Data/TalkingData/test/train_ready.csv output_model=/home/ike/Data/TalkingData/test/lightgbm.model
lightgbm config=lightgbm.test.config data=/home/ike/Data/TalkingData/test/test_ready.csv output_result=/home/ike/Data/TalkingData/test/test_result.csv
