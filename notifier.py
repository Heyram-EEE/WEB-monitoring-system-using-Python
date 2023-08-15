from smtplib import SMTP_SSL, SMTP_SSL_PORT
from datetime import datetime
from twilio.rest import Client


SMTP_HOST = '#############'
SMTP_USER = '#############'
SMTP_PASS = '#############'



class notify:
    def sendmail(self,errortext,site,notimail):
        from_email = 'Site Notification <monitoring@he5.in>'  
        to_emails = [notimail]
        body = "Error Occured on Site \n"+site+" \nError: "+errortext
        headers = f"From: {from_email}\r\n"
        headers += f"To: {', '.join(to_emails)}\r\n" 
        headers += f"Subject: Error In Site - {site}\r\n"
        email_message = headers + "\r\n" + body  
        try:
            smtp_server = SMTP_SSL(SMTP_HOST, port=SMTP_SSL_PORT)
            smtp_server.login(SMTP_USER, SMTP_PASS)
            smtp_server.sendmail(from_email, to_emails, email_message)
            smtp_server.quit()
            print("Mail Sent")
        except Exception as e:    
            print(e)
    def sendsms(self,errortext,site,notisms):
        if(notisms != ''):
            account_sid = '#############'
            auth_token = '#############'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_='+16205019489',
                body="Error Occured on Site \n"+site+" \nError: "+errortext,
                to=notisms
            )
    def __init__(self,errortext,site,notids):
        self.sendmail(errortext,site,notids[0])
        self.sendsms(errortext,site,notids[1])


