import smtplib

smtp_server = "mail.smtp2go.com"
smtp_port = 2525
smtp_username = "xxx"
smtp_password = "xxx"
# ^ these settings are correct, I modified them 1 by 1 to test the connection

from_email = "xxx@aitxxx.com"
to_email = "xxxi@gmail.com"

server = smtplib.SMTP(smtp_server, smtp_port)
# server.starttls()  # not necessary
try:
    server.login(smtp_username, smtp_password)
    server.sendmail(from_email, to_email, "Hello from Python without tls!")
    print("SMTP auth successful")
except smtplib.SMTPAuthenticationError:
    print("SMTP authentication failed")
server.quit()

# It works, I'm receiving the email in gmail