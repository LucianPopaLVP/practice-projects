import smtplib
from email.messages import EmailMessage

email = EmailMessage()
email['from'] = 'USTR '
email['to'] = '@gmail.com'
email['subject'] = 'Hello there! How Are you?'

email.set_content('I am ready to send lots of emails!')

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('@gmail.com', 'yourpassword')
    smtp.send_message(email)
    print('All done!')


