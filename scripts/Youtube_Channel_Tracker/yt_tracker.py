import webbrowser, pyttsx3
from win10toast import ToastNotifier
from time import sleep
from json import loads as jloads
from requests import get as rget

def speak(text):
    """
    Speaks the given string.
    """
    print(text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def look_for_new_video():
    """
    Looks for the new video of the channel specified.
    """

    # api key and channel id
    api_key = "YOUTUBE API KEY HERE" # GET IT FROM HERE https://console.developers.google.com/apis/api/youtube.googleapis.com
    channel_id = "CHANNEL ID YOU WANT TO TRACK"
    channel_name = "CHANNEL NAME YOU WANT TO TRACK"
        
    # base video url for youtube
    # base search url for the video search using youtube api
    base_video_url = "https://www.youtube.com/watch?v="
    base_search_url = "https://www.googleapis.com/youtube/v3/search?"

    # main url for api search
    url = base_search_url + f"key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=1"

    # initialising old video id
    r = rget(url).text
    parser = jloads(r)
    old_vidID = (parser['items'][0]['id']['videoId'])

    # intialising toaster object for notifications
    toaster = ToastNotifier()

    tries = 0
    while True:
        # initialising the new video url until new video is published
        r = rget(url).text
        parser = jloads(r)
        new_vidID = (parser['items'][0]['id']['videoId'])

        # when new video is not published, i.e. new video id is same as old video id
        if new_vidID == old_vidID:
            tries += 1
            print(f"Try {tries}: No new video!")
            sleep(30)
        
        # when new video has been published, i.e. new video id is different 
        else:
            try:
                # fetching video title from the api data
                title = parser['items'][0]['snippet']['title']

                # alerting the user by a notification and speaking
                toaster.show_toast(f"Youtube Tracker", f"New video from {channel_name} has arrived!\nTitle: {title}", duration=5)
                
                speak(f"New video has arrived! Title is:")
                speak(title)

                # opening the video on the default browser
                videoURL = base_video_url + new_vidID
                webbrowser.open(videoURL)


            except KeyboardInterrupt:
                raise SystemExit

            except Exception as e:
                print(e)
                raise SystemExit
        
if __name__ == "__main__":
    look_for_new_video()