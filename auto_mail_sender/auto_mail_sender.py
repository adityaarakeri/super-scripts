"""
Following code has been written and tested on Python 3.7.
This script sends mail with the given content to the specified recipients.
Example usage: When user needs to send auto-generated reports to multiple recipients.
"""
import win32com.client as win32object

"""
Launching the outlook application.
"""
outlook_object = win32object.Dispatch('outlook.application')


def send_mail_outlook(to_list=None, cc_list=None, bcc_list=None, list_attachment=None, subject=None, content=None):
    """
    :param to_list: list of email addresses for "To"
    :param cc_list: list of email addresses for "CC"
    :param bcc_list: list of email addresses for "BCC"
    :param list_attachment: list of email addresses for attachment
    :param subject: Subject of the mail
    :param content: Content of the mail
    :return:
    """
    mail = outlook_object.CreateItem(0)
    if to_list is not None:
        mail.To = to_list
    if cc_list is not None:
        mail.CC = cc_list
    if bcc_list is not None:
        mail.BCC = bcc_list
    if list_attachment is not None:
        for path_docs in list_attachment:
            mail.Attachments.Add(path_docs)
    if subject is not None:
        mail.Subject = subject
    if content is not None:
        mail.Body = content
    if to_list is None and cc_list is None and bcc_list is None:
        print("Please provide recipient address...")
    else:
        if subject is None:
            print("Mail will be send without subject..")
        if content is None:
            print("Mail will be send without any message..")
        mail.send
        print("Mail has been sent..")


def main():
    # replace the mail ID with the ones you need to send mail to
    to_list = "sample1@gmail.com;sample2@gmail.com"
    send_mail_outlook(to_list=to_list)


if __name__ == '__main__':
    main()
