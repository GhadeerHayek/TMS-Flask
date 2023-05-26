
import smtplib, ssl
from email.message import EmailMessage
# def send_email():
#     # recipient = request.form['email']
#     # message = request.form['message']
#     # subject = request.form['subject']
 
#     # return mghelper.verify_manager(manager.email)

#     gmail_user = 'ayahs19302@gmail.com'
#     gmail_password = 'mylafamilia'
#     sent_from = gmail_user
#     # recipient credentials 
#     to = ['hudaelshawa@gmail.com']
#     subject = 'testting flask'
#     body = 'i hope it wokrls adipiscing elit'

#     email_text = """\
#     From: %s
#     To: %s
#     Subject: %s

#     %s
#     """ % (sent_from, ", ".join(to), subject, body)

#     try:
#         smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#         smtp_server.ehlo()
#         smtp_server.login(gmail_user, gmail_password)
#         smtp_server.sendmail(sent_from, to, email_text)
#         smtp_server.close()
#         print ("Email sent successfully!")
#     except Exception as ex:
#         print ("Something went wrong….",ex)


# def send():
#     port = 465  # For SSL
#     smtp_server = "smtp.gmail.com"
#     sender_email = "ghadirel.hayek.2001@gmail.com"  # Enter your address
#     receiver_email = "ayahs19302@gmail.com"  # Enter receiver address
#     password = input("Type your password and press enter: ")
#     message = """\
#     Subject: Hi there

#     This message is sent from Python."""

#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message)


# def generate_email(sender, recipient, subject, body, attachment_path):
#     # Creates an email with an attachement.
#     # Basic email formatting
#     message = email.message.EmailMessage()
#     message["From"] = sender
#     message["To"] = recipient
#     message["Subject"] = subject
#     message.set_content(body)

#     return message


# def send_email(message):
#     """Sends the message to the configured SMTP server."""
#     mail_server = smtplib.SMTP('localhost')
#     mail_server.send_message(message)
#     mail_server.quit()

# generate_email("ghadirel.hayek.2001@gmail.com", "ayahs19302@gmail", "testttt", "wkgflwgflwf")


sender_email = "ghadirel.hayek.2001@gmail.com" 
sender_pass = "ghadeer123"
receiver_email = "ralokag125@introace.com" 
subi = "test"
body = """u should see this """

em = EmailMessage()
em['From']
em['To']
em['Subject']
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender_email, sender_pass)
    smtp.sendmail(sender_email, receiver_email, em.as_string)