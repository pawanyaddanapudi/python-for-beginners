
## Logs & Notifications
# Logging
# Reporting
# Email
import logging
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

print("This is OrSkl and you are in Python for Beginners class")
logging.error(" This is OrSkl and you are in Python for Beginners class")
logging.warning(" This is OrSkl and you are in Python for Beginners class")
logging.critical(" This is OrSkl and you are in Python for Beginners class")
logging.info(" This is OrSkl and you are in Python for Beginners class")
logging.getLogger().setLevel(logging.INFO)
logging.info(" This is OrSkl and you are in Python for Beginners class")


### Set handlers on your own


orskl_handler = logging.StreamHandler()
orskl_handler.setFormatter(logging.Formatter('%(asctime)s : %(name)s | %(levelname)s + %(message)s'))

orskl_logger = logging.getLogger(__name__)
orskl_logger.addHandler(orskl_handler)
orskl_logger.error(" This is OrSkl and you are in Python for Beginners class")
orskl_logger.critical(" This is OrSkl and you are in Python for Beginners class")

orskl_handler2 = logging.StreamHandler()
orskl_handler2.setFormatter(logging.Formatter('%(asctime)s : %(name)s | %(levelname)s + %(message)s'))

orskl_logger2 = logging.getLogger(__name__)
orskl_logger2.addHandler(orskl_handler2)
orskl_logger2.error(" This is OrSkl and you are in Python for Beginners class")
orskl_logger2.critical(" This is OrSkl and you are in Python for Beginners class")


orskl_handler3 = logging.StreamHandler()
orskl_handler3.setFormatter(logging.Formatter('%(asctime)s : %(name)s - %(levelname)s ---- %(message)s'))

orskl_logger3 = logging.getLogger(__name__)
orskl_logger3.addHandler(orskl_handler3)
orskl_logger3.error(" This is OrSkl and you are in Python for Beginners class")
orskl_logger3.critical(" This is OrSkl and you are in Python for Beginners class")


### Please try creating multiple handlers using config.yaml file and load into your python shell

logging.info('This is Info message')
logging.getLogger().setLevel(logging.INFO)
logging.info('This is Info message')


# Creating handlers and format
import logging
# Create a custom logger
orskl_logger = logging.getLogger(__name__)
orskl_handle = logging.StreamHandler()
orskl_handle.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
orskl_logger.addHandler(orskl_handle)
orskl_logger.error("Info message")

orskl_handle.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
orskl_logger.addHandler(orskl_handle)
orskl_logger.error("Info message")


# https://docs.python.org/3/library/logging.html



# https://myaccount.google.com/lesssecureapps

import smtplib
from credentials import *
user = username
passwd = password
toemail = to_email

# https://myaccount.google.com/lesssecureapps
# Switch on access
# Try logging in
# When you see error, goback to your emails
# Email, with critical access issue, open the email and accept it
# https://myaccount.google.com/lesssecureapps
# Switch it on

orskl_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
orskl_server.login(user, passwd)
orskl_server.sendmail(
  toemail,
  toemail,
  "this message is from python")
orskl_server.quit()


import smtplib
from credentials import *

gmail = username
paswd = password
toemail = to_email

orskl_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
orskl_server.login(gmail, paswd)
orskl_server.sendmail(
  toemail,
  toemail,
  "this message is from python")
orskl_server.quit()


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
orskl_mail_content = '''Hi,
This is the class of Python for Beginners.
We are in Session 17 today.

Regards,
Pawan
'''
#The mail addresses and password
orskl_sender_address = user
orskl_sender_pass = passwd
orskl_receiver_address = toemail
#Setup the MIME
orskl_message = MIMEMultipart()
orskl_message['From'] = orskl_sender_address
orskl_message['To'] = orskl_receiver_address
orskl_message['Subject'] = 'Email through Python'   #The subject line

orskl_message.attach(MIMEText(orskl_mail_content, 'plain'))
#Create SMTP session for sending the mail
orskl_session =smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
orskl_session.starttls() #enable security
orskl_session.login(orskl_sender_address, orskl_sender_pass) #login with mail_id and password
orskl_text = orskl_message.as_string()
orskl_session.sendmail(orskl_sender_address, orskl_receiver_address, orskl_text)
orskl_session.quit()
print('Mail Sent')




