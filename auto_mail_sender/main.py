from Message import Message
from htmlJinja import template_loader
import pandas as pd


def send_each_msg(Message ,sender, subject, html_template, **kwargs):

    '''
        Async function for sending each mail one by one

        Args:
            Message: [Meaasge Object]
            sender: name of sender
            to: To
            sebject: subject of the message
            additional args
    '''
    try:
        to = kwargs['email']
        kwargs.pop('email')
    
    except KeyError:
        print("Email id is missing")
    
    else:
        html_template = html_template.render(**kwargs)
        Message.create_message_html(sender, to, subject, html_template)
        Message.send_message()
    return


if __name__ == "__main__":
    
    #------- CONFIG --------
    sender = 'Arkadip <in2arkadipb13@gmail.com>'
    subject = 'This it a subject'
    template_name = 'email.html'
    template_folder = 'templates'
    #----------------------

    #------- SETUP AND LOGIN ------
    print("Setting things up...")
    msg = Message(SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send'])
    print("Logging in...")
    msg.login()
    print("Successfully logged in.")
    #-------------------------------

    #------- HTML TEMPLATE LOADER ------
    print("Loading HTML template...")
    html_template = template_loader(template_name= template_name, template_folder= template_folder)
    #-----------------------------------

    #------- CSV FETCHING --------
    print("Fetching the CSV...")
    send_file = pd.read_csv('send.csv')
    print("Got the file...\nSending mails....")
    #-----------------------------

    #------- SENDING INDIVISUAL --------
    for _ , values in send_file.iterrows():
        send_each_msg(msg, sender , subject, html_template, **values)
    #-----------------------------------