import tweepy
consumer_key='SJzCh4qrCCw85CwueWPU2ObXV'
consumer_key_secret ='PmZVJ480YsLX5UO4KHQb2nYoSegnmK9f1xAJ3nz6Nrw6drU3V'
access_token ='289979938Dhqt6hJYGpk9AzZV8rlsszG1hNPRAUwl4OmXeld2'
access_token_secret ='aPXJDDcfnc0DXKo5zDzZ1fJs8lrflMoo1XJll77EHdNqHw'

key = tweepy.OAuthHandler(consumer_key,consumer_key_secret)

key.set_access_token(access_token,access_token_secret)
api = tweepy.API(key)
print api.me().name


