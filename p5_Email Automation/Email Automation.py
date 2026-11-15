
import smtplib
from email.message import EmailMessage

# Create email message
msg = EmailMessage()
msg['Subject'] = 'Your Report Is Ready'
msg['From'] = 'your_email@gmail.com'
msg['To'] = 'recipient@example.com'

msg.set_content('Hello! Your report is ready.')

# Connect to SMTP server
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()

# Start secure connection
smtpObj.starttls()
smtpObj.ehlo()

# Login
smtpObj.login('your_email@gmail.com', 'YOUR_APP_PASSWORD')

# Send email
smtpObj.send_message(msg)

# Close connection
smtpObj.quit()

print('Email sent successfully!')
