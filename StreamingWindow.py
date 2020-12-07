import tweepy
from tweepy.auth import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json

CONSUMER_KEY = "Your key"
CONSUMER_SECRET = "Your secrect key"
ACCESS_TOKEN = "Your Token"
ACCESS_TOKEN_SECRET = "Your Token secret"


class TweetsListener(StreamListener):

    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            msg = json.loads(data)
            #print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


def sendData(c_socket):
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    twitter_stream = Stream(auth, TweetsListener(c_socket))
    twitter_stream.filter(
        track=['donald', 'Trump', 'US2020', 'USelection', '2020Election', 'Biden', 'JoeBiden', 'DonaldTrump'])


if __name__ == "__main__":
    s = socket.socket()
    host = "localhost"
    port = 8090
    s.bind((host, port))

    print("Listening on port: %s"+str(port))
    s.listen(5)
    c, addr = s.accept();
    print("Recieved request from:" + str(addr))
    sendData(c)