# YouTube Channel Tracker

## Overview

The **YouTube Channel Tracker** is a simple python script that opens Youtube when your favorite Youtuber uploads a new video. In this way, you can watch your favorite Youtuber's new video as soon as it is published! It uses the [YouTube API](https://console.developers.google.com/apis/api/youtube.googleapis.com) to accomplish this task.

## Setup
You'll need three things to get this script working:
* YouTube API Key
* Channel ID of the YouTube channel you want to track
* Channel name of the YouTube channel you want to track

*Note: Provide each of this thing in the code at lines 23, 24 and 25 respectively.*

### YouTube API Key
YouTube API key is the base of this script. Get the API key from here: https://console.developers.google.com/apis/api/youtube.googleapis.com

Paste it as the value for ```api_key``` variable at line 23.

### Channel ID
You would have to provide the channel ID of the youtube channel you want to track. 

For example:
![Channel ID](example.png)
The channel ID is the highlighted part of the URL, present just after the ```channel``` parameter.
Paste it in the ```channel_id``` variable at line 24.

### Channel name
Pretty obvious, the name of the channel you want to track, set the value for that at line 25.


## External modules required
- win10toast
- pyttsx3

Run the command ```pip install -r requirements.txt``` to install all these dependencies.

You are good to go!