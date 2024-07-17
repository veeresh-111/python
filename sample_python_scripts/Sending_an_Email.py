import smtplib
from email.mime.text import MIMEText

msg = MIMEText('This is a test email.')
msg['Subject'] = 'Test'
msg['From'] = 'from@example.com'
msg['To'] = 'to@example.com'

with smtplib.SMTP('smtp.example.com') as server:
    server.send_message(msg)

print('Email sent')
