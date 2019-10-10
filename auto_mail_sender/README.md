# Auto mail sender

This app will send customized mails automatically

## Before Use

- Make sure that you have a proper Internet connection
- MAke sure you have installed `Python 3.x`
- Make sure that your Python is not blocked by your firewall

## Steps to use

1. Clone or download the whole repo
2. Open `cmd` or `terminal` in your working directory.
3. Create a Virtualenv by typing `python -m virtualenv mailsender`
4. Activate the env by typing `./mailsender/Scripts/activate`
5. Install depandencies by typing `python -m pip install -r requirements.txt`
6. Goto [this](https://developers.google.com/gmail/api/quickstart/python) website to generate your gmail api credentials
7. Download the `credentials.json` file and place it in the working directory.
8. Edit the `send.csv` file and add columns amd rows im it depend upon your need
    - Don't forget to add `email` field in the file

9. Edit the `email.html` file under the `templates` dir depand upon your need
    - To edit it perfectly use Jinja2 HTML format. Check [this](https://jinja.palletsprojects.com/en/2.10.x/templates/) 
    - `Make sure that the column names in the csv and the variable names are the same`
10. Change the `CONFIG` part in the `main.py` file
11. run the `main.py` using `python main.py`
12. A Prompt for login can apprear if you are using if for the first time.

## Contributer
Arkadip Bhattacharya