import smtplib
import time
import imaplib
import email

"""Please remember to change the email/passowrd to your particular email's username 
and password!"""

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "yourEmailAddress" + ORG_EMAIL
FROM_PWD    = "yourPassword"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993


def read_email():
    try:
        m = imaplib.IMAP4_SSL(SMTP_SERVER)
        m.login(FROM_EMAIL,FROM_PWD)
        m.select('inbox')

        type, data = m.search(None, 'ALL')
        m_ids = data[0]

        id_list = m_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for responses in data:
                if isinstance(responses, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print 'From : ' + email_from + '\n'
                    print 'Subject : ' + email_subject + '\n'

    except Exception, e:
        print str(e)