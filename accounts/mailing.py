import smtplib  # library of python to support Simple Mail Transfer Protocol
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_userID(user_mail, user_id_generated):
    # Initialisations of SMTP Object

    mail = smtplib.SMTP('smtp.gmail.com',
                        587)  # SMTP Object is setup using google's SMTP server and corresponding port number
    mail.ehlo()  # Used to 'Identify' itself
    mail.starttls()  # Activate Transport Layer Security for outgoing mail

    # Initialisations of sender and receiver

    # Enter your data here,I have removed my data
    sender = "noreplyaarohi2022@gmail.com"  # Enter mail id here
    sender_password = "aarohi@1234"  # Enter password here
    receiver = user_mail

    # Mail transfer

    mail.login(sender, sender_password)  # Login to the mail server as sender
    # Creating the header

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "AAROHI2022 Registration ID"
    msg['From'] = sender
    msg['To'] = receiver

    # Create the body of the message (a plain-text and an HTML version).
    text = '''Greetings User!You have successfully been registered to the AAROHI2022 Database!
    We have generated a special user id,unique to every user.For logging in to our website,you have to use this as your userID
    and the password is already set by you during registration.
    Your id is:''' + user_id_generated + '''.We hope you have a great day!
    Thank You!'''  # Content to send

    html = """\
    <html>
    <head></head>
    <body>
        <p>Greetings User!</p>
        <p>You have successfully been registered to the AAROHI-22 Database!
        We have generated a unique USER ID for you to log in to AAROHI website.</p>
        <h3>Your id is """ + str(user_id_generated) + """</h3>
        <p>Please use the password set by you during registration</p>
        <h3>Have a good day !</h3>
    </body>
    </html>"""

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # header='To:'+receiver+'\n'+'From:'+sender+'\n'+'subject:AAROHI2022 Registration ID\n'
    # content='''Greetings User!You have successfully been registered to the AAROHI2022 Database!
    # We have generated a special user id,unique to every user.For logging in to our website,you have to use this as your userID
    # and the password is already set by you during registration.
    # Your id is:'''+user_id_generated+'''.We hope you have a great day!
    # Thank You!'''    #Content to send
    # content=header+content

    mail.sendmail(sender, receiver, msg.as_string())
    mail.close()


def send_newPassword(user_mail, user_password):
    # Initialisations of SMTP Object

    mail = smtplib.SMTP('smtp.gmail.com',
                        587)  # SMTP Object is setup using google's SMTP server and corresponding port number
    mail.ehlo()  # Used to 'Identify' itself
    mail.starttls()  # Activate Transport Layer Security for outgoing mail

    # Initialisations of sender and receiver

    # Enter your data here,I have removed my data
    sender = "noreplyaarohi2022@gmail.com"  # Enter mail id here
    sender_password = "aarohi@1234"  # Enter password here
    receiver = user_mail

    # Mail transfer

    mail.login(sender, sender_password)  # Login to the mail server as sender
    # Creating the header

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "AAROHI 2022 Registration ID"
    msg['From'] = sender
    msg['To'] = receiver

    # Create the body of the message (a plain-text and an HTML version).
    text = '''
        Hi user,You recently requested a new password via reset/forgot password
        The new password is :
    ''' + user_password + " .Please dont share this with anyone,and after logging in,change your password to whatever you feel is comfortable"

    html = """\
    <html>
    <head></head>
    <body>
        <p>Greetings User!</p>
        <p>Hi user,You recently requested a new password via reset/forgot password</p>
        <h3>The new password is """ + str(user_password) + """</h3>
        <p>Please do not share this with anyone,and after logging in,change your password to whatever you feel is comfortable</p>
        <h3>Have a good day !</h3>
    </body>
    </html>"""

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # header='To:'+receiver+'\n'+'From:'+sender+'\n'+'subject:AXIS2021 Registration ID\n'
    # content='''
    #    Hi user,You recently requested a new password via reset/forgot password
    #    The new password is :
    # '''+  user_password +" .Please dont share this with anyone,and after logging in,change your password to whatever you feel is comfortable"  #Content to send
    # content=header+content

    mail.sendmail(sender, receiver, msg.as_string())
    mail.close()