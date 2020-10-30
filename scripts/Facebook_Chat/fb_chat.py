import fbchat
from fbchat.models import *
from getpass import getpass

username = input("Username: ")
client = fbchat.Client(username, getpass())
no_of_friends = int(input("Number of friends: "))

for i in range(no_of_friends):
    name = input("Name: ")
    friends = client.searchForUsers(name) # return a list of names
    friend = friends[0]
    message = input("Message: ")
    sent = client.send(Message(text=message), thread_id=friend.uid)
    if sent:
        print("Message sent successfully!")
    else:
        print("Message Sending failed")
