# Provider	SMTP server domain name
# Gmail (will need App Password)	smtp.gmail.com
# Yahoo Mail	smtp.mail.yahoo.com
# Outlook.com/Hotmail.com	smtp-mail.outlook.com
# AT&T	smpt.mail.att.net (Use port 465)
# Verizon	smtp.verizon.net (Use port 465)
# Comcast	smtp.comcast.net
import smtplib, getpass
smtp_object = smtplib.SMTP('smtp.gmail.com',587) #587 port 
smtp_object.ehlo()
smtp_object.starttls()
result = getpass.getpass("Type something here and it will be hidden: ")
print(result)
input("Enter your password")
#https://support.google.com/accounts/answer/185833?hl=en/
email = getpass.getpass("Enter your email: ")
password = getpass.getpass("Enter your password: ")
smtp_object.login(email,password)

from_address = getpass.getpass("Enter your email: ")
to_address = getpass.getpass("Enter the email of the recipient: ")
subject = input("Enter the subject line: ")
message = input("Type out the message you want to send: ")
msg = "Subject: " + subject + '\n' + message

smtp_object.sendmail(from_address,to_address,msg)

smtp_object.quit()