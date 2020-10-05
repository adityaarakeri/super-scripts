# Auto-lecture attender
***
This python script lets you automatically join a Google meet meeting and attend it for a specified time period. Mind it, this script is not for skipping lectures [I wrote it during a lecture anyway :)].
***
# Dependencies
1. `python3`
If you use a linux distro, you probably got this already. Check with the following command:
`python3 -V`
or [Download](https://www.python.org/downloads/) for your machine.
2. `pip3`

You may or may not have this depending on your distro (Most linux guys may not have this)

Check:
`pip3 -V`

Install it using following command:
`apt-get install python3-pip`

3. `selenium`

Install using pip3 from a terminal:
`pip install selenium`

Download driver for chrome from [here](https://chromedriver.storage.googleapis.com/index.html?path=86.0.4240.22/). Choose the one which matches your machine.

After downloading chrome driver, extract the .zip file.
Place the driver file somewhere secure. (/usr/local/bin for linux)

Now, open main.py file of this project in a text editor and replace the `executable_path` entry on line 15 which should look like:
```
self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
```
to the path of wherever you placed the chrome driver.

4. `Chrome`
[Download](https://www.google.com/intl/en_in/chrome/) it from here

# Usage

Open the project directory in terminal

Run the main file using following command:
`python3 main.py`

`Enter your Gmail address:`
It'll ask you for your Gmail address. This would be the address using which you may want to join the meet.

`Password:`
Don't worry, your password doesn't get stored locally nor does it get displayed anywhere (input is obscure), it's used for logging in to your Google account. Now, here you can speed up things by hardcoding your password in the `main.py` file on line 9 e.g `pw=Covid19` . But this way, your password will be stored in the file and anyone with access to your machine can retrieve it. I would strongly recommend to follow the default method and don't hardcode your password.

`Enter the Google Meet link:`
Paste the link to your Google meet meeting here e.g `https://meet.google.com/yourlecturelink` 

`Duration of lecture:`
Enter how long you want to stay in the meet. Enter this value in seconds only. e.g If you want to attend a lecture for 1 hour, enter `3600`. Or if you want to attend a lecture for 45 minutes, enter `2700`
Keep in mind that after the specified time, script will end and browser will be closed, hence exiting from the meet.

Default config:
Camera and microphone are turned off by default.
The infamous Chrome `allow permission` dialog box can't be closed automatically. It doesn't affect the meet anyway.