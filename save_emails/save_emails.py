import imaplib
import email
from collections import defaultdict
import configparser
import os
import sys
from os import listdir
from os.path import isfile, join

# adds email note to corresponding note in directory
def add_to_note(to_add):
	dir_1 = "../thoughts_on/"
	for new_note in to_add:
		temp_file = open(dir_1+'temp.txt',"w+")
		new_txt = to_add[new_note][0] + '\n' + to_add[new_note][1] + '\n'
		temp_file.write(new_txt)
		print("wrote %s" % new_txt)
		fname = dir_1 + new_note + '.txt'

		# adds new note to beginning of file
		old_file = open(fname, "r+")
		temp_file.write(old_file.read())
		old_file.seek(0)
		temp_file.seek(0)
		old_file.write(temp_file.read())
		
		temp_file.close()
		old_file.close()

# read email
def readmail():
	notes_to_add=defaultdict(lambda:'')

	config=configparser.RawConfigParser()
	config.read(os.path.join(os.path.dirname(sys.argv[0]),".emailrc"))
	email_address = config.get('auth','email')
	password = config.get('auth','password')
	approved_from = config.get('auth','from')

	SMTP_SERVER = "imap.gmail.com"
	SMTP_PORT  = 993
	mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
	mail.login(email_address,password)
	mail.select('inbox')

	# reads unseen messages and adds to dict
	type, data = mail.search(None, '(UNSEEN)')
	mail_ids = [int(x) for x in data[0].decode("utf-8").split()]
	for index, emailid in enumerate(mail_ids):
		resp, data = mail.fetch(str(emailid),'(RFC822)' )
		for response_part in data:
			if isinstance(response_part, tuple):
				msg = email.message_from_string(response_part[1].decode('utf-8'))
				# print(msg.keys())
				email_subject = msg['subject']
				email_from = msg['from']
				email_date = msg['date']
				for part in msg.walk():
					if part.get_content_type() == 'text/plain':
					    body = part.get_payload() # prints the raw text
					    # if email_from == approved_from:
					    notes_to_add[email_subject] = [email_date,body]

	mail.close()
	mail.logout()

	return notes_to_add

if __name__ == '__main__':
	to_add = readmail()

	add_to_note(to_add)
	
