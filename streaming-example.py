from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key='aWotBD0Mgu5RFnBwGJa6UNbRW'
consumer_secret='6sP0WXVKRrvCUz2VUCDwGpdv7rA7cWc7vMI9M6mA5rWbaFWH65'

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token='2439574633-hFQDS7YBoHNRdqxxjK3TPAtwVG1QufflVl1zmQJ'
access_token_secret='z5cGMlzEcuHod44YPiVYw2Ux5HPMwPZcci15lZR08sfJi'

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print json.loads(data)['text']
        return False

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['chicago'])