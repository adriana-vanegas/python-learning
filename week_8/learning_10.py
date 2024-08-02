# Send Emails

from email.mime.multipart import MIMEMultipart
# MIME: stands for multipurpose internet mail extension
  # It serves to define the format of emails

# Multipart: serves to send a message in HTML or Plain Text Content


from email.mime.text import MIMEText
from email.mime.image import MIMEImage
# MIME text let's us write the body of a message as text or HTML

import smtplib
# This calls a server to send an email

message = MIMEMultipart()
message["from"] = "Adriana"
message["to"] = "xxx"
message["subject"] = "This is a test"

#To set the body, we need to attach it to message
message.attach(MIMEText("This is the body"))

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
  smtp.ehlo() # This initiates the SMTP server
  smtp.starttls() # All commands we send will be encrypted
  smtp.login("xxx","xxx")
  smtp.send_message(message)
  print("Sent")
