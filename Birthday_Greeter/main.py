#This script will send the birthday Greet message when someone birthday is found from the text file.

from tweepy import OAuthHandler
import tweepy
import time

#add your keys here.
APP_KEY = ''
APP_SECRET = ''
access_token= ''
access_token_secret =''
auth = OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(access_token, access_token_secret)

# Create API object
API = tweepy.API(auth)

#sending Message on birthdays
def AutoBirthdayMessage():
    #opening file which has dates and usernames
    with open('birthdayFile.txt', 'r') as fileName:
    
        #getting Current date
        today = time.strftime('%m/%d')

        #checking if there is any dates match from file with current date
        for line in fileName:

            #if day is matched,then send the message to that user.
            if today in line:
                line = line.split(' ')
                user = API.get_user(line[1])
                message = f"Wishing you a day filled with happiness and a year filled with joy. Happy birthday {user.name}"
                API.send_direct_message(user.id, message)

####################################
try:
    while True:
        AutoBirthdayMessage()
        #loop back after 24hr
        time.sleep(86400)
except Exception as e:
    print(e)




#bonus function for sending message to followers
#send message to followers
def sendMessageAll(message):
    for follower in API.followers_ids():
        API.send_direct_message(follower,message)





#author 20prince12
