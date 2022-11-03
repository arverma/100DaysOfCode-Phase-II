# import tweepy
# from tweepy import Stream
# import socket
# import json
#
# # Authentication Token
# access_token = "71VOVfeoRTn8wsptUaft3dfO3"
# access_secret = "wPsA6RNYHvkH4d0io6HidwpRw0q57Nmb0eyeVO6vhkHgUDGV0r"
#
# # Consumer Key
# consumer_key = "Gd29UnaBynFyEQsYV6jTZSXJr"
# consumer_secret = "GwQiWcmBQGjpLkvpDeHrPFtMLQV1hL3NVTiqVxrvvx8CgZLbno"
#
#
# def sendData():
#     twitter_stream = Stream(access_token=access_token, access_token_secret=access_secret, consumer_key=consumer_key, consumer_secret=consumer_secret)
#     twitter_stream.filter(track=['football'])
#
#
# if __name__ == "__main__":
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
#     host = "127.0.0.1"  # Get local machine name
#     port = 5555  # Reserve a port for your service.
#     s.bind((host, port))  # Bind to the port
#
#     print("Listening on port: %s" % str(port))
#
#     s.listen(5)  # Now wait for client connection.
#     c, addr = s.accept()  # Establish connection with client.
#
#     print("Received request from: " + str(addr))
#
#     sendData()

from pyspark.sql import SparkSession