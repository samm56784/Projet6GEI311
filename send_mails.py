
from twilio.rest import Client
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from datetime import datetime


def send_email(destination):

    mail = EmailMessage()

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string1 = now.strftime("%d%m%y_%H%M%S")

    mail = MIMEMultipart()

    email_text = MIMEText("Mouvement detected on the camera at " + dt_string)
    mail.attach(email_text)

    mail["From"] = "kaba74425@gmail.com"
    mail["Pass"] = "A9hk7G6RM8nr"
    mail["To"] = destination
    mail["Subject"] = "Alert - Mouvement detected"

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(mail["From"], mail["Pass"])

    except:
        print("Error logging")

    try:
        server.sendmail(mail["From"], mail["To"], mail.as_string())
        print("Email sent")
    except:
        print("Error sending email")
        return
    server.quit()
    return


def send_sms(destination):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    account_sid = "AC0552c4c15d8a3309b977acc3a3da9f30"
    auth_token = "25a6f579a31e9cd93bf74eb6626848c0"
    client = Client(account_sid, auth_token)


    message = client.messages.create(
        body="\ Suspicious movement detected. \n "
        "regarde ton mail. \n\n" + dt_string,
        from_='+15627847636',
        to=destination,
    )
    print(message.sid)


if __name__ == "__main__":
    # send_email()
    send_sms('+15814471678')