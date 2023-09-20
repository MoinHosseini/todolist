from __future__ import absolute_import, unicode_literals
from celery import task

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

@task()
def task_number_one():
    # Do something..
    # Email details
    sender_email = "moinceuis8@gmail.com"
    receiver_email = "moinceuis8@gmail.com"
    subject = "Hello from Python!"
    message = "This is a test email."

    # SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "moinceuis8@gmail.com"
    smtp_password = "zwimnchktonrcgcp"

    # Create the email
    email = MIMEMultipart()
    email["From"] = sender_email
    email["To"] = receiver_email
    email["Subject"] = subject

    email.attach(MIMEText(message, "plain"))

    # Create a secure connection to the SMTP server
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()

    # Login to the SMTP server
    smtp.login(smtp_username, smtp_password)

    # Send the email
    smtp.sendmail(sender_email, receiver_email, email.as_string())

    # Close the SMTP connection
    smtp.quit()

    print("Email sent successfully!")
