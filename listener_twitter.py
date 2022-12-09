import socket
import tweepy

HOST = 'localhost'
PORT = 9009

s = socket.socket()
s.bind((HOST,PORT))
print(f'Aguardando conexão na porta : {PORT}')

s.listen(5)
connection,  address = s.accept()
print(f'Recebendo solicitação de : {address}')


token ='AAAAAAAAAAAAAAAAAAAAAFBWkAEAAAAA6pSu%2BMCzxFKJYf%2BLE2w8xsPKkg8%3D8Bt3ZBU7zMIut6t9E9GwEW9o3NRNdLM90FUP7OVL4aTxZ1VaBY'
key_word = 'one piece'

class GetTweets(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        print('\n')
        print('='*50)
        connection.send(tweet.text.encode('utf-8', 'ignore'))

printer = GetTweets(token)
printer.add_rules(tweepy.StreamRule(key_word))
printer.filter()



connection.close()