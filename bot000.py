import tweepy

# المفاتيح من Twitter Developer
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# المصادقة
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# تغريدة
api.update_status("أول تغريدة من البوت 🤖!")

