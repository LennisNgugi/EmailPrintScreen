import pyautogui
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#The following script takes a printscreen and emails it to selected email addresses

#Screenshot Subject
myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'screenshot1.png')

#Screen notification
print('Screenshot taken')

#The mail addresses and password, in this example i'm using a gmail
sender_address = 'Sender@gmail.com'
sender_pass = 'Sendergmailpassword'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

#Setup mail content
mail_content = '''
		Demo content
	'''

#Setup global the MIME
message = MIMEMultipart()
message['Subject'] = 'Demo subject'

#Body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = 'screenshot1.png'
attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) #encode the attachment
payload.add_header('Content-Disposition', 'attachment', filename=attach_file_name)
message.attach(payload)

#Create SMTP session 
session = smtplib.SMTP(smtp_server, smtp_port)
session.starttls() #enable security
session.login(sender_address, sender_pass) #login
text = message.as_string()

mails = ['Receiver@hotmail.co.uk', 'Receiver@gmail.com']

for receiver_address in mails:
	#Setup the MIME
	message['From'] = sender_address
	message['To'] = receiver_address
	session.sendmail(sender_address, receiver_address, text)
	print('Mail Sent: '+receiver_address)

session.quit()
