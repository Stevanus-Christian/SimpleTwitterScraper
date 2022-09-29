import tweepy
import csv 

# This is my private API key, better use your own API key!
api_key = "SdGTAU6SVeyhBR5JCmwB5brDX"
api_key_secret = "UUdkyX4yavxC0NvGoeyT0AL8BuPgQmnhGtpG6DOq8ZmzbBbEnc"
bearer_token = "1023097683332853760-pwRD2YZXPG700P6A2SQo5Jkx2fE5ma"
bearer_token_secret = "MwxMO1hRPkR5ekHD4lYKimoyjCoYWVHWcZa6rttr4wsr7"

# Verifying Credentials
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(bearer_token, bearer_token_secret)
api = tweepy.API(auth)

try:
	api.verify_credentials()
	print("Authentication OK")
	tweets = tweepy.Cursor(api.search_tweets, q="bjorka").items()

	# CMD
	#for tweet in tweets:
	#	print(tweet.created_at, tweet.user.name,'\n',tweet.text)
	#	print('\n')
	
	# Flat File
	#with open('tweet.txt', 'a+', newline='', encoding="utf-8") as file:	
	#	try:
	#		i = 0
	#		for tweet in tweets:
	#			file.write(str(tweet.created_at))
	#			file.write('\n')
	#			file.write(tweet.user.name)
	#			file.write('\n')
	#			file.write(tweet.text)
	#			file.write('\n')
	#			file.write('\n')
	#			print(i)
	#			i = i + 1
	#		file.close()
	#	except Exception as e:
	#		print(e)
	
	# CSV
	with open('tweet.csv', 'a', newline='', encoding="utf-8") as file:
		try:
			writer = csv.writer(file)
			i = 0
			for tweet in tweets:
				tw = [tweet.created_at,tweet.user.name,tweet.text,tweet.user.location]
				writer.writerow(tw)
				print(i)
				i = i + 1
		except Exception as e:
			print(e)
except Exception as e:
    print(e)
