import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MailClient():

    def __init__(self, login, password):
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"
        self.SMTP_PORT = 587
        self.login = login
        self.password = password

    def create_message(self, recipients, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        return msg

    def send_message(self, recipients, subject, message):
        msg = self.create_message(recipients,subject, message)
        ms = smtplib.SMTP(self.GMAIL_SMTP, self.SMTP_PORT)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, recipients, msg.as_string())
        ms.quit()

    def receive_message(self, header=None):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        mail.logout()
        return email_message

if __name__ == '__main__':
    client1 = MailClient('login@gmail.com', 'qwerty')
    client1.send_message(['vasya@email.com', 'petya@email.com'],'Subject','Message')
    client1.receive_message()
