class User:
    def registeruser(self,username,password,email):
        with open('Email.txt','a') as f:
            f.write("username:{username},password:{password},Email:{email}\n")

import logging
class Loggr:
    def writelogsystem(self,message):
        logging.basicConfig(filename='log.txt',level=logging.DEBUG)
        logging.debug(message)

import smtplib,ssl,json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class Email:
    def send_email(self,to_email,subject="User Register"):
        credintial={'fromuser':"sureshkadam283@gmail.com",'password':'Suresh@18'}
        # data= json.load(credintial)
        # print(data)
        smtp_server="smtp.gmail.com"
        port=465
        sender_email=str(credintial['fromuser'])
        password=str(credintial['password'])

        cotext=ssl.create_default_context()
        message=MIMEMultipart('alternative')

        message["From"]=sender_email
        message["To"]=to_email
        message["Subject"]=subject
        message_content=f'<h1>Successfully Register, Thanks For Register</h1>'
        part=MIMEText(message_content,"html")
        message.attach(part)

        with smtplib.SMTP_SSL(smtp_server,port,context=cotext) as server:
            server.login(sender_email,password)
            server.sendmail(sender_email,to_email,message.as_string())

        print(f'Successfuly send{to_email}')

class Rgistration:
    def registration_user(self,username,password,email):
        try:
            User().registeruser(username,password,email)
            Email().send_email(email,'You Have successfull registration')
        except Exception as f:
            Loggr().writelogsystem(f'Invalid credential{f}',)

r=Rgistration()
r.registration_user("suresh","Suresh@18","sachinkadam7179@gmail.com ",)


