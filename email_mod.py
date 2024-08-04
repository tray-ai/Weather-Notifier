import smtplib, os
from dotenv import load_dotenv

# Load env variables into file. 
load_dotenv()

def send_notification_message(msg):
   """ This function sends a email/text 
   message via the SMTP protocol."""

   # Create the connection to gmail smtp server. 
   server = smtplib.SMTP('smtp.gmail.com', 587)

   # Create a secure connection / encryption
   server.starttls()

   # Initate variables for login creds for gmail.
   email = os.getenv('EMAIL')
   password = os.getenv('PASSWORD')

   try:
      # Attempt to login to gmail.
      server.login(email, password)
   except smtplib.SMTPHeloError:
      print('The server did not respond properly.')
   except smtplib.SMTPNotSupportedError:
      print('The AUTH command is not supported by the server.')
   except smtplib.SMTPException:
      print('No suitable authentication method was found.')

   try:
      # Attempt to send the email/text message.
      server.sendmail(email, os.getenv('PUSHOVER_EMAIL'), msg)
   except smtplib.SMTPHeloError:
      print('The server did not respond properly.')
   except smtplib.SMTPRecipientsRefused:
      print('All recipents were refused. Nobody got the mail.')
   except smtplib.SMTPDataError:
      print('The server replied with an unexpected error code.')

   # Close the connection.
   server.quit()

