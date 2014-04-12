#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Bugs:
1) if two people have more than one tag in common, sends it to them twice
2) if message is still too long after the "name name tags" format, will delete from dictionary 
*** 3) Does the same thing every time we run; need to save most_recent tweet
 '''
import tweepy
import time
import sys
import re #regex

#initializing variables
sleep_time = 60 #in seconds
#dict in form of hashtag (with #) : screen_name (w/o @)
all_hashtags = {}
#stores most recent tweet to avoid re-checking; false to check all on first run
most_recent = False

#takes filename as parameter; run as run helloworld helloworld.txt
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'aWotBD0Mgu5RFnBwGJa6UNbRW'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '6sP0WXVKRrvCUz2VUCDwGpdv7rA7cWc7vMI9M6mA5rWbaFWH65'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '2439574633-hFQDS7YBoHNRdqxxjK3TPAtwVG1QufflVl1zmQJ'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'z5cGMlzEcuHod44YPiVYw2Ux5HPMwPZcci15lZR08sfJi'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#while True:
	#all tweets directed at us in reverse chronological order; most recent is first
tweets = api.mentions_timeline()

while True:
	for tweet in tweets:
		print tweet
		#most_recent: always true unless it's first time
		if most_recent and (tweet.id == most_recent.id):
			break
		else:
			#find all hashtags in text - includes #
			hashtags = re.findall('#[^ #]*',tweet.text)
			for hashtag in hashtags:
				#use lower case versions
				hashtag = str.lower(str(hashtag))
				if hashtag in all_hashtags:
					user1 = all_hashtags[hashtag]
					user2 = tweet.user.screen_name
					message = str.format('@{0} and @{1} are {2} buddies!', user1, user2, hashtag)
					if len(message) > 140:
						message = str.format('@{0} @{1} {2}', user1, user2, hashtag)
					api.update_status(message)
					del all_hashtags[hashtag]
				else:
					all_hashtags[hashtag] = tweet.user.screen_name
	#update most recent tweet
	most_recent = tweets[0]
	#time.sleep(sleep_time)
