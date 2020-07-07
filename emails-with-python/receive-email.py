import imaplib, getpass, email
M = imaplib.IMAP4_SSL('imap.gmail.com')

email = getpass.getpass("Email: ")
password = getpass.getpass("Enter your password: ")
M.login(user,password)
M.list() #will show all your folders
M.select('inbox')
#typ ,data = M.search(None,'FROM example')
typ ,data = M.search(None,'SUBJECT "this is a test email for python"')
typ  #ok
email_id = data[0]
result, email_data = M.fetch(email_id,"(RFC822)") #RFC822 protocol
email_data

email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
    #if part.get_content_type() == "text/html": #if the link in email
        body = part.get_payload(decode=True)
        print(body)

# ALL'	Returns all messages in your email folder. Often there are size limits from imaplib. To change these use imaplib._MAXLINE = 100 , where 100 is whatever you want the limit to be.