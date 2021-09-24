from twitter_bot import InternetSpeedTwitterBot, PROMISED_UP, PROMISED_DOWN

internet_speed_complaint = InternetSpeedTwitterBot()
internet_speed_complaint.get_internet_speed()
if float(internet_speed_complaint.download_speed) < PROMISED_DOWN or \
        float(internet_speed_complaint.upload_speed) < PROMISED_UP:
    internet_speed_complaint.tweet_at_provider()
else:
    print("Nothing wrong with your internet speed!")
